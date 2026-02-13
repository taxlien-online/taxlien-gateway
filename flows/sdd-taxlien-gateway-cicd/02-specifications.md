# Specifications: taxlien-gateway CI/CD

> Version: 1.0
> Status: DRAFTED
> Last Updated: 2026-02-12
> Requirements: ./01-requirements.md

## Overview

CI/CD для автоматического деплоя **taxlien-gateway** на инстансы prod/dev/stage через GitHub Actions с self-hosted runners.

**Ключевые особенности:**
- Мульти-платформенность: **Linux (Unix)** и **macOS** (stage может быть на macOS).
- Отдельный **IP/интерфейс** для привязки сервисов — без накладок с другими Docker-проектами.
- **Внешние тома (external volume)** для БД и raw-данных — данные на хосте.

## Multi-Platform Support

### Platform Matrix

| Platform   | Docker         | DEPLOY_DIR / data paths     | Примечание        |
|-----------|----------------|-----------------------------|-------------------|
| Linux     | Docker Engine  | `/opt/taxlien-gateway/`     | Полный стек       |
| macOS     | Docker Desktop | `~/taxlien-gateway/`        | В т.ч. stage      |

### Configuration per Platform

**Linux Runner:**
```bash
export DEPLOY_DIR=/opt/taxlien-gateway
```

**macOS Runner:**
```bash
export DEPLOY_DIR=~/taxlien-gateway
```

### Workflow: определение OS

```bash
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  PROFILE_FLAG="--profile linux"   # если появятся linux-only сервисы
  DATA_BASE="${DEPLOY_DIR}"
else
  PROFILE_FLAG=""
  DATA_BASE="${DEPLOY_DIR}"
fi
```

Пути к данным задаются через `.env` (DATA_DIR), так что один и тот же compose подходит и для Linux, и для macOS.

## Affected Systems

| System                      | Impact  | Notes                                              |
|----------------------------|---------|----------------------------------------------------|
| `.github/workflows/`       | Create  | deploy.yml (деплой по веткам + workflow_dispatch)  |
| `docker-compose.yml`       | Modify  | BIND_IP, порты, теги, external volumes для data   |
| `.env.example`             | Create  | Шаблон переменных (BIND_IP, DATA_DIR, порты)      |
| Dockerfile.gateway         | As-is   | Используется при сборке образа gateway             |

## Architecture

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                   GitHub Repository (taxlien-gateway)             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │
│  │ branch:prod │  │ branch:dev  │  │ branch:stage│                │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘                │
│         └────────────────┼────────────────┘                      │
│                          ▼                                        │
│              ┌───────────────────────┐                           │
│              │  .github/workflows/   │                           │
│              │     deploy.yml        │                           │
│              └───────────┬───────────┘                           │
└──────────────────────────┼───────────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  Server: Prod    │ │  Server: Dev    │ │  Server: Stage  │
│  (Linux, BIND_IP)│ │  (Linux)        │ │  (macOS / Linux)│
│  DEPLOY_DIR/    │ │  DEPLOY_DIR/    │ │  DEPLOY_DIR/    │
│    prod/        │ │    dev/         │ │    stage/       │
│    data/        │ │    data/        │ │    data/        │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

### Отдельный IP для Docker (изоляция)

На сервере с несколькими проектами:
- Каждому окружению taxlien-gateway задаётся свой **BIND_IP** (интерфейс или alias).
- Все порты биндятся на этот IP: `${BIND_IP}:${GATEWAY_PORT}:8081` и т.д.
- Конфликтов с другими стеками по портам не возникает.

### External volumes для БД и raw

Используются host-пути, заданные в `.env`:

```yaml
# Концепт docker-compose
volumes:
  - ${DATA_DIR}/postgres:/var/lib/postgresql/data
  - ${DATA_DIR}/redis:/data
  - ${DATA_DIR}/raw:/data/raw
  - ${DATA_DIR}/grafana:/var/lib/grafana
```

Переменная **DATA_DIR** в `.env`: например `/opt/taxlien-gateway/prod/data` (Linux) или `~/taxlien-gateway/stage/data` (macOS). Данные переживают `docker-compose down/up` и доступны для бэкапов на хосте.

### Deploy Flow

```
Push to branch (prod/dev/stage)
         │
         ▼
GitHub Actions → runner by label (self-hosted, prod|dev|stage)
         │
         ▼
Checkout → Copy compose/Dockerfile/source to DEPLOY_DIR/{env}/
         │ (preserve .env, docker-compose.override.yml, data/)
         ▼
docker-compose build (ENV_TAG from .env)
         │
         ▼
docker-compose down && docker-compose up -d [--profile linux]
         │
         ▼
Health check (optional, warning only)
```

