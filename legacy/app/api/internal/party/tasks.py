from fastapi import APIRouter, Depends, Path, Request
import structlog
from app.services.worker_queue import WorkerQueue
from app.core.redis import get_redis

logger = structlog.get_logger()
router = APIRouter()

@router.post("/tasks/{task_id}/complete")
async def complete_task(
    request: Request,
    task_id: str = Path(...),
    redis = Depends(get_redis)
):
    """
    Mark a task as completed.
    """
    auth = request.state.auth
    worker_id = auth.worker_id or "unknown"
    
    queue = WorkerQueue(redis)
    success = await queue.complete_task(worker_id, task_id)
    
    return {"success": success}

@router.post("/tasks/{task_id}/fail")
async def fail_task(
    request: Request,
    task_id: str = Path(...),
    redis = Depends(get_redis)
):
    """
    Mark a task as failed. In MVP: just log it.
    TODO: Implement retry logic or DLQ.
    """
    auth = request.state.auth
    worker_id = auth.worker_id or "unknown"
    
    logger.error("task_failed", worker_id=worker_id, task_id=task_id)
    
    return {"status": "reported"}
