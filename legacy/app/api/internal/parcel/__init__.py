from fastapi import APIRouter
from .work import router as work_router
from .results import router as results_router
from .tasks import router as tasks_router

router = APIRouter(prefix="/parcel", tags=["internal-parcel"])
router.include_router(work_router)
router.include_router(results_router)
router.include_router(tasks_router)
