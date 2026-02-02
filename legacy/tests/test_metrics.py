import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch
from app.main import app

@pytest_asyncio.fixture
async def client():
    # Mock rate limiter and redis manager
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit, \
         patch("app.core.redis.redis_manager.connect", new_callable=AsyncMock), \
         patch("app.core.redis.redis_manager.redis", new_callable=AsyncMock):
        mock_limit.return_value = (True, 100)
        
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac

@pytest.mark.asyncio
async def test_metrics_endpoint(client):
    # Trigger some requests to generate metrics
    await client.get("/health")
    
    response = await client.get("/metrics")
    assert response.status_code == 200
    assert "gateway_requests_total" in response.text