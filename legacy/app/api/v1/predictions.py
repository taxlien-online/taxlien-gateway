from fastapi import APIRouter, Depends, Request, HTTPException
from starlette.responses import Response
import structlog
import json
from app.services.http_client import ServiceClient
from app.core.config import settings
from app.core.redis import get_redis
from app.core.authorization import enforce_tier

logger = structlog.get_logger()
router = APIRouter()

ml_client = ServiceClient(settings.ML_SERVICE_URL, "ml")

@router.post("/predictions/batch")
async def get_predictions_batch(
    request: Request, 
    redis = Depends(get_redis),
    _tier_check = Depends(enforce_tier("ai_analysis"))
):
    """
    Proxy request to ML Service for batch predictions.
    """
    auth = request.state.auth
    
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON body")

    headers = {
        "X-User-ID": auth.user_id or "anonymous",
        "X-User-Tier": auth.tier.value,
        "Content-Type": "application/json"
    }
    
    try:
        response = await ml_client.request(
            "POST", 
            "/api/v1/predict/batch",
            json=body,
            headers=headers
        )
        
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("Content-Type")
        )
    except Exception as e:
        logger.error("proxy_predictions_failed", error=str(e))
        raise HTTPException(status_code=502, detail="Upstream ML service error")
