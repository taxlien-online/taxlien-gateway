from redis.asyncio import Redis
import time
import structlog

logger = structlog.get_logger()

# Lua script for atomic Token Bucket
# KEYS[1] - ratelimit key
# ARGV[1] - current timestamp
# ARGV[2] - refill rate (tokens/sec)
# ARGV[3] - burst capacity
# ARGV[4] - requested tokens
TOKEN_BUCKET_LUA = """
local key = KEYS[1]
local now = tonumber(ARGV[1])
local rate = tonumber(ARGV[2])
local burst = tonumber(ARGV[3])
local requested = tonumber(ARGV[4])

local state = redis.call('HMGET', key, 'tokens', 'updated_at')
local last_tokens = tonumber(state[1]) or burst
local last_updated = tonumber(state[2]) or now

local delta = math.max(0, now - last_updated)
local new_tokens = math.min(burst, last_tokens + delta * rate)

if new_tokens >= requested then
    redis.call('HMSET', key, 'tokens', new_tokens - requested, 'updated_at', now)
    redis.call('EXPIRE', key, 3600)
    return {1, math.floor(new_tokens - requested)}
else
    return {0, math.floor(new_tokens)}
end
"""

class RateLimiter:
    def __init__(self, redis: Redis):
        self.redis = redis
        self._script = None

    async def check(self, key: str, rate: float, burst: int, requested: int = 1):
        if self._script is None:
            self._script = self.redis.register_script(TOKEN_BUCKET_LUA)
        
        allowed, remaining = await self._script(
            keys=[key],
            args=[time.time(), rate, burst, requested]
        )
        return bool(allowed), remaining

async def is_rate_limited(redis: Redis, identifier: str, tier: str) -> tuple[bool, int]:
    # Simplified limits for now
    limits = {
        "anonymous": (0.1, 5),    # 1 req per 10s, burst 5
        "free": (0.5, 10),       # 1 req per 2s, burst 10
        "starter": (1.0, 20),    # 1 req per 1s, burst 20
        "premium": (2.0, 50),    # 2 req per 1s, burst 50
        "internal": (10.0, 100)  # 10 req per 1s, burst 100
    }
    
    rate, burst = limits.get(tier, limits["anonymous"])
    key = f"ratelimit:{tier}:{identifier}"
    
    limiter = RateLimiter(redis)
    return await limiter.check(key, rate, burst)
