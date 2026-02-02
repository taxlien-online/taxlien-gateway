from redis.asyncio import Redis
import datetime
import structlog
from app.models.auth import UserTier
from app.core.redis import get_redis
from fastapi import Depends

logger = structlog.get_logger()

# Daily limits config
TIER_LIMITS = {
    UserTier.ANONYMOUS: {"daily_search": 5, "daily_details": 10},
    UserTier.FREE: {"daily_search": 20, "daily_details": 50},
    UserTier.STARTER: {"daily_search": 1000, "daily_details": 2000},
    UserTier.PREMIUM: {"daily_search": -1, "daily_details": -1}, # -1 = unlimited
    UserTier.INTERNAL: {"daily_search": -1, "daily_details": -1},
}

class UsageTracker:
    def __init__(self, redis: Redis):
        self.redis = redis

    def _get_key(self, user_id: str, feature: str) -> str:
        date_str = datetime.date.today().isoformat()
        return f"usage:{user_id}:{feature}:{date_str}"

    async def check_and_increment(self, user_id: str, tier: UserTier, feature: str) -> bool:
        limit = TIER_LIMITS.get(tier, {}).get(feature, 0)
        if limit == -1:
            return True
        if limit == 0:
            return False

        key = self._get_key(user_id, feature)
        current = await self.redis.incr(key)
        if current == 1:
            await self.redis.expire(key, 86400) # 24 hours
            
        if current > limit:
            logger.warning("tier_limit_exceeded", user_id=user_id, tier=tier, feature=feature)
            return False
        
        return True

    async def get_user_usage(self, user_id: str) -> dict:
        """
        Get current usage for all tracked features.
        """
        date_str = datetime.date.today().isoformat()
        features = ["daily_search", "daily_details"]
        results = {}
        
        for feature in features:
            key = f"usage:{user_id}:{feature}:{date_str}"
            val = await self.redis.get(key)
            results[feature] = int(val) if val else 0
            
        return results

async def get_usage_service(redis: Redis = Depends(get_redis)) -> UsageTracker:
    return UsageTracker(redis)