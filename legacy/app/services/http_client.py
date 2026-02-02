import httpx
import time
import asyncio
import structlog
from typing import Dict, Any, Optional
from enum import Enum

logger = structlog.get_logger()

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, name: str, threshold: int = 5, recovery_timeout: int = 30):
        self.name = name
        self.threshold = threshold
        self.recovery_timeout = recovery_timeout
        self.state = CircuitState.CLOSED
        self.failures = 0
        self.last_failure_time = 0

    def record_success(self):
        self.failures = 0
        self.state = CircuitState.CLOSED

    def record_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
        if self.failures >= self.threshold:
            self.state = CircuitState.OPEN
            logger.error("circuit_breaker_opened", service=self.name, failures=self.failures)

    def can_execute(self) -> bool:
        if self.state == CircuitState.CLOSED:
            return True
        
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = CircuitState.HALF_OPEN
                logger.info("circuit_breaker_half_open", service=self.name)
                return True
            return False
        
        return True # HALF_OPEN

class ServiceClient:
    _breakers: Dict[str, CircuitBreaker] = {}

    def __init__(self, base_url: str, service_name: str):
        self.base_url = base_url
        self.service_name = service_name
        if service_name not in self._breakers:
            self._breakers[service_name] = CircuitBreaker(service_name)
        self.breaker = self._breakers[service_name]

    async def request(
        self, 
        method: str, 
        path: str, 
        params: Optional[Dict] = None, 
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: float = 30.0
    ):
        if not self.breaker.can_execute():
            logger.warning("circuit_breaker_blocked_request", service=self.service_name)
            raise httpx.HTTPStatusError("Circuit breaker is OPEN", request=None, response=None)

        async with httpx.AsyncClient(base_url=self.base_url) as client:
            try:
                response = await client.request(
                    method=method,
                    url=path,
                    params=params,
                    json=json,
                    headers=headers,
                    timeout=timeout
                )
                
                if response.status_code >= 500:
                    self.breaker.record_failure()
                else:
                    self.breaker.record_success()
                    
                return response
            except (httpx.RequestError, asyncio.TimeoutError):
                self.breaker.record_failure()
                raise
