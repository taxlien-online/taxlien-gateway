import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch
from app.main import app
from app.core.config import settings

@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_rate_limit_allowed(client):
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit:
        mock_limit.return_value = (True, 5)
        
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.headers["X-RateLimit-Remaining"] == "5"

@pytest.mark.asyncio
async def test_rate_limit_exceeded(client):
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit:
        mock_limit.return_value = (False, 0)
        
        response = await client.get("/health")
        assert response.status_code == 429
        assert response.json()["error"]["code"] == "RATE_LIMIT_EXCEEDED"
        assert response.headers["X-RateLimit-Remaining"] == "0"

@pytest.mark.asyncio
async def test_rate_limit_uses_internal_tier(client):
    # Use real AuthMiddleware with internal token
    headers = {
        "X-Worker-Token": settings.INTERNAL_API_TOKEN,
        "X-Worker-ID": "test-worker"
    }
    
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit:
        mock_limit.return_value = (True, 99)
        
        response = await client.get("/health", headers=headers)
        assert response.status_code == 200
        
        # Verify is_rate_limited was called with internal tier
        args, kwargs = mock_limit.call_args
        # args[2] is tier
        assert args[2] == "internal"
