# Specifications: API Gateway

**Version:** 1.0
**Status:** SPECIFICATIONS
**Last Updated:** 2026-01-18
**Tech Stack:** FastAPI, Redis, Firebase Admin SDK, Prometheus

---

## System Architecture - Tri-Port Design

**Key Architectural Decision:** Single service running THREE FastAPI applications on separate ports.

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                GATEWAY SERVICE (Single Process)                                   │
├───────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                   │
│   ┌───────────────────────────┐    ┌───────────────────────────┐    ┌───────────────────────────┐ │
│   │   PUBLIC API APP (:8080)  │    │  PARCEL INTERNAL (:8081)  │    │   PARTY INTERNAL (:8082)  │ │
│   │   api.taxlien.online      │    │  parcel-api.taxlien.local │    │   party-api.taxlien.local │ │
│   ├───────────────────────────┤    ├───────────────────────────┤    ├───────────────────────────┤ │
│   │                           │    │                           │    │                           │ │
│   │ MIDDLEWARE CHAIN:         │    │ MIDDLEWARE CHAIN:         │    │ MIDDLEWARE CHAIN:         │ │
│   │ ├─ Firebase/API Key Auth  │    │ ├─ Worker Token Auth      │    │ ├─ Worker Token Auth      │ │
│   │ ├─ Tier-based Rate Limit  │    │ ├─ Parcel-specific Limits │    │ ├─ Party-specific Limits  │ │
│   │ ├─ Response Caching       │    │ └─ Request Logging        │    │ └─ Request Logging        │ │
│   │                           │    │                           │    │                           │ │
│   │ ENDPOINTS:                │    │ ENDPOINTS:                │    │ ENDPOINTS:                │ │
│   │ GET /v1/properties/*      │    │ GET  /internal/work       │    │ GET  /internal/work       │ │
│   │ GET /v1/search/*          │    │ POST /internal/results    │    │ POST /internal/results    │ │
│   │ GET /v1/top-lists/*       │    │ POST /internal/heartbeat  │    │ GET  /internal/documents  │ │
│   │                           │    │                           │    │                           │ │
│   └───────────────────────────┘    └───────────────────────────┘    └───────────────────────────┘ │
│                    │                              │                               │               │
│                    └──────────────┬───────────────┴───────────────┬───────────────┘               │
│                                   │                               │                               │
│                                   ▼                               ▼                               │
│   ┌─────────────────────────────────────────────────────────────────────────────────────────────┐ │
│   │                                    SHARED CORE SERVICES                                     │ │
│   │                                                                                             │ │
│   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐    │ │
│   │  │  PostgreSQL  │  │    Redis     │  │   Storage    │  │   Queues     │  │   Metrics   │    │ │
│   │  │  (Parcels)   │  │  (Parties)   │  │   (Raw HTML) │  │ (Tasks/Job)  │  │ (Prometheus)│    │ │
│   │  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘  └─────────────┘    │ │
│   │                                                                                             │ │
│   └─────────────────────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                                   │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Data Flow:**

```
┌─────────────┐                     ┌─────────────────────────────────────────────┐
│ Flutter App │─────────────────────│                                             │
│   (User)    │  Firebase JWT       │         PUBLIC API (:8080)                  │
└─────────────┘        │            │                                             │
                       ▼            │  ┌─────────────────────────────────────┐    │
                   port:8080 ──────▶│  │ CORS → Firebase Auth → Rate Limit  │────┼───▶ Response
                                    │  │        → Cache → Route             │    │
┌─────────────┐                     │  └─────────────────────────────────────┘    │
│  SSR Site   │─────────────────────│                                             │
│ (Next.js)   │  X-SSR-Token        └─────────────────────────────────────────────┘
└─────────────┘

┌─────────────┐                     ┌─────────────────────────────────────────────┐
│Parser Worker│─────────────────────│                                             │
│ (Machine A) │  X-Worker-Token     │         INTERNAL API (:8081)                │
└─────────────┘        │            │                                             │
                       ▼            │  ┌─────────────────────────────────────┐    │
                   port:8081 ──────▶│  │ Worker Auth → IP Whitelist → Route │────┼───▶ Tasks/Results
                                    │  └─────────────────────────────────────┘    │
┌─────────────┐                     │                                             │
│Parser Worker│─────────────────────│                                             │
│ (Cloud VM)  │  X-Worker-Token     └─────────────────────────────────────────────┘
└─────────────┘
```

---

## tor-socks-proxy: NOT Gateway's Responsibility

**Gateway has ZERO knowledge of tor-socks-proxy.**

Workers manage their own proxy connections independently:
- Workers know `TOR_PROXY_HOST` and `TOR_PROXY_PORT` from their own environment
- Workers connect directly to tor-socks-proxy
- Gateway never sees proxy configuration

```
┌─────────────┐                              ┌─────────────────┐
│   Gateway   │                              │ tor-socks-proxy │
│             │                              │                 │
│  Tasks only │     ┌─────────────┐          │  SOCKS5 only    │
│  No proxy   │◄────│   WORKER    │─────────►│                 │
│  knowledge  │     │             │          │  (independent)  │
└─────────────┘     └─────────────┘          └─────────────────┘
      │                   │
      │ GET /internal/work│ SOCKS5://tor:9050
      │ POST /internal/results
      │ POST /internal/heartbeat
```

**Gateway endpoints (NO proxy endpoints):**
- `GET /internal/work` - Pull tasks
- `POST /internal/results` - Submit parsed data
- `POST /internal/raw-files` - Upload HTML
- `POST /internal/tasks/{id}/*` - Report status
- `POST /internal/heartbeat` - Status pulse

**Removed from Gateway:**
- ~~`GET /internal/proxy/create`~~ - Worker knows proxy config
- ~~`POST /internal/proxy/{port}/rotate`~~ - Worker manages directly
- ~~`POST /internal/proxy/{port}/ban`~~ - Not Gateway's concern

---

## 1. Project Structure (Dual-Port Architecture)

```
gateway/
├── main.py                          # Entry point: runs BOTH apps concurrently
├── config.py                        # Shared settings (ports, tokens, URLs)
├── dependencies.py                  # Shared dependency injection
│
├── apps/                            # THREE SEPARATE FASTAPI APPLICATIONS
│   ├── __init__.py
│   ├── public.py                    # Public API app (:8080)
│   ├── parcel_internal.py           # Internal Parcel API app (:8081)
│   └── party_internal.py            # Internal Party API app (:8082)
│
├── api/                             # Route handlers (separated by app)
│   ├── __init__.py
│   ├── public/                      # Public API routes (/v1/*)
│   │   └── ...
│   └── internal/                    # Internal API routes
│       ├── parcel/                  # Parcel worker routes
│       │   ├── work.py
│       │   ├── results.py
│       │   └── tasks.py
│       ├── party/                   # Party worker routes
│       │   ├── work.py
│       │   ├── results.py
│       │   └── documents.py
│       └── heartbeat.py             # Shared heartbeat
│
├── middleware/                      # Middleware chains (separated by app)
│   ├── __init__.py
│   ├── public/                      # Public API middleware
│   │   ├── __init__.py
│   │   ├── cors.py                  # CORS configuration
│   │   ├── firebase_auth.py         # Firebase token validation
│   │   ├── rate_limit.py            # Tier-based rate limiting
│   │   ├── cache.py                 # Response caching
│   │   └── request_id.py            # X-Request-ID injection
│   │
│   └── internal/                    # Internal API middleware
│       ├── __init__.py
│       ├── worker_auth.py           # X-Worker-Token validation
│       ├── ip_whitelist.py          # Optional IP restrictions
│       └── logging.py               # Structured request logging
│
├── core/                            # SHARED core services (used by both apps)
│   ├── __init__.py
│   ├── database.py                  # AsyncPG connection pool
│   ├── redis.py                     # Redis connection
│   └── storage.py                   # Raw file storage
│
├── services/                        # SHARED business logic
│   ├── __init__.py
│   ├── task_queue.py                # Redis queue management
│   ├── cache.py                     # Redis response cache
│   ├── worker_registry.py           # Worker tracking
│   └── properties.py                # PostgreSQL queries
│
├── models/                          # Shared Pydantic models
│   ├── __init__.py
│   ├── task.py                      # Task, WorkTask models
│   ├── parcel.py                    # ParcelResult, Property models
│   └── worker.py                    # WorkerStatus, HeartbeatResponse
│
├── metrics.py                       # Prometheus metrics (shared)
│
└── tests/
    ├── conftest.py                  # Fixtures (both apps)
    ├── test_public_auth.py          # Public API auth tests
    ├── test_internal_auth.py        # Internal API auth tests
    ├── test_rate_limit.py           # Rate limiting tests
    ├── test_public_api.py           # Public API integration tests
    └── test_internal_api.py         # Internal API integration tests
```

---

## 2. Configuration (Dual-Port)

**File:** `gateway/config.py`

```python
from pydantic_settings import BaseSettings
from typing import Optional, Set
from functools import lru_cache

class Settings(BaseSettings):
    # Server - DUAL PORT CONFIGURATION
    host: str = "0.0.0.0"
    public_port: int = 8080      # Public API port
    internal_port: int = 8081    # Internal API port
    debug: bool = False

    # Database
    postgres_url: str
    redis_url: str = "redis://localhost:6379"

    # Authentication - Public API
    firebase_project_id: str
    firebase_credentials_path: Optional[str] = None
    ssr_service_token: str

    # Authentication - Internal API
    worker_tokens: str  # Comma-separated: "token1,token2,token3"
    internal_ip_whitelist: Optional[str] = None  # Comma-separated IPs, or None to disable

    # Services
    raw_storage_path: str = "/data/raw"

    # Rate Limiting
    rate_limit_enabled: bool = True

    # Cache (Public API only)
    cache_ttl_properties: int = 3600      # 1 hour
    cache_ttl_search: int = 900           # 15 min
    cache_ttl_predictions: int = 86400    # 24 hours

    # Worker Management (Internal API only)
    worker_heartbeat_timeout: int = 300   # 5 minutes
    dead_worker_check_interval: int = 60  # 1 minute
    internal_rate_limit_per_worker: int = 1000  # req/min per worker

    @property
    def worker_tokens_set(self) -> Set[str]:
        return set(self.worker_tokens.split(",")) if self.worker_tokens else set()

    @property
    def ip_whitelist_set(self) -> Optional[Set[str]]:
        if not self.internal_ip_whitelist:
            return None
        return set(self.internal_ip_whitelist.split(","))

    class Config:
        env_file = ".env"
        env_prefix = "GATEWAY_"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
```

**File:** `gateway/main.py` - Entry Point Running Both Apps

```python
import asyncio
import uvicorn
from gateway.config import get_settings
from gateway.apps.public import create_public_app
from gateway.apps.internal import create_internal_app
from gateway.core.database import init_database, close_database
from gateway.core.redis import init_redis, close_redis

settings = get_settings()

async def run_servers():
    """Run both Public and Internal API servers concurrently."""

    # Initialize shared resources
    await init_database()
    await init_redis()

    # Create both FastAPI applications
    public_app = create_public_app()
    internal_app = create_internal_app()

    # Configure uvicorn servers
    public_config = uvicorn.Config(
        public_app,
        host=settings.host,
        port=settings.public_port,
        log_level="info",
    )
    internal_config = uvicorn.Config(
        internal_app,
        host=settings.host,
        port=settings.internal_port,
        log_level="info",
    )

    public_server = uvicorn.Server(public_config)
    internal_server = uvicorn.Server(internal_config)

    try:
        # Run both servers concurrently
        await asyncio.gather(
            public_server.serve(),
            internal_server.serve(),
        )
    finally:
        # Cleanup shared resources
        await close_database()
        await close_redis()

if __name__ == "__main__":
    asyncio.run(run_servers())
```

**File:** `gateway/apps/public.py` - Public API Application

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gateway.middleware.public.firebase_auth import FirebaseAuthMiddleware
from gateway.middleware.public.rate_limit import RateLimitMiddleware
from gateway.middleware.public.cache import CacheMiddleware
from gateway.middleware.public.request_id import RequestIDMiddleware
from gateway.api.public import properties, search, predictions, top_lists, usage
from gateway.config import get_settings

def create_public_app() -> FastAPI:
    """Create Public API FastAPI application (:8080)."""
    settings = get_settings()

    app = FastAPI(
        title="TAXLIEN.online Public API",
        description="Public API for Flutter app, SSR site, and B2B clients",
        version="1.0.0",
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
    )

    # Middleware chain (order matters: first added = last executed)
    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(CacheMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(FirebaseAuthMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://taxlien.online", "https://app.taxlien.online"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["Authorization", "X-API-Key", "X-SSR-Token"],
    )

    # Routes
    app.include_router(properties.router, prefix="/v1")
    app.include_router(search.router, prefix="/v1")
    app.include_router(predictions.router, prefix="/v1")
    app.include_router(top_lists.router, prefix="/v1")
    app.include_router(usage.router, prefix="/v1")

    @app.get("/health")
    async def health():
        return {"status": "healthy", "app": "public"}

    return app
```

**File:** `gateway/apps/internal.py` - Internal API Application

```python
from fastapi import FastAPI
from gateway.middleware.internal.worker_auth import WorkerAuthMiddleware
from gateway.middleware.internal.ip_whitelist import IPWhitelistMiddleware
from gateway.middleware.internal.logging import LoggingMiddleware
from gateway.api.internal import work, results, raw_files, tasks, heartbeat
from gateway.config import get_settings

def create_internal_app() -> FastAPI:
    """Create Internal API FastAPI application (:8081)."""
    settings = get_settings()

    app = FastAPI(
        title="TAXLIEN.online Internal API",
        description="Internal API for Parser Workers only",
        version="1.0.0",
        docs_url="/docs" if settings.debug else None,
        redoc_url=None,  # No redoc for internal
    )

    # Middleware chain (simpler than public)
    app.add_middleware(LoggingMiddleware)
    if settings.ip_whitelist_set:
        app.add_middleware(IPWhitelistMiddleware)
    app.add_middleware(WorkerAuthMiddleware)

    # Routes
    app.include_router(work.router, prefix="/internal")
    app.include_router(results.router, prefix="/internal")
    app.include_router(raw_files.router, prefix="/internal")
    app.include_router(tasks.router, prefix="/internal")
    app.include_router(heartbeat.router, prefix="/internal")

    @app.get("/health")
    async def health():
        return {"status": "healthy", "app": "internal"}

    return app
```

---

## 3. Authentication Module

### 3.1 Authenticator

**File:** `gateway/auth/authenticator.py`

```python
from fastapi import Request, HTTPException
from firebase_admin import auth as firebase_auth
from typing import Optional
from dataclasses import dataclass
from enum import Enum
import hashlib
import time

class AuthMethod(Enum):
    FIREBASE = "firebase"
    SSR_TOKEN = "ssr"
    API_KEY = "api_key"
    WORKER_TOKEN = "worker"
    ANONYMOUS = "anonymous"

@dataclass
class User:
    id: str
    tier: str                    # anonymous, free, starter, premium, enterprise
    auth_method: AuthMethod
    email: Optional[str] = None

@dataclass
class AuthResult:
    authenticated: bool
    user: Optional[User]
    error: Optional[str] = None

class Authenticator:
    def __init__(self, settings):
        self.settings = settings
        self._firebase_cache = {}  # token -> (user, expires_at)
        self._worker_tokens = set(settings.worker_tokens.split(","))

    async def authenticate(self, request: Request) -> AuthResult:
        """
        Authenticate request using multiple methods.
        Order: Firebase → SSR → Worker → API Key → Anonymous
        """
        # 1. Firebase ID Token (Bearer)
        if auth_header := request.headers.get("Authorization"):
            if auth_header.startswith("Bearer "):
                token = auth_header[7:]
                return await self._validate_firebase_token(token)

        # 2. SSR Service Token
        if ssr_token := request.headers.get("X-SSR-Token"):
            return self._validate_ssr_token(ssr_token)

        # 3. Worker Token (Internal API only)
        if worker_token := request.headers.get("X-Worker-Token"):
            worker_id = request.headers.get("X-Worker-ID", "unknown")
            return self._validate_worker_token(worker_token, worker_id)

        # 4. API Key
        if api_key := request.headers.get("X-API-Key"):
            return await self._validate_api_key(api_key)

        # 5. Anonymous
        return AuthResult(
            authenticated=False,
            user=User(id="anonymous", tier="anonymous", auth_method=AuthMethod.ANONYMOUS)
        )

    async def _validate_firebase_token(self, token: str) -> AuthResult:
        """Validate Firebase ID token with 5-minute cache."""
        # Check cache
        cache_key = hashlib.sha256(token.encode()).hexdigest()[:16]
        if cached := self._firebase_cache.get(cache_key):
            user, expires_at = cached
            if time.time() < expires_at:
                return AuthResult(authenticated=True, user=user)

        try:
            decoded = firebase_auth.verify_id_token(token)
            user = User(
                id=decoded["uid"],
                tier=decoded.get("tier", "free"),
                auth_method=AuthMethod.FIREBASE,
                email=decoded.get("email")
            )
            # Cache for 5 minutes
            self._firebase_cache[cache_key] = (user, time.time() + 300)
            return AuthResult(authenticated=True, user=user)
        except Exception as e:
            return AuthResult(authenticated=False, user=None, error=str(e))

    def _validate_ssr_token(self, token: str) -> AuthResult:
        """Validate SSR service token (constant-time comparison)."""
        import secrets
        if secrets.compare_digest(token, self.settings.ssr_service_token):
            return AuthResult(
                authenticated=True,
                user=User(id="ssr-service", tier="internal", auth_method=AuthMethod.SSR_TOKEN)
            )
        return AuthResult(authenticated=False, user=None, error="Invalid SSR token")

    def _validate_worker_token(self, token: str, worker_id: str) -> AuthResult:
        """Validate parser worker token."""
        if token in self._worker_tokens:
            return AuthResult(
                authenticated=True,
                user=User(id=f"worker:{worker_id}", tier="worker", auth_method=AuthMethod.WORKER_TOKEN)
            )
        return AuthResult(authenticated=False, user=None, error="Invalid worker token")

    async def _validate_api_key(self, api_key: str) -> AuthResult:
        """Validate API key from database."""
        # Query PostgreSQL for API key
        # SELECT user_id, tier FROM api_keys WHERE key_hash = $1 AND active = true
        # Placeholder implementation:
        return AuthResult(authenticated=False, user=None, error="API key validation not implemented")
```

### 3.2 Authorizer

**File:** `gateway/auth/authorizer.py`

```python
from dataclasses import dataclass
from typing import Optional
from .models import User

@dataclass
class AuthzResult:
    allowed: bool
    reason: Optional[str] = None
    remaining: Optional[int] = None
    upgrade_to: Optional[str] = None

class Authorizer:
    """Tier-based access control."""

    # Feature limits by tier (-1 = unlimited)
    LIMITS = {
        "anonymous": {
            "search": 5,
            "details": 10,
            "predictions": 0,
            "top_lists": 0,
            "bulk_export": 0,
            "on_demand_scrape": 0,
        },
        "free": {
            "search": 10,
            "details": 20,
            "predictions": 3,
            "top_lists": 0,
            "bulk_export": 0,
            "on_demand_scrape": 0,
        },
        "starter": {
            "search": -1,
            "details": -1,
            "predictions": 10,
            "top_lists": 10,    # Top 10 only
            "bulk_export": 0,
            "on_demand_scrape": 0,
        },
        "premium": {
            "search": -1,
            "details": -1,
            "predictions": -1,
            "top_lists": -1,
            "bulk_export": 1000,
            "on_demand_scrape": 10,
        },
        "enterprise": {
            "search": -1,
            "details": -1,
            "predictions": -1,
            "top_lists": -1,
            "bulk_export": -1,
            "on_demand_scrape": 100,
        },
        "internal": {
            "search": -1,
            "details": -1,
            "predictions": -1,
            "top_lists": -1,
            "bulk_export": -1,
            "on_demand_scrape": -1,
        },
        "worker": {
            "internal_api": -1,
        }
    }

    def __init__(self, redis):
        self.redis = redis

    async def authorize(self, user: User, action: str) -> AuthzResult:
        """Check if user is authorized for action."""
        tier_limits = self.LIMITS.get(user.tier, {})
        limit = tier_limits.get(action, 0)

        # No access
        if limit == 0:
            return AuthzResult(
                allowed=False,
                reason="tier_restriction",
                upgrade_to=self._suggest_upgrade(user.tier, action)
            )

        # Unlimited
        if limit == -1:
            return AuthzResult(allowed=True)

        # Check usage counter
        usage_key = f"usage:{user.id}:{action}:{self._today()}"
        usage = int(await self.redis.get(usage_key) or 0)

        if usage >= limit:
            return AuthzResult(
                allowed=False,
                reason="limit_exceeded",
                remaining=0,
                upgrade_to=self._suggest_upgrade(user.tier, action)
            )

        # Increment usage
        await self.redis.incr(usage_key)
        await self.redis.expire(usage_key, 86400)  # 24h TTL

        return AuthzResult(allowed=True, remaining=limit - usage - 1)

    def _today(self) -> str:
        from datetime import date
        return date.today().isoformat()

    def _suggest_upgrade(self, current_tier: str, action: str) -> Optional[str]:
        """Suggest which tier enables this action."""
        tier_order = ["anonymous", "free", "starter", "premium", "enterprise"]
        current_idx = tier_order.index(current_tier) if current_tier in tier_order else -1

        for tier in tier_order[current_idx + 1:]:
            if self.LIMITS.get(tier, {}).get(action, 0) != 0:
                return tier
        return None
```

---

## 4. Rate Limiting

**File:** `gateway/middleware/rate_limit.py`

```python
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Token bucket rate limiting."""

    # Tier-based limits
    LIMITS = {
        "anonymous": {"rate": 10/60, "burst": 5},      # 10/min, burst 5
        "free": {"rate": 30/60, "burst": 10},          # 30/min, burst 10
        "starter": {"rate": 60/60, "burst": 20},       # 60/min, burst 20
        "premium": {"rate": 120/60, "burst": 50},      # 120/min, burst 50
        "enterprise": {"rate": 600/60, "burst": 100},  # 600/min, burst 100
        "internal": {"rate": 1000/60, "burst": 200},   # Internal services
        "worker": {"rate": 1000/60, "burst": 200},     # Workers
    }

    def __init__(self, app, redis):
        super().__init__(app)
        self.redis = redis

    async def dispatch(self, request: Request, call_next):
        # Skip health checks
        if request.url.path in ["/health", "/metrics"]:
            return await call_next(request)

        # Get user from request state (set by auth middleware)
        user = getattr(request.state, "user", None)
        tier = user.tier if user else "anonymous"
        identifier = user.id if user else request.client.host

        # Check rate limit
        result = await self._check_limit(identifier, tier)

        if not result["allowed"]:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded",
                headers={
                    "Retry-After": str(result["retry_after"]),
                    "X-RateLimit-Limit": str(result["limit"]),
                    "X-RateLimit-Remaining": "0",
                    "X-RateLimit-Reset": str(result["reset_at"]),
                }
            )

        response = await call_next(request)

        # Add rate limit headers
        response.headers["X-RateLimit-Limit"] = str(result["limit"])
        response.headers["X-RateLimit-Remaining"] = str(result["remaining"])
        response.headers["X-RateLimit-Reset"] = str(result["reset_at"])

        return response

    async def _check_limit(self, identifier: str, tier: str) -> dict:
        """Token bucket algorithm in Redis."""
        config = self.LIMITS.get(tier, self.LIMITS["anonymous"])
        key = f"ratelimit:{identifier}"

        now = time.time()

        # Get current state
        data = await self.redis.hmget(key, "tokens", "updated")
        tokens = float(data[0]) if data[0] else config["burst"]
        last_update = float(data[1]) if data[1] else now

        # Refill tokens
        elapsed = now - last_update
        tokens = min(config["burst"], tokens + elapsed * config["rate"])

        if tokens < 1:
            return {
                "allowed": False,
                "retry_after": int((1 - tokens) / config["rate"]),
                "limit": int(config["rate"] * 60),
                "remaining": 0,
                "reset_at": int(now + (1 - tokens) / config["rate"]),
            }

        # Consume token
        new_tokens = tokens - 1
        await self.redis.hmset(key, {"tokens": new_tokens, "updated": now})
        await self.redis.expire(key, 3600)

        return {
            "allowed": True,
            "limit": int(config["rate"] * 60),
            "remaining": int(new_tokens),
            "reset_at": int(now + (config["burst"] - new_tokens) / config["rate"]),
        }
```

---

## 5. Internal API Endpoints

### 5.1 Work Distribution

**File:** `gateway/routes/internal/work.py`

```python
from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from datetime import datetime
from ...services.queue import QueueService
from ...services.proxy_pool import ProxyPoolService
from ...models.task import WorkTask, WorkResponse, ProxyInfo
from ...auth.authenticator import User
from ...dependencies import get_current_worker

router = APIRouter(prefix="/internal", tags=["Internal API"])

@router.get("/work", response_model=WorkResponse)
async def get_work(
    capacity: int = Query(default=10, ge=1, le=100),
    platforms: Optional[List[str]] = Query(default=None),
    max_tier: int = Query(default=4, ge=1, le=4),
    worker: User = Depends(get_current_worker),
    queue: QueueService = Depends(),
    proxy_pool: ProxyPoolService = Depends(),
):
    """
    Worker pulls tasks from queue (PULL model).

    Gateway logic:
    1. Filter platforms by worker capability
    2. Check proxy availability per platform
    3. Select tasks with priority ordering
    4. Assign proxy to each task
    5. Return task batch
    """
    worker_id = worker.id.split(":")[1]  # Extract from "worker:xyz"

    # Get available platforms based on proxy health
    available_platforms = []
    for platform in (platforms or ["beacon", "qpublic", "floridatax"]):
        proxy_count = await proxy_pool.get_available_count(platform)
        if proxy_count > 0:
            available_platforms.append(platform)

    if not available_platforms:
        return WorkResponse(tasks=[], retry_after=60)

    # Fetch tasks from queue
    tasks = await queue.fetch_tasks(
        platforms=available_platforms,
        limit=capacity,
        worker_id=worker_id,
    )

    if not tasks:
        return WorkResponse(tasks=[], retry_after=30)

    # Assign proxies to tasks
    work_tasks = []
    for task in tasks:
        proxy = await proxy_pool.allocate(task.platform, worker_id)

        work_tasks.append(WorkTask(
            task_id=task.id,
            platform=task.platform,
            state=task.state,
            county=task.county,
            parcel_id=task.parcel_id,
            priority=task.priority,
            url=task.url,
            proxy=ProxyInfo(
                host=proxy.host,
                port=proxy.port,
                type="socks5",
            ) if proxy else None,
        ))

    return WorkResponse(tasks=work_tasks, retry_after=0)
```

### 5.2 Results Submission

**File:** `gateway/routes/internal/results.py`

```python
from fastapi import APIRouter, Depends
from typing import List
from datetime import datetime
from ...services.properties import PropertyService
from ...models.parcel import ParcelResult, SubmitResponse
from ...auth.authenticator import User
from ...dependencies import get_current_worker

router = APIRouter(prefix="/internal", tags=["Internal API"])

@router.post("/results", response_model=SubmitResponse)
async def submit_results(
    results: List[ParcelResult],
    worker: User = Depends(get_current_worker),
    properties: PropertyService = Depends(),
):
    """
    Worker submits parsed parcel data.
    Gateway batch-inserts into PostgreSQL.
    """
    worker_id = worker.id.split(":")[1]

    inserted = 0
    updated = 0
    failed = 0
    errors = []

    for result in results:
        try:
            is_new = await properties.upsert_parcel(
                parcel_id=result.parcel_id,
                platform=result.platform,
                state=result.state,
                county=result.county,
                data=result.data,
                scraped_at=result.scraped_at,
                worker_id=worker_id,
            )
            if is_new:
                inserted += 1
            else:
                updated += 1
        except Exception as e:
            failed += 1
            errors.append(f"{result.parcel_id}: {str(e)}")

    return SubmitResponse(
        inserted=inserted,
        updated=updated,
        failed=failed,
        errors=errors[:10],  # Limit error messages
    )
```

### 5.3 Raw Files Upload

**File:** `gateway/routes/internal/raw_files.py`

```python
from fastapi import APIRouter, Depends, UploadFile, File, Form
from ...services.storage import StorageService
from ...auth.authenticator import User
from ...dependencies import get_current_worker
import json

router = APIRouter(prefix="/internal", tags=["Internal API"])

@router.post("/raw-files")
async def upload_raw_files(
    file: UploadFile = File(...),
    metadata: str = Form(...),
    worker: User = Depends(get_current_worker),
    storage: StorageService = Depends(),
):
    """
    Worker uploads raw HTML/PDF files.
    Gateway saves to /data/raw/ or S3.
    """
    meta = json.loads(metadata)
    content = await file.read()

    file_path = await storage.save_raw_file(
        content=content,
        platform=meta["platform"],
        state=meta["state"],
        county=meta["county"],
        parcel_id=meta["parcel_id"],
        content_type=meta.get("content_type", "text/html"),
        scraped_at=meta["scraped_at"],
    )

    return {"status": "ok", "path": file_path}
```

### 5.4 Task Status

**File:** `gateway/routes/internal/tasks.py`

```python
from fastapi import APIRouter, Depends, Path, HTTPException
from ...services.queue import QueueService
from ...services.proxy_pool import ProxyPoolService
from ...models.task import TaskMetrics, FailureInfo, RetryInfo
from ...auth.authenticator import User
from ...dependencies import get_current_worker

router = APIRouter(prefix="/internal", tags=["Internal API"])

@router.post("/tasks/{task_id}/complete")
async def complete_task(
    task_id: str = Path(...),
    metrics: TaskMetrics = None,
    worker: User = Depends(get_current_worker),
    queue: QueueService = Depends(),
):
    """Mark task as completed."""
    worker_id = worker.id.split(":")[1]
    await queue.complete_task(task_id, worker_id, metrics)
    return {"status": "ok"}

@router.post("/tasks/{task_id}/fail", response_model=RetryInfo)
async def fail_task(
    task_id: str = Path(...),
    error: FailureInfo = None,
    worker: User = Depends(get_current_worker),
    queue: QueueService = Depends(),
    proxy_pool: ProxyPoolService = Depends(),
):
    """
    Report task failure.
    Gateway decides: retry, requeue, or dead-letter.
    """
    worker_id = worker.id.split(":")[1]

    # Handle proxy ban
    if error and error.reason == "blocked" and error.proxy_port:
        await proxy_pool.ban(
            port=error.proxy_port,
            platform=error.platform,
            reason=error.message,
            duration_minutes=60,
        )

    # Determine retry strategy
    retry_info = await queue.handle_failure(
        task_id=task_id,
        worker_id=worker_id,
        error=error,
    )

    # Get new proxy if retrying
    if retry_info.should_retry and error:
        new_proxy = await proxy_pool.allocate(error.platform, worker_id)
        retry_info.new_proxy = new_proxy

    return retry_info
```

### 5.5 Proxy Management

**File:** `gateway/routes/internal/proxy.py`

```python
from fastapi import APIRouter, Depends, Path, Query, HTTPException
from ...services.proxy_pool import ProxyPoolService
from ...models.proxy import ProxyInfo
from ...auth.authenticator import User
from ...dependencies import get_current_worker

router = APIRouter(prefix="/internal/proxy", tags=["Internal API - Proxy"])

@router.get("/create", response_model=ProxyInfo)
async def create_proxy(
    platform: str = Query(...),
    worker: User = Depends(get_current_worker),
    proxy_pool: ProxyPoolService = Depends(),
):
    """Get a proxy for platform."""
    worker_id = worker.id.split(":")[1]
    proxy = await proxy_pool.allocate(platform, worker_id)

    if not proxy:
        raise HTTPException(503, "No proxies available for platform")

    return ProxyInfo(
        host=proxy.host,
        port=proxy.port,
        type="socks5",
        expires_at=proxy.expires_at,
    )

@router.post("/{port}/rotate", response_model=ProxyInfo)
async def rotate_proxy(
    port: int = Path(...),
    platform: str = Query(...),
    reason: str = Query(...),
    worker: User = Depends(get_current_worker),
    proxy_pool: ProxyPoolService = Depends(),
):
    """Replace banned/slow proxy."""
    worker_id = worker.id.split(":")[1]

    # Mark old proxy for cooldown
    await proxy_pool.cooldown(port, platform, reason)

    # Allocate new proxy
    new_proxy = await proxy_pool.allocate(platform, worker_id)

    if not new_proxy:
        raise HTTPException(503, "No replacement proxies available")

    return ProxyInfo(
        host=new_proxy.host,
        port=new_proxy.port,
        type="socks5",
        expires_at=new_proxy.expires_at,
    )

@router.post("/{port}/ban")
async def ban_proxy(
    port: int = Path(...),
    platform: str = Query(...),
    reason: str = Query(...),
    duration_minutes: int = Query(default=60),
    worker: User = Depends(get_current_worker),
    proxy_pool: ProxyPoolService = Depends(),
):
    """Explicitly ban proxy for platform."""
    await proxy_pool.ban(port, platform, reason, duration_minutes)
    return {"status": "banned"}
```

### 5.6 Worker Heartbeat

**File:** `gateway/routes/internal/heartbeat.py`

```python
from fastapi import APIRouter, Depends
from datetime import datetime
from ...services.worker_registry import WorkerRegistry
from ...models.worker import WorkerStatus, HeartbeatResponse
from ...auth.authenticator import User
from ...dependencies import get_current_worker

router = APIRouter(prefix="/internal", tags=["Internal API"])

@router.post("/heartbeat", response_model=HeartbeatResponse)
async def worker_heartbeat(
    status: WorkerStatus,
    worker: User = Depends(get_current_worker),
    registry: WorkerRegistry = Depends(),
):
    """
    Worker sends periodic heartbeat.
    Gateway tracks active workers for dashboard.
    """
    worker_id = worker.id.split(":")[1]

    # Update worker status
    await registry.update(
        worker_id=worker_id,
        status=status,
        last_seen=datetime.utcnow(),
    )

    # Check for pending commands
    commands = await registry.get_commands(worker_id)

    return HeartbeatResponse(
        acknowledged=True,
        commands=commands,
    )
```

---

## 6. Data Models

**File:** `gateway/models/task.py`

```python
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class FailureReason(str, Enum):
    PLATFORM_DOWN = "platform_down"
    FORMAT_CHANGED = "format_changed"
    RATE_LIMITED = "rate_limited"
    BLOCKED = "blocked"
    PARSER_BUG = "parser_bug"
    NETWORK_ERROR = "network_error"
    TIMEOUT = "timeout"

class ProxyInfo(BaseModel):
    host: str
    port: int
    type: str = "socks5"
    expires_at: Optional[datetime] = None

class WorkTask(BaseModel):
    task_id: str
    platform: str
    state: str
    county: str
    parcel_id: str
    priority: int
    url: Optional[str] = None
    proxy: Optional[ProxyInfo] = None

class WorkResponse(BaseModel):
    tasks: List[WorkTask]
    retry_after: int = 30

class TaskMetrics(BaseModel):
    duration_ms: int
    bytes_downloaded: int
    fields_parsed: int

class FailureInfo(BaseModel):
    reason: FailureReason
    message: str
    platform: Optional[str] = None
    proxy_port: Optional[int] = None
    retry_suggested: bool = True

class RetryInfo(BaseModel):
    should_retry: bool
    retry_after: Optional[int] = None
    new_proxy: Optional[ProxyInfo] = None
    moved_to_dlq: bool = False
```

**File:** `gateway/models/parcel.py`

```python
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class ParcelResult(BaseModel):
    task_id: str
    parcel_id: str
    platform: str
    state: str
    county: str
    data: Dict[str, Any]
    scraped_at: datetime
    parse_duration_ms: int
    raw_html_hash: Optional[str] = None

class SubmitResponse(BaseModel):
    inserted: int
    updated: int
    failed: int
    errors: List[str]
```

**File:** `gateway/models/worker.py`

```python
from pydantic import BaseModel
from typing import List

class WorkerStatus(BaseModel):
    active_tasks: int
    completed_last_minute: int
    failed_last_minute: int
    platforms: List[str]
    cpu_percent: float
    memory_percent: float

class HeartbeatResponse(BaseModel):
    acknowledged: bool
    commands: List[str] = []  # "shutdown", "pause", "config_update"
```

---

## 7. Services

### 7.1 Queue Service

**File:** `gateway/services/queue.py`

```python
from typing import List, Optional
from datetime import datetime
import json

class QueueService:
    """Redis-based task queue with priorities."""

    PRIORITY_QUEUES = {
        1: "queue:urgent",
        2: "queue:high",
        3: "queue:normal",
        4: "queue:low",
    }

    def __init__(self, redis):
        self.redis = redis

    async def enqueue(self, task: dict, priority: int = 3):
        """Add task to priority queue."""
        queue_key = self.PRIORITY_QUEUES[priority]
        task_json = json.dumps(task)
        await self.redis.zadd(queue_key, {task_json: datetime.utcnow().timestamp()})

    async def fetch_tasks(
        self,
        platforms: List[str],
        limit: int,
        worker_id: str,
    ) -> List[dict]:
        """Fetch tasks for worker (PULL model)."""
        tasks = []

        # Check queues in priority order
        for priority in sorted(self.PRIORITY_QUEUES.keys()):
            if len(tasks) >= limit:
                break

            queue_key = self.PRIORITY_QUEUES[priority]

            # Pop tasks atomically
            remaining = limit - len(tasks)
            raw_tasks = await self.redis.zpopmin(queue_key, remaining)

            for task_json, score in raw_tasks:
                task = json.loads(task_json)

                # Filter by platform
                if platforms and task.get("platform") not in platforms:
                    # Re-queue if worker doesn't support platform
                    await self.redis.zadd(queue_key, {task_json: score})
                    continue

                # Mark as processing
                await self._mark_processing(task["id"], worker_id)
                tasks.append(task)

        return tasks

    async def complete_task(self, task_id: str, worker_id: str, metrics: dict = None):
        """Mark task completed."""
        await self.redis.delete(f"processing:{task_id}")
        if metrics:
            await self._record_metrics(task_id, metrics)

    async def handle_failure(self, task_id: str, worker_id: str, error: dict) -> dict:
        """Handle task failure - retry or DLQ."""
        task_data = await self.redis.get(f"processing:{task_id}")
        if not task_data:
            return {"should_retry": False, "moved_to_dlq": True}

        task = json.loads(task_data)
        retry_count = task.get("retry_count", 0)

        # Max 3 retries
        if retry_count >= 3 or (error and not error.get("retry_suggested", True)):
            # Move to Dead Letter Queue
            await self.redis.lpush("dlq", json.dumps({
                "task": task,
                "error": error,
                "failed_at": datetime.utcnow().isoformat(),
            }))
            await self.redis.delete(f"processing:{task_id}")
            return {"should_retry": False, "moved_to_dlq": True}

        # Requeue with incremented retry count
        task["retry_count"] = retry_count + 1
        await self.enqueue(task, priority=task.get("priority", 3))
        await self.redis.delete(f"processing:{task_id}")

        # Exponential backoff
        retry_after = 30 * (2 ** retry_count)
        return {"should_retry": True, "retry_after": retry_after}

    async def _mark_processing(self, task_id: str, worker_id: str):
        """Track task being processed."""
        await self.redis.setex(
            f"processing:{task_id}",
            300,  # 5 minute timeout
            json.dumps({
                "worker_id": worker_id,
                "started_at": datetime.utcnow().isoformat(),
            })
        )

    async def _record_metrics(self, task_id: str, metrics: dict):
        """Record task completion metrics."""
        pass  # Prometheus metrics updated here
```

### 7.2 Proxy Pool Service

**File:** `gateway/services/proxy_pool.py`

```python
from typing import Optional, Dict
from datetime import datetime, timedelta
import aiohttp

class ProxyPoolService:
    """Manage tor-socks-proxy pool via its REST API."""

    def __init__(self, settings, redis):
        self.tor_api_url = settings.tor_proxy_url
        self.redis = redis

    async def get_available_count(self, platform: str) -> int:
        """Count available (non-banned) proxies for platform."""
        key = f"proxy:available:{platform}"
        count = await self.redis.scard(key)
        return count

    async def allocate(self, platform: str, worker_id: str) -> Optional[dict]:
        """Allocate a proxy for platform."""
        # Check if worker already has proxy for this platform
        existing = await self.redis.hget(f"worker:{worker_id}:proxies", platform)
        if existing:
            return self._parse_proxy(existing)

        # Request new proxy from tor-socks-proxy API
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.tor_api_url}/proxies", json={
                "geo": "US",
                "platform": platform,
            }) as resp:
                if resp.status != 200:
                    return None
                data = await resp.json()

        proxy = {
            "host": data["host"],
            "port": data["port"],
            "expires_at": datetime.utcnow() + timedelta(hours=1),
        }

        # Track allocation
        await self.redis.hset(
            f"worker:{worker_id}:proxies",
            platform,
            self._serialize_proxy(proxy)
        )
        await self.redis.sadd(f"proxy:available:{platform}", data["port"])

        return proxy

    async def ban(self, port: int, platform: str, reason: str, duration_minutes: int):
        """Ban proxy for platform."""
        await self.redis.srem(f"proxy:available:{platform}", port)
        await self.redis.setex(
            f"proxy:banned:{platform}:{port}",
            duration_minutes * 60,
            reason
        )

        # Notify tor-socks-proxy
        async with aiohttp.ClientSession() as session:
            await session.post(f"{self.tor_api_url}/proxies/{port}/rotate")

    async def cooldown(self, port: int, platform: str, reason: str):
        """Put proxy in cooldown (temporary ban)."""
        await self.redis.srem(f"proxy:available:{platform}", port)
        await self.redis.setex(
            f"proxy:cooldown:{platform}:{port}",
            300,  # 5 minute cooldown
            reason
        )

    def _parse_proxy(self, data: str) -> dict:
        import json
        return json.loads(data)

    def _serialize_proxy(self, proxy: dict) -> str:
        import json
        return json.dumps(proxy, default=str)
```

### 7.3 Worker Registry

**File:** `gateway/services/worker_registry.py`

```python
from typing import List, Optional
from datetime import datetime
import json

class WorkerRegistry:
    """Track active workers and their status."""

    def __init__(self, redis, settings):
        self.redis = redis
        self.heartbeat_timeout = settings.worker_heartbeat_timeout

    async def update(self, worker_id: str, status: dict, last_seen: datetime):
        """Update worker status."""
        await self.redis.hset("workers", worker_id, json.dumps({
            **status.dict() if hasattr(status, 'dict') else status,
            "last_seen": last_seen.isoformat(),
        }))
        await self.redis.setex(f"worker:alive:{worker_id}", self.heartbeat_timeout, "1")

    async def get_commands(self, worker_id: str) -> List[str]:
        """Get pending commands for worker."""
        commands = await self.redis.lrange(f"worker:commands:{worker_id}", 0, -1)
        await self.redis.delete(f"worker:commands:{worker_id}")
        return [c.decode() if isinstance(c, bytes) else c for c in commands]

    async def send_command(self, worker_id: str, command: str):
        """Queue command for worker."""
        await self.redis.rpush(f"worker:commands:{worker_id}", command)

    async def get_active_workers(self) -> List[dict]:
        """Get all active workers."""
        workers = await self.redis.hgetall("workers")
        active = []

        for worker_id, data in workers.items():
            worker_id_str = worker_id.decode() if isinstance(worker_id, bytes) else worker_id
            if await self.redis.exists(f"worker:alive:{worker_id_str}"):
                active.append({
                    "id": worker_id_str,
                    **json.loads(data),
                })

        return active

    async def cleanup_dead_workers(self):
        """Find and handle dead workers."""
        workers = await self.redis.hgetall("workers")

        for worker_id, data in workers.items():
            worker_id_str = worker_id.decode() if isinstance(worker_id, bytes) else worker_id
            if not await self.redis.exists(f"worker:alive:{worker_id_str}"):
                # Worker is dead - requeue its tasks
                await self._requeue_worker_tasks(worker_id_str)
                await self.redis.hdel("workers", worker_id)

    async def _requeue_worker_tasks(self, worker_id: str):
        """Requeue tasks from dead worker."""
        keys = await self.redis.keys(f"processing:*")
        for key in keys:
            data = await self.redis.get(key)
            if data:
                task_info = json.loads(data)
                if task_info.get("worker_id") == worker_id:
                    # Requeue logic handled by queue service
                    await self.redis.delete(key)
```

---

## 8. Redis Schema

```
# Rate Limiting
ratelimit:{user_id}
  - tokens: float
  - updated: timestamp

# Usage Tracking
usage:{user_id}:{action}:{date} = count (TTL: 24h)

# Task Queues
queue:urgent   - sorted set (score = timestamp)
queue:high     - sorted set
queue:normal   - sorted set
queue:low      - sorted set
dlq            - list of failed tasks

# Task Processing
processing:{task_id} = {worker_id, started_at} (TTL: 5min)

# Workers
workers = hash {worker_id -> status JSON}
worker:alive:{worker_id} = "1" (TTL: heartbeat_timeout)
worker:commands:{worker_id} = list of commands
worker:{worker_id}:proxies = hash {platform -> proxy JSON}

# Proxy Pool
proxy:available:{platform} = set of ports
proxy:banned:{platform}:{port} = reason (TTL: ban duration)
proxy:cooldown:{platform}:{port} = reason (TTL: 5min)

# Cache
cache:prop:{parcel_id} = JSON (TTL: 1h)
cache:search:{hash} = JSON (TTL: 15min)
cache:pred:{parcel_id} = JSON (TTL: 24h)
cache:toplist:{strategy} = JSON (TTL: 1h)
```

---

## 9. Prometheus Metrics

**File:** `gateway/metrics.py`

```python
from prometheus_client import Counter, Histogram, Gauge

# Request metrics
REQUESTS_TOTAL = Counter(
    "gateway_requests_total",
    "Total HTTP requests",
    ["method", "path", "status", "tier"]
)

REQUEST_DURATION = Histogram(
    "gateway_request_duration_seconds",
    "Request duration",
    ["method", "path", "service"],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
)

# Cache metrics
CACHE_HITS = Counter("gateway_cache_hits_total", "Cache hits", ["endpoint"])
CACHE_MISSES = Counter("gateway_cache_misses_total", "Cache misses", ["endpoint"])

# Rate limiting
RATE_LIMIT_HITS = Counter("gateway_rate_limit_hits_total", "Rate limit exceeded", ["tier"])

# Worker metrics
WORKERS_ACTIVE = Gauge("gateway_workers_active", "Active workers", ["platform"])
WORKERS_TASKS_TOTAL = Counter("gateway_worker_tasks_total", "Tasks processed", ["platform", "status"])

# Queue metrics
QUEUE_DEPTH = Gauge("gateway_queue_depth", "Queue depth", ["priority"])

# Proxy metrics
PROXY_AVAILABLE = Gauge("gateway_proxy_available", "Available proxies", ["platform"])
PROXY_BANNED = Gauge("gateway_proxy_banned", "Banned proxies", ["platform"])
```

---

## 10. Error Response Format

```python
from pydantic import BaseModel
from typing import Optional, Dict, Any

class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None

class ErrorResponse(BaseModel):
    error: ErrorDetail
    request_id: str
    documentation_url: Optional[str] = None

ERROR_CODES = {
    400: "INVALID_REQUEST",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    422: "VALIDATION_ERROR",
    429: "RATE_LIMIT_EXCEEDED",
    500: "INTERNAL_ERROR",
    502: "SERVICE_UNAVAILABLE",
    503: "MAINTENANCE",
}
```

---

## 11. Docker Configuration (Dual-Port)

**File:** `gateway/Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose BOTH ports
EXPOSE 8080 8081

# Healthcheck for both apps
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health && curl -f http://localhost:8081/health || exit 1

# Run main.py which starts both servers
CMD ["python", "main.py"]
```

**File:** `docker-compose.yml`

```yaml
version: '3.8'

services:
  gateway:
    build: ./gateway
    ports:
      - "8080:8080"    # Public API (exposed via nginx/cloudflare)
      - "8081:8081"    # Internal API (VPN/private network only)
    environment:
      - GATEWAY_POSTGRES_URL=postgresql://user:pass@postgres:5432/taxlien
      - GATEWAY_REDIS_URL=redis://redis:6379
      - GATEWAY_FIREBASE_PROJECT_ID=taxlien-online
      - GATEWAY_SSR_SERVICE_TOKEN=${SSR_TOKEN}
      - GATEWAY_WORKER_TOKENS=${WORKER_TOKENS}
      - GATEWAY_RAW_STORAGE_PATH=/data/raw
      - GATEWAY_PUBLIC_PORT=8080
      - GATEWAY_INTERNAL_PORT=8081
      - GATEWAY_INTERNAL_IP_WHITELIST=${INTERNAL_IP_WHITELIST:-}
    volumes:
      - raw_storage:/data/raw
    depends_on:
      - postgres
      - redis
    networks:
      - public
      - internal

  postgres:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=taxlien
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - internal

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    networks:
      - internal

  # Parser workers only have access to internal network
  parser-worker:
    build: ./parser-worker
    environment:
      - GATEWAY_INTERNAL_URL=http://gateway:8081
      - WORKER_TOKEN=${WORKER_TOKEN_1}
      - TOR_PROXY_HOST=tor-proxy
      - TOR_PROXY_PORT=9050
    networks:
      - internal
    deploy:
      replicas: 4
    depends_on:
      - gateway
      - tor-proxy

  tor-proxy:
    build: ./tor-socks-proxy
    networks:
      - internal

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
    networks:
      - internal

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
    ports:
      - "3000:3000"
    networks:
      - internal

networks:
  public:
    driver: bridge
  internal:
    driver: bridge
    internal: true  # No external access - workers can't reach internet directly

volumes:
  postgres_data:
  redis_data:
  raw_storage:
  prometheus_data:
  grafana_data:
```

**File:** `prometheus.yml` - Scrape both apps

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'gateway-public'
    static_configs:
      - targets: ['gateway:8080']
    metrics_path: /metrics

  - job_name: 'gateway-internal'
    static_configs:
      - targets: ['gateway:8081']
    metrics_path: /metrics
```

---

## 12. Testing Specifications

### Unit Tests

```python
# tests/test_auth.py
import pytest
from gateway.auth.authenticator import Authenticator

async def test_firebase_token_valid(authenticator, mock_firebase):
    mock_firebase.verify_id_token.return_value = {
        "uid": "user123",
        "tier": "premium",
        "email": "test@example.com"
    }

    request = MockRequest(headers={"Authorization": "Bearer valid_token"})
    result = await authenticator.authenticate(request)

    assert result.authenticated is True
    assert result.user.id == "user123"
    assert result.user.tier == "premium"

async def test_worker_token_valid(authenticator):
    request = MockRequest(headers={
        "X-Worker-Token": "valid-worker-token",
        "X-Worker-ID": "worker-1"
    })
    result = await authenticator.authenticate(request)

    assert result.authenticated is True
    assert result.user.auth_method.value == "worker"
```

### Integration Tests

```python
# tests/test_internal_api.py
import pytest
from httpx import AsyncClient

async def test_get_work_returns_tasks(client, worker_headers, populated_queue):
    response = await client.get(
        "/internal/work",
        params={"platforms": ["beacon"], "capacity": 5},
        headers=worker_headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data["tasks"]) <= 5

async def test_submit_results_inserts_data(client, worker_headers, db):
    results = [{
        "task_id": "task-1",
        "parcel_id": "12-34-56",
        "platform": "beacon",
        "state": "FL",
        "county": "Orange",
        "data": {"owner": "John Doe", "value": 100000},
        "scraped_at": "2026-01-18T12:00:00Z",
        "parse_duration_ms": 150,
    }]

    response = await client.post(
        "/internal/results",
        json=results,
        headers=worker_headers,
    )

    assert response.status_code == 200
    assert response.json()["inserted"] == 1
```

---

## 13. CI/CD Pipeline

### 13.1 Workflow Triggers
- **Pull Request:** Trigger on open/synchronize to `main` branch.
- **Push:** Trigger on push to `main` branch.
- **Release:** Trigger on tag creation `v*`.

### 13.2 Build & Test Job
- **Environment:** Ubuntu-latest
- **Steps:**
    1. Checkout code.
    2. Set up Python 3.11.
    3. Install dependencies (`poetry install`).
    4. Run linting (`ruff check .`).
    5. Run type checking (`mypy .`).
    6. Run tests (`pytest`).
    7. Build Docker image (dry run).

### 13.3 Publish Job (Main/Tag only)
- **Environment:** Ubuntu-latest
- **Steps:**
    1. Login to GitHub Container Registry (GHCR).
    2. Build and push Docker image.
    3. Image tagging strategy:
        - `main`: `ghcr.io/taxlien-online/gateway:latest`, `ghcr.io/taxlien-online/gateway:sha-{commit_hash}`
        - `tag`: `ghcr.io/taxlien-online/gateway:{tag}`

### 13.4 Secrets
- `GITHUB_TOKEN`: For GHCR authentication (automatic).

---

## 14. Monitoring Dashboards (Grafana)

### 14.1 Dashboard: Gateway Command Center

**Panels & Queries:**

1.  **System Health Row:**
    *   **Success Rate:** `sum(rate(gateway_requests_total{status=~"2.."}[5m])) / sum(rate(gateway_requests_total[5m]))`
    *   **P95 Latency:** `histogram_quantile(0.95, sum(rate(gateway_request_duration_seconds_bucket[5m])) by (le))`
    *   **RPS:** `sum(rate(gateway_requests_total[1m]))`

2.  **Worker Fleet Row:**
    *   **Active Workers:** `sum(gateway_workers_active) by (platform)`
    *   **Task Success/Fail:** `sum(rate(gateway_worker_tasks_total[5m])) by (status)`
    *   **Queue Depth:** `gateway_queue_depth` (by priority)

3.  **Proxy & Cache Row:**
    *   **Proxy Health:** `gateway_proxy_available` vs `gateway_proxy_banned`
    *   **Cache Hit Rate:** `sum(rate(gateway_cache_hits_total[5m])) / (sum(rate(gateway_cache_hits_total[5m])) + sum(rate(gateway_cache_misses_total[5m])))`

4.  **Business Row:**
    *   **Traffic by Tier:** `sum(gateway_requests_total) by (tier)`
    *   **Rate Limit Hits:** `increase(gateway_rate_limit_hits_total[1m])`

---

**Next Phase:** PLAN
