from fastapi import APIRouter
from app.api.internal.parcel import router as parcel_router
from app.api.internal.party import router as party_router
from app.api.internal.monitoring import router as monitoring_router
from app.api.internal.proxy import router as proxy_router
from app.api.internal.raw_files import router as raw_files_router

router = APIRouter(prefix="/internal", tags=["internal"])
router.include_router(parcel_router)
router.include_router(party_router)
router.include_router(monitoring_router)
router.include_router(proxy_router)
router.include_router(raw_files_router)