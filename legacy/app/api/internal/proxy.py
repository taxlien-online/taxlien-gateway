from fastapi import APIRouter, Depends, Request, HTTPException
import httpx
import structlog
from app.models.worker import ProxyInfo
from app.core.config import settings

logger = structlog.get_logger()
router = APIRouter()

@router.get("/proxy/create", response_model=ProxyInfo)
async def create_proxy(
    request: Request,
    platform: str
):
    """
    Get or create a proxy for a specific platform.
    Proxies request to the internal tor-socks-proxy service.
    """
    # For MVP: Proxying to the internal service
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{settings.PROXY_SERVICE_URL}/create",
                params={"platform": platform},
                timeout=10.0
            )
            response.raise_for_status()
            return ProxyInfo(**response.json())
        except Exception as e:
            logger.error("proxy_creation_failed", platform=platform, error=str(e))
            # Fallback or error
            raise HTTPException(status_code=502, detail="Proxy service unavailable")

@router.post("/proxy/{port}/rotate", response_model=ProxyInfo)
async def rotate_proxy(
    port: int,
    request: Request,
    platform: str,
    reason: str = "banned"
):
    """
    Rotate a proxy that is banned or slow.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{settings.PROXY_SERVICE_URL}/rotate/{port}",
                params={"platform": platform, "reason": reason},
                timeout=10.0
            )
            response.raise_for_status()
            return ProxyInfo(**response.json())
        except Exception as e:
            logger.error("proxy_rotation_failed", port=port, error=str(e))
            raise HTTPException(status_code=502, detail="Proxy service unavailable")
