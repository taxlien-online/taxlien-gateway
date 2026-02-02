from fastapi import APIRouter
from app.api.v1.properties import router as properties_router
from app.api.v1.predictions import router as predictions_router
from app.api.v1.search import router as search_router
from app.api.v1.top_lists import router as top_lists_router
from app.api.v1.usage import router as usage_router

router = APIRouter(prefix="/v1", tags=["v1"])
router.include_router(properties_router)
router.include_router(predictions_router)
router.include_router(search_router, prefix="/search")
router.include_router(top_lists_router, prefix="/top-lists")
router.include_router(usage_router, prefix="/usage")
