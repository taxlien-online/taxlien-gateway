from redis.asyncio import Redis
import json
import hashlib
import structlog
from typing import Optional, Any
from app.core.redis import get_redis

logger = structlog.get_logger()

class CacheService:
    def __init__(self, redis: Redis):
        self.redis = redis

    def _generate_key(self, prefix: str, identifier: str, params: Optional[dict] = None) -> str:
        param_str = json.dumps(params, sort_keys=True) if params else ""
        param_hash = hashlib.md5(param_str.encode()).hexdigest() if param_str else "raw"
        return f"cache:{prefix}:{identifier}:{param_hash}"

    async def get(self, key: str) -> Optional[dict]:
        data = await self.redis.get(key)
        if data:
            logger.info("cache_hit", key=key)
            return json.loads(data)
        return None

    async def set(self, key: str, value: Any, ttl: int = 3600):
        await self.redis.setex(key, ttl, json.dumps(value))
        logger.info("cache_set", key=key, ttl=ttl)

async def get_cache_service() -> CacheService:
    redis = await get_redis()
    return CacheService(redis)
