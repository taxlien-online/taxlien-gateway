from fastapi import Request, HTTPException, Depends
from app.models.auth import UserTier
from app.services.usage import UsageTracker
from app.core.redis import get_redis

def enforce_tier(feature: str):
    async def dependency(request: Request, redis = Depends(get_redis)):
        auth = request.state.auth
        user_id = auth.user_id or request.client.host
        
        tracker = UsageTracker(redis)
        allowed = await tracker.check_and_increment(user_id, auth.tier, feature)
        
        if not allowed:
            raise HTTPException(
                status_code=403,
                detail={
                    "code": "TIER_LIMIT_EXCEEDED",
                    "message": f"Daily limit for {feature} exceeded. Upgrade your tier.",
                    "upgrade_url": "https://taxlien.online/pricing"
                }
            )
        return True
    return dependency
