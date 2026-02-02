# TAXLIEN.online API Gateway

Unified entry point for all TAXLIEN.online services.

## Features

- **External API (v1)**: Access for Flutter App, SSR Site, and B2B clients.
- **Internal API**: Communication with distributed Parser Workers.
- **Authentication**: Firebase JWT and API Key support.
- **Rate Limiting**: Tier-based limits via Redis.
- **Caching**: Performance optimization for property data and search results.

## Quick Start

### Using Docker Compose

```bash
docker-compose up --build
```

The gateway will be available at `http://localhost:8000`.
Documentation is at `http://localhost:8000/docs`.

### Local Development

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

- `/v1/*`: Public API endpoints.
- `/internal/*`: Internal endpoints for workers (requires `X-Worker-Token`).
- `/health`: Service health check.
