from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

class UserTier(str, Enum):
    ANONYMOUS = "anonymous"
    FREE = "free"
    STARTER = "starter"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"
    INTERNAL = "internal"

class AuthContext(BaseModel):
    user_id: Optional[str] = None
    tier: UserTier = UserTier.ANONYMOUS
    scopes: List[str] = []
    worker_id: Optional[str] = None
