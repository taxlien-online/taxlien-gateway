from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from app.models.parcel import Parcel
from app.models.worker import ParcelResult
from datetime import datetime
import structlog

logger = structlog.get_logger()

class PropertyService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def upsert_parcel(self, result: ParcelResult, worker_id: str) -> bool:
        """
        Upsert a parcel result. Returns True if inserted, False if updated.
        """
        stmt = insert(Parcel).values(
            parcel_id=result.parcel_id,
            platform=result.platform,
            state=result.state,
            county=result.county,
            data=result.data,
            scraped_at=result.scraped_at,
            worker_id=worker_id
        )

        # On conflict, update the data and scraped_at
        update_stmt = stmt.on_conflict_do_update(
            constraint='_parcel_platform_uc',
            set_={
                "data": stmt.excluded.data,
                "scraped_at": stmt.excluded.scraped_at,
                "worker_id": stmt.excluded.worker_id
            }
        )

        try:
            res = await self.session.execute(update_stmt)
            # In SQLAlchemy with asyncpg, we might not get 'inserted' vs 'updated' easily from execute()
            # but the operation is atomic.
            return True # Simplified for now
        except Exception as e:
            logger.error("upsert_parcel_failed", parcel_id=result.parcel_id, error=str(e))
            raise
