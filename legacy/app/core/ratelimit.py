from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import structlog
from app.core.redis import get_redis
from app.services.ratelimit import is_rate_limited
from app.models.auth import AuthContext

logger = structlog.get_logger()

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Determine identifier (IP for now, later User ID)
        client_ip = request.client.host if request.client else "unknown"
        
        # Use tier from AuthContext
        auth_context = getattr(request.state, "auth", AuthContext())
        t = auth_context.tier
        tier = t.value if hasattr(t, "value") else str(t)
        identifier = auth_context.user_id or auth_context.worker_id or client_ip
        
        redis = await get_redis()
        allowed, remaining = await is_rate_limited(redis, identifier, tier)
        
        if not allowed:
            logger.warning("rate_limit_exceeded", ip=client_ip, tier=tier)
            return JSONResponse(
                status_code=429,
                content={
                    "error": {
                        "code": "RATE_LIMIT_EXCEEDED",
                        "message": "Too many requests. Please slow down."
                    }
                },
                headers={"X-RateLimit-Remaining": str(remaining)}
            )
            
        response = await call_next(request)
        response.headers["X-RateLimit-Remaining"] = str(remaining)
        return response
