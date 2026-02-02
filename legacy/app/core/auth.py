from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import structlog
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
from app.core.config import settings
from app.models.auth import AuthContext, UserTier

logger = structlog.get_logger()

# Initialize Firebase
def init_firebase():
    if not settings.FIREBASE_PROJECT_ID:
        logger.info("firebase_not_configured", message="Running without Firebase validation (Dev Mode)")
        return
        
    try:
        if settings.FIREBASE_CREDENTIALS_PATH:
            cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
            firebase_admin.initialize_app(cred)
        else:
            firebase_admin.initialize_app()
        logger.info("firebase_initialized")
    except Exception as e:
        logger.error("firebase_init_failed", error=str(e))

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_context = AuthContext()
        
        # 1. Check for Worker Token (Internal)
        worker_token = request.headers.get("X-Worker-Token")
        if worker_token:
            if worker_token == settings.INTERNAL_API_TOKEN:
                auth_context.tier = UserTier.INTERNAL
                auth_context.worker_id = request.headers.get("X-Worker-ID", "unknown")
            else:
                return JSONResponse(
                    status_code=401,
                    content={"error": {"code": "UNAUTHORIZED", "message": "Invalid worker token"}}
                )

        # 2. Check for Firebase Token (External)
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer ") and auth_context.tier == UserTier.ANONYMOUS:
            token = auth_header[7:]
            try:
                # In Dev Mode without Firebase, we might want to bypass or use a mock
                if not settings.FIREBASE_PROJECT_ID:
                    # Mock validation for development
                    auth_context.user_id = "mock-user-123"
                    auth_context.tier = UserTier.FREE
                else:
                    decoded_token = firebase_auth.verify_id_token(token)
                    auth_context.user_id = decoded_token["uid"]
                    # Map custom claims or check DB for tier
                    auth_context.tier = decoded_token.get("tier", UserTier.FREE)
            except Exception as e:
                logger.warning("invalid_firebase_token", error=str(e))
                return JSONResponse(
                    status_code=401,
                    content={"error": {"code": "UNAUTHORIZED", "message": "Invalid or expired session"}}
                )

        # Protect /internal routes
        if request.url.path.startswith("/internal") and auth_context.tier != UserTier.INTERNAL:
            logger.warning("unauthorized_internal_access", path=request.url.path)
            return JSONResponse(
                status_code=401,
                content={"error": {"code": "UNAUTHORIZED", "message": "Internal access required"}}
            )

        # Inject context into request state
        request.state.auth = auth_context
        
        response = await call_next(request)
        return response
