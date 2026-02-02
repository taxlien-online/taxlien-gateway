from fastapi import APIRouter, Depends, Query, Request
from typing import List, Optional
from app.models.worker import WorkResponse
from app.services.worker_queue import WorkerQueue
from app.core.redis import get_redis

router = APIRouter()

@router.get("/work", response_model=WorkResponse)
async def get_work(
    request: Request,
    capacity: int = Query(10, ge=1, le=100),
    platforms: List[str] = Query(...),
    redis = Depends(get_redis)
):
    """
    Parser workers pull tasks from this endpoint.
    Requires X-Worker-Token and X-Worker-ID.
    """
    auth = request.state.auth
    worker_id = auth.worker_id or "unknown"
    
    queue = WorkerQueue(redis)
    tasks = await queue.pop_tasks(
        worker_id=worker_id,
        platforms=platforms,
        capacity=capacity
    )
    
    return WorkResponse(
        tasks=tasks,
        retry_after=30 if not tasks else 5
    )
