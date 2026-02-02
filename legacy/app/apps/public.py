from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.ratelimit import RateLimitMiddleware
from app.core.auth import AuthMiddleware
from app.core.metrics import PrometheusMiddleware
from app.api.v1 import router as v1_router

def create_public_app() -> FastAPI:
    """Create Public API FastAPI application (:8080)."""
    app = FastAPI(
        title=f"{settings.PROJECT_NAME} Public API",
        version=settings.VERSION,
        debug=settings.DEBUG,
    )

    # Set up CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Set up Metrics
    app.add_middleware(PrometheusMiddleware)

    # Set up Auth and Rate Limiting
    # Note: Currently AuthMiddleware and RateLimitMiddleware handle both.
    # We might want to specialize them later for public vs internal.
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(AuthMiddleware)

    # Include Public Routers
    app.include_router(v1_router)

    @app.get("/health")
    async def health_check():
        return {"status": "ok", "service": "gateway", "app": "public"}

    return app
