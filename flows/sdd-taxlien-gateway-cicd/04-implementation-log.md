# Implementation Log: taxlien-gateway CI/CD

> Started: 2026-02-12
> Plan: ./03-plan.md
> Status: Implementation complete

## Progress Tracker

| Task | Status | Notes |
|------|--------|-------|
| 1.1 BIND_IP и порты | Done | All services use BIND_IP and *_PORT |
| 1.2 ENV_TAG образов | Done | taxlien-gateway:${ENV_TAG:-latest} |
| 1.3 External volumes (DATA_DIR) | Done | ${DATA_DIR:-./data}/postgres|redis|raw|grafana |
| 1.4 COMPOSE_PROJECT_NAME | Done | Documented in .env.example |
| 2.1 .env.example | Done | Created with examples |
| 2.2 .gitignore | Done | .env already present |
| 3.1–3.4 deploy.yml | Done | Triggers, validation, copy, build, up, health check |
| 4.1 README | Done | CI/CD section added |
| 4.2 Локальная проверка | Pending | `docker compose config` with .env recommended |

## Session Log

### Session 2026-02-12

**Context:** Plan approved; implementation from scratch for taxlien-gateway.

**Done:**
- **Phase 1:** docker-compose.yml parameterized: BIND_IP, GATEWAY_PORT, DB_PORT, REDIS_PORT, PROMETHEUS_PORT, GRAFANA_PORT; ENV_TAG for gateway-go image; DATA_DIR for postgres, redis, raw, grafana (external volumes). Legacy gateway left with named volume for local dev.
- **Phase 2:** .env.example created; .gitignore already contained .env.
- **Phase 3:** .github/workflows/deploy.yml — push to prod/dev/stage and workflow_dispatch; DEPLOY_DIR and .env validation; copy compose, Dockerfile.gateway, go.mod, go.sum, cmd, internal, pkg, migrations, monitoring; docker compose build / down / up --profile go; health check (warning only).
- **Phase 4:** README extended with CI/CD: prerequisites, directory layout, initial setup, triggers, macOS note.

**Deviations:** None.

**Handoff:** Ready for first deploy after setting up DEPLOY_DIR, .env, and data dirs on runners.

## Deviations Summary

| Planned | Actual | Reason |
|---------|--------|--------|
| — | — | — |

## Learnings

- Deploy uses `--profile go` so only gateway-go (Go Worker API) is started; db, redis, prometheus, grafana have no profile and start by default.
- DATA_DIR defaults to ./data so local runs work without .env.