## Interfaces

### GitHub Actions Workflow (концепт)

```yaml
name: Deploy

on:
  push:
    branches: [prod, dev, stage]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment'
        required: true
        type: choice
        options: [prod, dev, stage]

jobs:
  deploy:
    runs-on: [self-hosted, "${{ github.ref_name }}"]

    steps:
      - uses: actions/checkout@v4

      - name: Validate environment
        run: |
          if [ -z "${DEPLOY_DIR}" ]; then
            echo "::error::DEPLOY_DIR not set"
            exit 1
          fi
          ENV_NAME="${{ github.ref_name }}"
          TARGET_DIR="${DEPLOY_DIR}/${ENV_NAME}"
          if [ ! -f "${TARGET_DIR}/.env" ]; then
            echo "::error::.env not found in ${TARGET_DIR}"
            exit 1
          fi

      - name: Deploy
        run: |
          ENV_NAME="${{ github.ref_name }}"
          TARGET_DIR="${DEPLOY_DIR}/${ENV_NAME}"
          cp docker-compose.yml "${TARGET_DIR}/"
          cp Dockerfile.gateway "${TARGET_DIR}/"
          cp go.mod go.sum "${TARGET_DIR}/"
          cp -r cmd internal pkg migrations "${TARGET_DIR}/"   # для сборки gateway
          cp -r monitoring "${TARGET_DIR}/"
          [ -f .env.example ] && cp .env.example "${TARGET_DIR}/"

          cd "${TARGET_DIR}"
          if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            PROFILE_FLAG="--profile linux"
          else
            PROFILE_FLAG=""
          fi

          docker-compose build
          docker-compose down
          docker-compose ${PROFILE_FLAG} up -d

      - name: Health check
        run: |
          sleep 10
          cd "${DEPLOY_DIR}/${{ github.ref_name }}"
          docker-compose ps
          # optional: curl http://${BIND_IP}:8081/health
```

### Parameterized docker-compose.yml (концепт)

- **COMPOSE_PROJECT_NAME** — из .env (например taxlien-gateway-prod).
- **ENV_TAG** — тег образов (:prod, :dev, :stage).
- **BIND_IP** — IP для привязки портов (обязательно на сервере).
- **DATA_DIR** — базовый каталог для external volumes (postgres, redis, raw, grafana).
- **Порты** — GATEWAY_PORT, DB_PORT, REDIS_PORT, PROMETHEUS_PORT, GRAFANA_PORT с дефолтами.

Пример фрагмента:

```yaml
services:
  gateway-go:
    build:
      context: .
      dockerfile: Dockerfile.gateway
    image: taxlien-gateway:${ENV_TAG:-latest}
    ports:
      - "${BIND_IP:-0.0.0.0}:${GATEWAY_PORT:-8081}:8081"
    environment:
      - GATEWAY_PORT=8081
      - GATEWAY_POSTGRES_URL=postgres://user:pass@db:5432/taxlien
      - GATEWAY_REDIS_URL=redis://redis:6379/0
      - GATEWAY_RAW_STORAGE_PATH=/data/raw
      - GATEWAY_WORKER_TOKENS=${GATEWAY_WORKER_TOKENS:-}
    volumes:
      - ${DATA_DIR}/raw:/data/raw
    depends_on:
      - redis
      - db
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: taxlien
    ports:
      - "${BIND_IP:-0.0.0.0}:${DB_PORT:-5432}:5432"
    volumes:
      - ${DATA_DIR}/postgres:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "${BIND_IP:-0.0.0.0}:${REDIS_PORT:-6379}:6379"
    volumes:
      - ${DATA_DIR}/redis:/data
    restart: unless-stopped

  prometheus:
    image: prom/prometheus:v2.45.0
    ports:
      - "${BIND_IP:-0.0.0.0}:${PROMETHEUS_PORT:-9090}:9090"
    volumes:
      - ./monitoring/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    restart: unless-stopped

  grafana:
    image: grafana/grafana:10.0.0
    ports:
      - "${BIND_IP:-0.0.0.0}:${GRAFANA_PORT:-3000}:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: ${GRAFANA_PASSWORD:-admin}
    volumes:
      - ${DATA_DIR}/grafana:/var/lib/grafana
      - ./monitoring/grafana/provisioning:/etc/grafana/provisioning
      - ./monitoring/grafana/dashboards:/var/lib/grafana/dashboards
    restart: unless-stopped
```

## Data Models

### .env.example (концепт)

