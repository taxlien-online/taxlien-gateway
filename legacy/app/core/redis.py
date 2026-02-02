from redis.asyncio import Redis, from_url
from app.core.config import settings
import structlog

logger = structlog.get_logger()

class RedisManager:
    def __init__(self):
        self.redis: Redis | None = None

    async def connect(self):
        try:
            self.redis = from_url(settings.REDIS_URL, decode_responses=True)
            await self.redis.ping()
            logger.info("redis_connected", url=settings.REDIS_URL)
        except Exception as e:
            logger.error("redis_connection_failed", error=str(e))
            raise

    async def disconnect(self):
        if self.redis:
            await self.redis.close()
            logger.info("redis_disconnected")

redis_manager = RedisManager()

async def get_redis() -> Redis:
    if redis_manager.redis is None:
        await redis_manager.connect()
    return redis_manager.redis
