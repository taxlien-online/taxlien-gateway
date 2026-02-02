from fastapi import APIRouter, Depends, Request, HTTPException
from starlette.responses import Response
import structlog
from app.services.http_client import ServiceClient
from app.core.config import settings

from app.services.cache import get_cache_service
from app.core.redis import get_redis

from app.core.authorization import enforce_tier

logger = structlog.get_logger()
router = APIRouter()

parser_client = ServiceClient(settings.PARSER_SERVICE_URL, "parser")

@router.get("/properties/{parcel_id}")
async def get_property(
    parcel_id: str, 
    request: Request, 
    redis = Depends(get_redis),
    _tier_check = Depends(enforce_tier("daily_details"))
):
    """
    Proxy request to Parser Service for property details.
    """
    auth = request.state.auth
    
    # Cache key depends on parcel_id and user tier (since visibility might vary)
    cache_key = f"cache:prop:{parcel_id}:{auth.tier.value}"
    
    # Try cache
    cached_data = await redis.get(cache_key)
    if cached_data:
        return Response(
            content=cached_data,
            media_type="application/json",
            headers={"X-Cache": "HIT"}
        )

    headers = {
        "X-User-ID": auth.user_id or "anonymous",
        "X-User-Tier": auth.tier.value,
        "X-Request-ID": request.headers.get("X-Request-ID", "")
    }
    
    try:
        response = await parser_client.request(
            "GET", 
            f"/api/v1/properties/{parcel_id}",
            headers=headers
        )
        
        if response.status_code == 200:
            # Cache successful response for 1 hour
            await redis.setex(cache_key, 3600, response.content)
            
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("Content-Type"),
            headers={"X-Cache": "MISS"}
        )
    except Exception as e:
        logger.error("proxy_property_failed", parcel_id=parcel_id, error=str(e))
        raise HTTPException(status_code=502, detail="Upstream service error")

@router.get("/properties")
async def search_properties(request: Request):
    """
    Proxy request to Parser Service for property search.
    """
    auth = request.state.auth
    headers = {
        "X-User-ID": auth.user_id or "anonymous",
        "X-User-Tier": auth.tier.value
    }
    
    try:
        response = await parser_client.request(
            "GET", 
            "/api/v1/properties",
            params=dict(request.query_params),
            headers=headers
        )
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("Content-Type")
        )
    except Exception as e:
        logger.error("proxy_search_failed", error=str(e))
        raise HTTPException(status_code=502, detail="Upstream service error")
