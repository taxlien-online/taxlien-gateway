import pytest
import pytest_asyncio
import json
import httpx
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch, MagicMock
from app.main import app
from app.core.config import settings
from app.models.worker import WorkTask
from app.core.redis import get_redis
from app.core.db import get_db

# Mock Redis
mock_redis = AsyncMock()
# Mock DB Session
mock_db = AsyncMock()

async def override_get_redis():
    return mock_redis

async def override_get_db():
    yield mock_db

@pytest_asyncio.fixture(autouse=True)
def setup_overrides():
    app.dependency_overrides[get_redis] = override_get_redis
    app.dependency_overrides[get_db] = override_get_db
    yield
    app.dependency_overrides = {}

@pytest_asyncio.fixture
async def client():
    # Mock rate limiter and redis manager to avoid real connections
    with patch("app.core.ratelimit.is_rate_limited", new_callable=AsyncMock) as mock_limit, \
         patch("app.core.redis.redis_manager.connect", new_callable=AsyncMock), \
         patch("app.core.redis.redis_manager.redis", new_callable=AsyncMock):
        mock_limit.return_value = (True, 100)
        
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            yield ac

@pytest.mark.asyncio
async def test_get_work_flow(client):
    headers = {
        "X-Worker-Token": settings.INTERNAL_API_TOKEN,
        "X-Worker-ID": "worker-123"
    }
    
    task = WorkTask(task_id="t1", platform="beacon", target={"url": "test.com"})
    with patch("app.api.internal.work.WorkerQueue.pop_tasks", new_callable=AsyncMock) as mock_pop:
        mock_pop.return_value = [task]
        
        response = await client.get("/internal/work?platforms=beacon&capacity=5", headers=headers)
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["tasks"]) == 1
        assert data["tasks"][0]["task_id"] == "t1"

@pytest.mark.asyncio
async def test_submit_results_flow(client):
    headers = {
        "X-Worker-Token": settings.INTERNAL_API_TOKEN,
        "X-Worker-ID": "worker-123"
    }
    
    results = [{
        "task_id": "t1",
        "parcel_id": "p1",
        "platform": "beacon",
        "state": "FL",
        "county": "Orange",
        "data": {"owner": "test"},
        "parse_duration_ms": 100
    }]
    
    with patch("app.api.internal.results.WorkerQueue.complete_task", new_callable=AsyncMock) as mock_complete, \
         patch("app.api.internal.results.PropertyService.upsert_parcel", new_callable=AsyncMock) as mock_upsert:
        mock_complete.return_value = True
        mock_upsert.return_value = True # True means inserted
        
        response = await client.post("/internal/results", json=results, headers=headers)
        
        assert response.status_code == 200
        assert response.json()["inserted"] == 1

@pytest.mark.asyncio
async def test_heartbeat_flow(client):
    headers = {
        "X-Worker-Token": settings.INTERNAL_API_TOKEN,
        "X-Worker-ID": "worker-123"
    }
    
    status = {
        "active_tasks": 0,
        "completed_last_minute": 0,
        "failed_last_minute": 0,
        "platforms": ["beacon"],
        "cpu_percent": 10.5,
        "memory_percent": 20.0
    }
    
    mock_redis.reset_mock()
    response = await client.post("/internal/heartbeat", json=status, headers=headers)
    
    assert response.status_code == 200
    assert response.json()["acknowledged"] is True
    mock_redis.hset.assert_called_once()

@pytest.mark.asyncio
async def test_proxy_endpoints(client):
    headers = {
        "X-Worker-Token": settings.INTERNAL_API_TOKEN,
        "X-Worker-ID": "worker-123"
    }
    
    # Setup mock response
    mock_resp = MagicMock(spec=httpx.Response)
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "host": "proxy-host",
        "port": 8888,
        "type": "socks5"
    }
    
    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_resp
        
        response = await client.get("/internal/proxy/create?platform=beacon", headers=headers)
        
        assert response.status_code == 200
        assert response.json()["host"] == "proxy-host"
