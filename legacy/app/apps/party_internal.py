from fastapi import FastAPI
from app.core.config import settings
from app.core.auth import AuthMiddleware
from app.core.metrics import PrometheusMiddleware
from app.api.internal import router as internal_router

def create_party_internal_app() -> FastAPI:
    """Create Internal Party API FastAPI application (:8082)."""
    app = FastAPI(
        title=f"{settings.PROJECT_NAME} Internal Party API",
        version=settings.VERSION,
        debug=settings.DEBUG,
    )

    # Set up Metrics
    app.add_middleware(PrometheusMiddleware)

    # Set up Auth
    app.add_middleware(AuthMiddleware)

    # Include Internal Routers
    # In future, we can filter routers to include only party-relevant ones
    app.include_router(internal_router)

    @app.get("/health")
    async def health_check():
        return {"status": "ok", "service": "gateway", "app": "party_internal"}

    return app
