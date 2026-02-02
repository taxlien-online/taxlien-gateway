from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings
import structlog

logger = structlog.get_logger()

class Base(DeclarativeBase):
    pass

class DatabaseManager:
    def __init__(self):
        self.engine = create_async_engine(
            settings.DATABASE_URL,
            echo=settings.DEBUG,
            future=True
        )
        self.async_session_maker = async_sessionmaker(
            self.engine, 
            class_=AsyncSession, 
            expire_on_commit=False
        )

    async def disconnect(self):
        await self.engine.dispose()
        logger.info("database_disconnected")

db_manager = DatabaseManager()

async def get_db():
    async with db_manager.async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
