from fastapi import APIRouter, Depends, Request
import structlog
import time
from app.models.worker import WorkerStatus
from app.core.redis import get_redis

logger = structlog.get_logger()
router = APIRouter()

@router.post("/heartbeat")
async def worker_heartbeat(
    request: Request,
    status: WorkerStatus,
    redis = Depends(get_redis)
):
    """
    Workers send periodic heartbeats to this endpoint.
    """
    auth = request.state.auth
    worker_id = auth.worker_id or "unknown"
    
    # Update worker status in Redis
    key = f"worker:{worker_id}:status"
    await redis.hset(key, mapping={
        "last_seen": time.time(),
        "active_tasks": status.active_tasks,
        "platforms": ",".join(status.platforms),
        "cpu": status.cpu_percent,
        "memory": status.memory_percent
    })
    await redis.expire(key, 300) # 5 minute TTL
    
    logger.info("heartbeat_received", worker_id=worker_id)
    
    return {"acknowledged": True, "commands": []}
