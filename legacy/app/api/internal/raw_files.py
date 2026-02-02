from fastapi import APIRouter, Depends, Request, UploadFile, File, Form
import structlog
import os
import aiofiles
from app.core.config import settings

logger = structlog.get_logger()
router = APIRouter()

@router.post("/raw-files")
async def upload_raw_file(
    request: Request,
    file: UploadFile = File(...),
    metadata: str = Form(...)
):
    """
    Upload raw HTML/PDF from workers.
    Saves to local storage defined in settings.
    """
    auth = request.state.auth
    worker_id = auth.worker_id or "unknown"
    
    # Ensure storage path exists
    storage_path = "/Users/anton/proj/TAXLIEN.online/taxlien-sdd/data/raw" # Fallback
    os.makedirs(storage_path, exist_ok=True)
    
    file_path = os.path.join(storage_path, file.filename)
    
    try:
        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)
            
        logger.info("raw_file_uploaded", worker_id=worker_id, file=file.filename)
        return {"status": "ok", "path": file_path}
    except Exception as e:
        logger.error("raw_file_upload_failed", error=str(e))
        return {"status": "error", "message": str(e)}
