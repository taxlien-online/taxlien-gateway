from fastapi import APIRouter, Depends, Request, HTTPException
from starlette.responses import Response
import structlog
from app.services.http_client import ServiceClient
from app.core.config import settings
from app.core.authorization import enforce_tier

logger = structlog.get_logger()
router = APIRouter()

parser_client = ServiceClient(settings.PARSER_SERVICE_URL, "parser")

@router.get("/address")
async def search_by_address(
    request: Request,
    _tier_check = Depends(enforce_tier("search"))
):
    """
    Proxy request to Parser Service for address search.
    """
    auth = request.state.auth
    headers = {
        "X-User-ID": auth.user_id or "anonymous",
        "X-User-Tier": auth.tier.value
    }
    
    try:
        response = await parser_client.request(
            "GET", 
            "/api/v1/search/address",
            params=dict(request.query_params),
            headers=headers
        )
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("Content-Type")
        )
    except Exception as e:
        logger.error("proxy_search_address_failed", error=str(e))
        raise HTTPException(status_code=502, detail="Upstream service error")

@router.get("/owner")
async def search_by_owner(
    request: Request,
    _tier_check = Depends(enforce_tier("search"))
):
    """
    Proxy request to Parser Service for owner search.
    """
    auth = request.state.auth
    headers = {
        "X-User-ID": auth.user_id or "anonymous",
        "X-User-Tier": auth.tier.value
    }
    
    try:
        response = await parser_client.request(
            "GET", 
            "/api/v1/search/owner",
            params=dict(request.query_params),
            headers=headers
        )
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("Content-Type")
        )
    except Exception as e:
        logger.error("proxy_search_owner_failed", error=str(e))
        raise HTTPException(status_code=502, detail="Upstream service error")
