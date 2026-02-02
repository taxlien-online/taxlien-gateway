from fastapi import APIRouter, Depends, Request
from typing import List
import structlog
from app.models.worker import ParcelResult, SubmitResponse
from app.services.worker_queue import WorkerQueue
from app.services.properties import PropertyService
from app.core.redis import get_redis
from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

logger = structlog.get_logger()
router = APIRouter()

@router.post("/results", response_model=SubmitResponse)
async def submit_results(
    request: Request,
    results: List[ParcelResult],
    redis = Depends(get_redis),
    db: AsyncSession = Depends(get_db)
):
    """
    Parser workers submit results to this endpoint.
    Data is persisted to PostgreSQL and tasks are marked as complete in the queue.
    """
    auth = request.state.auth
    worker_id = auth.worker_id or "unknown"
    
    queue = WorkerQueue(redis)
    property_service = PropertyService(db)
    
    inserted = 0
    updated = 0
    failed = 0
    errors = []
    
    for res in results:
        try:
            # 1. Persist to PostgreSQL
            is_new = await property_service.upsert_parcel(res, worker_id)
            if is_new:
                inserted += 1
            else:
                updated += 1
                
            # 2. Mark task as completed in the queue
            await queue.complete_task(worker_id, res.task_id)
            
            logger.info("result_processed", task_id=res.task_id, parcel_id=res.parcel_id, worker_id=worker_id)
        except Exception as e:
            failed += 1
            errors.append(str(e))
            logger.error("result_processing_failed", task_id=res.task_id, error=str(e))
            
    return SubmitResponse(
        inserted=inserted,
        updated=updated,
        failed=failed,
        errors=errors
    )
