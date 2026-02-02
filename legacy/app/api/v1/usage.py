from fastapi import APIRouter, Depends, Request
from app.services.usage import UsageTracker, get_usage_service
import structlog

logger = structlog.get_logger()
router = APIRouter()

@router.get("")
async def get_usage(
    request: Request,
    usage_tracker: UsageTracker = Depends(get_usage_service)
):
    """
    Get usage statistics for the current user.
    """
    auth = request.state.auth
    user_id = auth.user_id or "anonymous"
    
    usage_stats = await usage_tracker.get_user_usage(user_id)
    
    return {
        "user_id": user_id,
        "tier": auth.tier,
        "usage": usage_stats
    }
