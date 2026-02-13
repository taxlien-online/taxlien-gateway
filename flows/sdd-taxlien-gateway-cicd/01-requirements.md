# Requirements: taxlien-gateway CI/CD

> Version: 1.0
> Status: DRAFTED
> Last Updated: 2026-02-12

## Problem Statement

Необходимо автоматизировать процесс деплоя **taxlien-gateway** на различные окружения (prod, dev, stage) при пуше в соответствующие ветки. Документация адаптирована с нуля под данный сервис (референс: CI/CD другого meta-сервиса).

**Ключевые проблемы, которые решает CI/CD:**
- Порты и привязка к 0.0.0.0 — риск конфликтов с другими Docker-проектами на том же хосте
- Нет изоляции по IP — нужен отдельный интерфейс/IP для Docker-стека taxlien-gateway
- Образы без тегов окружения — конфликты при нескольких средах на одном сервере
- Данные БД и raw — должны храниться во внешних томах (external volume), а не только внутри Docker

## Current State

**Репозиторий:** taxlien-gateway

**Сервисы в docker-compose.yml:**

| Сервис      | Порт  | Build                | Описание                    |
|------------|-------|----------------------|-----------------------------|
| gateway-go | 8081  | Dockerfile.gateway   | Go Worker API (v3.0)       |
| db         | 5432  | postgres:16-alpine   | PostgreSQL                 |
| redis      | 6379  | redis:7-alpine       | Redis                      |
| prometheus | 9090  | prom/prometheus      | Метрики                    |
| grafana    | 3000  | grafana/grafana      | Дашборды                   |

**Данные для внешнего хранения:**
- PostgreSQL: `/var/lib/postgresql/data`
- Redis: `/data`
- Raw storage (воркеры): `/data/raw`
- Grafana: `/var/lib/grafana`

**Структура репо:**
```
taxlien-gateway/
├── docker-compose.yml
├── Dockerfile.gateway
├── cmd/gateway/
├── internal/
├── monitoring/
│   ├── prometheus/
│   └── grafana/
└── supabase/migrations/
```

## User Stories

### Primary

**As a** разработчик  
**I want** автоматический деплой при пуше в ветку (prod/dev/stage)  
**So that** я могу быстро доставлять изменения без ручных операций

**As a** DevOps инженер  
**I want** базы данных и raw-данные во внешних томах Docker  
**So that** данные переживают пересоздание контейнеров и бэкапятся с хоста

**As a** оператор  
**I want** у taxlien-gateway свой IP/интерфейс для Docker  
**So that** не было накладок с другими проектами на том же сервере

### Secondary

**As a** разработчик  
**I want** возможность запускать stage на macOS  
**So that** можно тестировать деплой локально или на Mac-инстансе

## Acceptance Criteria

### Must Have

1. **Given** пуш в ветку `prod`/`dev`/`stage`  
   **When** GitHub Actions workflow запускается  
   **Then** self-hosted runner на соответствующем инстансе:
   - Собирает образы локально (в т.ч. gateway из Dockerfile.gateway)
   - Обновляет и перезапускает контейнеры
   - Все сервисы стека (gateway, db, redis, prometheus, grafana) деплоятся вместе

2. **Given** несколько окружений или других проектов на одном сервере  
   **When** taxlien-gateway запущен  
   **Then**:
   - Сервисы привязаны к **конкретному IP** (BIND_IP), а не к 0.0.0.0
   - Разные теги образов по окружениям (`:dev`, `:prod`, `:stage`)
   - Нет конфликтов по портам с другими стеками

3. **Given** базы данных и raw-данные  
   **When** контейнеры пересоздаются при деплое  
   **Then** данные хранятся во **внешних Docker volumes**, примонтированных в host-пути (например `/opt/taxlien-gateway/{env}/data/...`), а не только именованные тома без явного host-пути

4. **Given** Docker-контейнер упал  
   **When** Docker daemon обнаружил это  
   **Then** контейнер автоматически перезапускается (restart: unless-stopped)

5. **Given** деплой на инстанс  
   **When** обновляется docker-compose.yml из репо  
   **Then** локальные `.env` и `docker-compose.override.yml` и **данные (volumes)** сохраняются

6. **Given** новый инстанс настраивается  
   **When** оператор смотрит репозиторий  
   **Then** есть `.env.example` с описанием всех переменных (BIND_IP, порты, пути к данным)

### Should Have

- Ручной триггер workflow (workflow_dispatch)
- Поддержка запуска на **macOS** и **Unix** (stage может быть на macOS)
- Простой health check после деплоя

### Won't Have (This Iteration)

- Blue-green deployment
- Автоматический rollback
- Уведомления (Slack/Telegram)
- Kubernetes

## Technical Decisions

### Сеть и изоляция
- **BIND_IP:** обязательная настройка на сервере; каждый окружение/проект — свой IP или интерфейс.
- **COMPOSE_PROJECT_NAME:** префикс для контейнеров/сетей/томов (изоляция multi-env на одном хосте).

### Хранение данных (external volume)
- **Подход:** именованные тома с driver: local и driver_opts type: none, device: `<host_path>`, o: bind.
- **Либо:** явные host-пути в volumes, например `${DATA_DIR}/postgres`, `${DATA_DIR}/redis`, `${DATA_DIR}/raw`, `${DATA_DIR}/grafana`.
- **Расположение на хосте:** например `/opt/taxlien-gateway/{env}/data/` (Linux) или `~/taxlien-gateway/{env}/data/` (macOS).

### Структура на сервере
```
/opt/taxlien-gateway/   # Linux (или ~/taxlien-gateway на macOS)
├── dev/
│   ├── .env
│   ├── docker-compose.yml
│   ├── docker-compose.override.yml
│   ├── data/           # external volumes
│   │   ├── postgres/
│   │   ├── redis/
│   │   ├── raw/
│   │   └── grafana/
│   └── logs/           # при необходимости
├── prod/
│   └── ...
└── stage/
    └── ...
```

## Constraints

- **Infrastructure:** Self-hosted GitHub Runner на каждом инстансе (или общий с labels).
- **Platform:** Docker + docker-compose; **Linux (Unix)** и **macOS** (в т.ч. для stage).
- **Network:** Отдельный IP/интерфейс для привязки сервисов (не 0.0.0.0 в prod/dev при мульти-проекте).
- **Data:** БД и raw — только через external volume (host path или bind-mounted volume).

## Open Questions

- [ ] Точные host-пути для data на prod/dev/stage (единый стандарт или на усмотрение оператора?)
- [ ] Нужен ли profile для Linux-only сервисов (например cadvisor), если появится — оставить расширяемость

## References

- [GitHub Actions self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners)
- [Docker Compose external volumes / bind mounts](https://docs.docker.com/compose/compose-file/07-volumes/)
- Текущий `docker-compose.yml` и `Dockerfile.gateway` в репозитории taxlien-gateway
