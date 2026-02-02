import pytest
import json
from unittest.mock import AsyncMock, MagicMock
from app.services.worker_queue import WorkerQueue
from app.models.worker import WorkTask

@pytest.fixture
def mock_redis():
    return AsyncMock()

@pytest.fixture
def worker_queue(mock_redis):
    return WorkerQueue(mock_redis)

@pytest.mark.asyncio
async def test_push_task(worker_queue, mock_redis):
    task = WorkTask(
        task_id="task-1",
        platform="beacon",
        target={"parcel_id": "123"},
        priority=1
    )
    await worker_queue.push_task(task)
    
    # Check if lpush was called with the right key and data
    queue_key = "queue:beacon:p1"
    mock_redis.lpush.assert_called_once()
    args, _ = mock_redis.lpush.call_args
    assert args[0] == queue_key
    assert json.loads(args[1])["task_id"] == "task-1"

@pytest.mark.asyncio
async def test_pop_tasks_priority_order(worker_queue, mock_redis):
    # Setup mock to return a task only for p1
    task_p1 = WorkTask(task_id="urgent", platform="beacon", target={}, priority=1)
    task_p2 = WorkTask(task_id="normal", platform="beacon", target={}, priority=2)
    
    # We want to simulate rpoplpush returning None for p1, p2, p3... except one
    mock_redis.rpoplpush.side_effect = [
        task_p1.model_dump_json(), # beacon p1
        None, # beacon p2 (shouldn't even be called if capacity is 1)
    ]
    
    tasks = await worker_queue.pop_tasks("worker-1", ["beacon"], capacity=1)
    
    assert len(tasks) == 1
    assert tasks[0].task_id == "urgent"
    # Verify rpoplpush was called for p1
    mock_redis.rpoplpush.assert_called_with("queue:beacon:p1", "processing:worker-1")

@pytest.mark.asyncio
async def test_complete_task_success(worker_queue, mock_redis):
    task = WorkTask(task_id="task-1", platform="beacon", target={}, priority=3)
    raw_task = task.model_dump_json()
    
    mock_redis.lrange.return_value = [raw_task]
    
    result = await worker_queue.complete_task("worker-1", "task-1")
    
    assert result is True
    mock_redis.lrem.assert_called_once_with("processing:worker-1", 1, raw_task)

@pytest.mark.asyncio
async def test_complete_task_not_found(worker_queue, mock_redis):
    mock_redis.lrange.return_value = []
    
    result = await worker_queue.complete_task("worker-1", "task-1")
    
    assert result is False
    mock_redis.lrem.assert_not_called()