```bash
# ===========================================
# taxlien-gateway — Environment Configuration
# ===========================================
# Copy to .env and set values per environment

# --- Core ---
COMPOSE_PROJECT_NAME=taxlien-gateway-dev
ENV_TAG=dev

# --- Network: отдельный IP для изоляции от других проектов ---
BIND_IP=0.0.0.0

# --- External volumes: БД и raw на хосте ---
DATA_DIR=./data

# --- Ports ---
GATEWAY_PORT=8081
DB_PORT=5432
REDIS_PORT=6379
PROMETHEUS_PORT=9090
GRAFANA_PORT=3000

# --- Secrets (заполнить на сервере) ---
GATEWAY_WORKER_TOKENS=
GRAFANA_PASSWORD=admin

# ===========================================
# Примеры:
# Linux prod (отдельный IP):
#   COMPOSE_PROJECT_NAME=taxlien-gateway-prod
#   ENV_TAG=prod
#   BIND_IP=10.0.0.1
#   DATA_DIR=/opt/taxlien-gateway/prod/data
#
# macOS stage:
#   COMPOSE_PROJECT_NAME=taxlien-gateway-stage
#   ENV_TAG=stage
#   BIND_IP=127.0.0.1
#   DATA_DIR=./data
```

### Directory Structure on Server

**Linux:**
```
/opt/taxlien-gateway/
├── prod/
│   ├── .env
│   ├── docker-compose.yml
│   ├── docker-compose.override.yml
│   ├── data/
│   │   ├── postgres/
│   │   ├── redis/
│   │   ├── raw/
│   │   └── grafana/
│   ├── Dockerfile.gateway
│   ├── cmd/ internal/ pkg/ go.mod go.sum
│   └── monitoring/
├── dev/
└── stage/
```

**macOS:**
```
~/taxlien-gateway/
├── stage/
│   ├── .env              # BIND_IP=127.0.0.1, DATA_DIR=./data
│   ├── data/
│   └── ...
└── dev/
```

## Behavior Specifications

### Happy Path: Push to Branch

1. Push в `dev` → workflow на runner с label `dev`.
2. Checkout, копирование файлов в `${DEPLOY_DIR}/dev/` (сохраняются .env, override, data).
3. `docker-compose build` → образы с тегом `:dev`.
4. `docker-compose down` → `docker-compose up -d`.
5. Health check (warning only при проблемах).
6. Workflow завершается успешно.

### Edge Cases

| Case           | Ожидание                                              |
|----------------|--------------------------------------------------------|
| Нет .env       | Workflow падает с явной ошибкой                        |
| Build failure  | Старые контейнеры остаются запущенными                 |
| Занят порт     | docker-compose up падает, ошибка в логах              |
| DATA_DIR не существует | Создать перед первым up (документировать в README) |

### Error Handling

- `.env` отсутствует → exit 1, контейнеры не трогаем.
- `docker-compose build` упал → exit, старые контейнеры не останавливаем.
- `docker-compose up` упал → залогировать, при необходимости down для консистентности.

## Dependencies

- На сервере: Docker, Docker Compose v2, GitHub Runner с label (prod/dev/stage).
- В runner environment: **DEPLOY_DIR** задан.
- В каждой env-директории: создана структура `data/`, настроен `.env` (BIND_IP, DATA_DIR, секреты).

## Testing Strategy

- Ручная проверка: push в dev → контейнеры с :dev, данные в DATA_DIR не теряются.
- Два окружения на одном сервере с разными BIND_IP → нет конфликтов.
- На macOS: деплой stage, проверка доступа по 127.0.0.1.

## Migration / Rollout

### Первичная настройка (Linux)

1. Установить Docker, Docker Compose, GitHub Runner (labels: prod/dev/stage).
2. `export DEPLOY_DIR=/opt/taxlien-gateway` в окружении runner.
3. Создать каталоги: `mkdir -p /opt/taxlien-gateway/{prod,dev,stage}/data/{postgres,redis,raw,grafana}`.
4. Скопировать `.env.example` в `.env` в каждую env-директорию, задать BIND_IP, DATA_DIR, секреты.
5. Первый деплой скопирует файлы и соберёт образы.

### Первичная настройка (macOS)

1. Docker Desktop, GitHub Runner (например label: stage).
2. `export DEPLOY_DIR=~/taxlien-gateway`.
3. `mkdir -p ~/taxlien-gateway/stage/data/{postgres,redis,raw,grafana}`.
4. `.env`: BIND_IP=127.0.0.1, DATA_DIR=./data (относительно stage/).

## Open Design Questions

- [ ] Имена подкаталогов в DATA_DIR (postgres/redis/raw/grafana) — зафиксировать в спеках.
- [ ] Нужен ли profile для будущих Linux-only сервисов (cadvisor и т.п.) — оставить в workflow для расширяемости.
