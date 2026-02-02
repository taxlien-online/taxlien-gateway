from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime

class ProxyInfo(BaseModel):
    host: str
    port: int
    type: str = "socks5"
    username: Optional[str] = None
    password: Optional[str] = None
    expires_at: Optional[datetime] = None

class WorkTask(BaseModel):
    task_id: str
    type: str = "scrape"
    platform: str
    target: Dict[str, Any]
    priority: int = 3  # 1=urgent, 2=high, 3=normal, 4=low
    proxy: Optional[ProxyInfo] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class WorkResponse(BaseModel):
    tasks: List[WorkTask]
    retry_after: int = 30

class ParcelResult(BaseModel):
    task_id: str
    parcel_id: str
    platform: str
    state: str
    county: str
    data: Dict[str, Any]
    scraped_at: datetime = Field(default_factory=datetime.utcnow)
    parse_duration_ms: int
    raw_html_hash: Optional[str] = None

class SubmitResponse(BaseModel):
    inserted: int
    updated: int
    failed: int
    errors: List[str] = []

class WorkerStatus(BaseModel):
    active_tasks: int
    completed_last_minute: int
    failed_last_minute: int
    platforms: List[str]
    cpu_percent: float
    memory_percent: float
