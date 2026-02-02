import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch
from app.main import app
from app.core.config import settings
from app.models.auth import UserTier

@pytest_asyncio.fixture
async def client():
    # Mock rate limiter and other infrastructure to isolate auth
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit:
        mock_limit.return_value = (True, 100)
        
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac

@pytest.mark.asyncio
async def test_worker_auth_success(client):
    headers = {
        "X-Worker-Token": settings.INTERNAL_API_TOKEN,
        "X-Worker-ID": "test-worker"
    }
    # Using /internal/monitoring as a test endpoint for internal auth
    response = await client.get("/internal/monitoring/heartbeat", headers=headers)
    # If the endpoint exists and auth passes, we expect something other than 401
    assert response.status_code != 401

@pytest.mark.asyncio
async def test_worker_auth_invalid_token(client):
    headers = {
        "X-Worker-Token": "wrong-token",
        "X-Worker-ID": "test-worker"
    }
    response = await client.get("/internal/monitoring/heartbeat", headers=headers)
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "UNAUTHORIZED"

@pytest.mark.asyncio
async def test_internal_route_protected(client):
    # No headers
    response = await client.get("/internal/monitoring/heartbeat")
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "UNAUTHORIZED"

@pytest.mark.asyncio
async def test_firebase_auth_mock_success(client):
    # Enable Firebase mock mode by ensuring project ID is set (or by patching verify_id_token)
    with patch("app.core.auth.firebase_auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "user-123", "tier": "premium"}
        
        # We need to ensure FIREBASE_PROJECT_ID is seen as set in the middleware logic
        with patch("app.core.auth.settings.FIREBASE_PROJECT_ID", "test-project"):
            headers = {"Authorization": "Bearer valid-token"}
            response = await client.get("/health", headers=headers)
            assert response.status_code == 200
            # Health check doesn't check auth, but middleware runs. 
            # We can check if auth context was injected if we had an endpoint that returns it.

@pytest.mark.asyncio
async def test_firebase_auth_invalid_token(client):
    with patch("app.core.auth.firebase_auth.verify_id_token") as mock_verify:
        mock_verify.side_effect = Exception("Invalid token")
        
        with patch("app.core.auth.settings.FIREBASE_PROJECT_ID", "test-project"):
            headers = {"Authorization": "Bearer invalid-token"}
            # Any route will trigger the middleware
            response = await client.get("/health", headers=headers)
            assert response.status_code == 401
            assert response.json()["error"]["code"] == "UNAUTHORIZED"

@pytest.mark.asyncio
async def test_anonymous_access_health(client):
    # Health check should be accessible anonymously
    response = await client.get("/health")
    assert response.status_code == 200
