import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch, MagicMock
from app.main import app
from app.core.config import settings
from app.core.redis import get_redis

# Mock Redis Client
mock_redis = AsyncMock()

# Dependency Override
async def override_get_redis():
    return mock_redis

@pytest_asyncio.fixture(autouse=True)
def setup_redis_override():
    app.dependency_overrides[get_redis] = override_get_redis
    # Reset mock before each test
    mock_redis.reset_mock()
    yield
    app.dependency_overrides = {}

@pytest_asyncio.fixture
async def client():
    # Mock the rate limiter globally for all tests
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit:
        mock_limit.return_value = (True, 99) # allowed, remaining
        
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac

@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "gateway"}

@pytest.mark.asyncio
async def test_internal_work_unauthorized(client):
    response = await client.get("/internal/work?platforms=beacon")
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_internal_work_authorized(client):
    # Mock redis pop_tasks logic (which might use a different redis method or class)
    # Since pop_tasks is inside WorkerQueue, we still need to patch WorkerQueue or ensure it uses the injected redis.
    # WorkerQueue usually instantiates its own redis or uses the manager.
    # Let's verify if WorkerQueue uses get_redis dependency.
    # Usually internal endpoints use the global manager if not via dependency.
    # So we keep the patch for WorkerQueue.pop_tasks just in case.
    with patch("app.api.internal.work.WorkerQueue.pop_tasks", new_callable=AsyncMock) as mock_pop:
        mock_pop.return_value = []
        
        headers = {
            "X-Worker-Token": settings.INTERNAL_API_TOKEN,
            "X-Worker-ID": "test-worker-1"
        }
        response = await client.get("/internal/work?platforms=beacon", headers=headers)
        assert response.status_code == 200
        assert "tasks" in response.json()

@pytest.mark.asyncio
async def test_external_property_anonymous_limit(client):
    # Mock parser client and usage tracker
    with patch("app.services.http_client.ServiceClient.request", new_callable=AsyncMock) as mock_request, \
         patch("app.services.usage.UsageTracker.check_and_increment", new_callable=AsyncMock) as mock_usage:
        
        # Configure Mock Redis (Dependency Override)
        mock_redis.get.return_value = None # Cache miss
        
        mock_request.return_value.status_code = 200
        mock_request.return_value.content = b'{"id": "123"}'
        mock_request.return_value.headers = {"Content-Type": "application/json"}
        
        # Mock usage tracker to return True (allowed)
        mock_usage.return_value = True
        
        response = await client.get("/v1/properties/123")
        assert response.status_code == 200
        assert response.headers["X-Cache"] == "MISS"
        
        # Verify setex was called (caching)
        mock_redis.setex.assert_called()

@pytest.mark.asyncio
async def test_rate_limit_headers(client):
    response = await client.get("/health")
    assert "X-RateLimit-Remaining" in response.headers

@pytest.mark.asyncio
async def test_circuit_breaker_open():
    from app.services.http_client import ServiceClient, CircuitState
    
    service = ServiceClient("http://fail", "fail-service")
    breaker = service.breaker
    
    # Force open
    for _ in range(6):
        breaker.record_failure()
    
    assert breaker.state == CircuitState.OPEN
    assert breaker.can_execute() is False