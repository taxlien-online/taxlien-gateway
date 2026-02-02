from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from fastapi import Request
import time

# Metrics
REQUEST_COUNT = Counter(
    "gateway_requests_total",
    "Total number of requests",
    ["method", "endpoint", "status", "tier"]
)

REQUEST_LATENCY = Histogram(
    "gateway_request_latency_seconds",
    "Latency of requests in seconds",
    ["method", "endpoint"]
)

class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        path = request.url.path
        
        # Determine tier from auth if available
        tier = "anonymous"
        if hasattr(request.state, "auth"):
            t = request.state.auth.tier
            tier = t.value if hasattr(t, "value") else str(t)
            
        start_time = time.time()
        
        response = await call_next(request)
        
        duration = time.time() - start_time
        status = response.status_code
        
        # Update metrics
        REQUEST_COUNT.labels(method=method, endpoint=path, status=status, tier=tier).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=path).observe(duration)
        
        return response

def metrics_response():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
