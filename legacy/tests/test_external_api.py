import pytest
import pytest_asyncio
import httpx
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch, MagicMock
from app.main import app
from app.core.redis import get_redis

# Mock Redis
mock_redis = AsyncMock()

async def override_get_redis():
    return mock_redis

@pytest_asyncio.fixture(autouse=True)
def setup_overrides():
    app.dependency_overrides[get_redis] = override_get_redis
    # Default mock values
    mock_redis.incr.return_value = 1
    mock_redis.get.return_value = None
    yield
    app.dependency_overrides = {}

@pytest_asyncio.fixture
async def client():
    # Mock rate limiter and other infra
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit:
        mock_limit.return_value = (True, 100)
        
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac

@pytest.mark.asyncio
async def test_get_property_cache_hit(client):
    mock_redis.get.return_value = b'{"parcel_id": "p1", "owner": "Cached John"}'
    
    response = await client.get("/v1/properties/p1")
    
    assert response.status_code == 200
    assert response.json()["owner"] == "Cached John"
    assert response.headers["X-Cache"] == "HIT"

@pytest.mark.asyncio
async def test_get_property_cache_miss_proxy_success(client):
    mock_redis.get.return_value = None
    
    # Setup mock response from ServiceClient
    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 200
    mock_resp.content = b'{"parcel_id": "p1", "owner": "Real John"}'
    mock_resp.headers = {"Content-Type": "application/json"}
    
    with patch("app.services.http_client.ServiceClient.request", new_callable=AsyncMock) as mock_request:
        mock_request.return_value = mock_resp
        
        response = await client.get("/v1/properties/p1")
        
        assert response.status_code == 200
        assert response.json()["owner"] == "Real John"
        assert response.headers["X-Cache"] == "MISS"
        # Verify it was cached
        mock_redis.setex.assert_called()

@pytest.mark.asyncio
async def test_tier_limit_enforced(client):
    mock_redis.get.return_value = None
    
    # Mock UsageTracker to return False (limit exceeded)
    with patch("app.services.usage.UsageTracker.check_and_increment", new_callable=AsyncMock) as mock_usage:
        mock_usage.return_value = False
        
        response = await client.get("/v1/properties/p1")
        
        assert response.status_code == 403
        # Current implementation uses 'detail' from HTTPException
        assert response.json()["detail"]["code"] == "TIER_LIMIT_EXCEEDED"

@pytest.mark.asyncio
async def test_circuit_breaker_behavior(client):
    from app.services.http_client import ServiceClient, CircuitState
    
    client_service = ServiceClient("http://test-service", "test")
    # Reset state
    client_service.breaker.failures = 0
    client_service.breaker.state = CircuitState.CLOSED
    
    with patch("httpx.AsyncClient.request", new_callable=AsyncMock) as mock_req:
        mock_req.side_effect = httpx.ConnectError("Connection failed", request=None)
        
        # Trigger failures up to threshold (default 5)
        for _ in range(5):
            try:
                await client_service.request("GET", "/")
            except httpx.ConnectError:
                pass
        
        assert client_service.breaker.state == CircuitState.OPEN
        assert client_service.breaker.can_execute() is False
        
        # Request should now fail immediately via circuit breaker
        with pytest.raises(httpx.HTTPStatusError, match="Circuit breaker is OPEN"):
            await client_service.request("GET", "/")