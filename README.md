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

## CI/CD (Deploy to prod / dev / stage)

Deploy is done via GitHub Actions and self-hosted runners. Each environment (prod, dev, stage) has its own runner label and directory; data (PostgreSQL, Redis, raw files, Grafana) is stored in **external volumes** on the host.

### Prerequisites on the server

- Docker and Docker Compose v2
- GitHub Actions runner registered with labels: `self-hosted` and one of `prod`, `dev`, `stage`
- Environment variable **DEPLOY_DIR** set (e.g. `/opt/taxlien-gateway` on Linux or `~/taxlien-gateway` on macOS)

### Directory layout (e.g. Linux)

```text
/opt/taxlien-gateway/
├── prod/
│   ├── .env          # from .env.example; set BIND_IP, DATA_DIR, secrets
│   ├── data/         # created once; subdirs: postgres, redis, raw, grafana
│   └── ...          # docker-compose.yml etc. copied on deploy
├── dev/
└── stage/
```

### Initial setup per environment

1. Create directory: `mkdir -p $DEPLOY_DIR/{prod,dev,stage}/data/{postgres,redis,raw,grafana}`
2. Copy `.env.example` to `$DEPLOY_DIR/<env>/.env` and set:
   - **COMPOSE_PROJECT_NAME** (e.g. `taxlien-gateway-prod`)
   - **ENV_TAG** (e.g. `prod`)
   - **BIND_IP** — dedicated IP for this stack (avoids port conflicts with other projects)
   - **DATA_DIR** — path to this env’s data dir (e.g. `/opt/taxlien-gateway/prod/data`)
   - **GATEWAY_WORKER_TOKENS**, **GRAFANA_PASSWORD**
3. First deploy will copy repo files and run `docker compose build && docker compose --profile go up -d`.

### Triggers

- **Push** to branch `prod`, `dev`, or `stage` → deploy runs on the runner with the matching label.
- **Manual**: Actions → Deploy → Run workflow → choose environment.

### macOS (e.g. stage)

Same steps; use `DEPLOY_DIR=~/taxlien-gateway` and in `.env` set `BIND_IP=127.0.0.1` and `DATA_DIR=./data` (relative to the env directory).
