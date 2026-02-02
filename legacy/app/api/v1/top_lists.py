from fastapi import APIRouter, Depends, Request, HTTPException
from starlette.responses import Response
import structlog
from app.services.http_client import ServiceClient
from app.core.config import settings
from app.core.authorization import enforce_tier

logger = structlog.get_logger()
router = APIRouter()

ml_client = ServiceClient(settings.ML_SERVICE_URL, "ml")

@router.get("/{strategy}")
async def get_top_list(
    strategy: str,
    request: Request,
    _tier_check = Depends(enforce_tier("top_lists"))
):
    """
    Proxy request to ML Service for top lists based on strategy.
    """
    auth = request.state.auth
    headers = {
        "X-User-ID": auth.user_id or "anonymous",
        "X-User-Tier": auth.tier.value
    }
    
    try:
        response = await ml_client.request(
            "GET", 
            f"/api/v1/top-lists/{strategy}",
            params=dict(request.query_params),
            headers=headers
        )
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("Content-Type")
        )
    except Exception as e:
        logger.error("proxy_top_lists_failed", strategy=strategy, error=str(e))
        raise HTTPException(status_code=502, detail="Upstream ML service error")
