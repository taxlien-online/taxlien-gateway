# Implementation Plan: taxlien-gateway CI/CD

> Version: 1.0
> Status: DRAFTED
> Last Updated: 2026-02-12
> Specifications: ./02-specifications.md

## Summary

Реализация CI/CD для taxlien-gateway: параметризованный docker-compose (BIND_IP, external volumes для БД и raw), .env.example, GitHub Actions deploy workflow. Поддержка Linux и macOS; отдельный IP для изоляции.

## Task Breakdown

### Phase 1: Docker Compose Parameterization

#### Task 1.1: Привязка к BIND_IP и параметризация портов
- **Description:** Все сервисы биндятся на `${BIND_IP}` и порты из переменных.
- **Files:** `docker-compose.yml`
- **Verification:** `docker-compose config` показывает BIND_IP и порты; без .env — дефолты.
- **Complexity:** Low

#### Task 1.2: Теги образов по окружению
- **Description:** Образ gateway (и при необходимости остальных) с тегом `${ENV_TAG:-latest}`.
- **Files:** `docker-compose.yml`
- **Verification:** При ENV_TAG=prod образы с суффиксом :prod.
- **Complexity:** Low

#### Task 1.3: External volumes для БД и raw
- **Description:** Заменить именованные тома на host-пути через `${DATA_DIR}/postgres`, `${DATA_DIR}/redis`, `${DATA_DIR}/raw`, `${DATA_DIR}/grafana`.
- **Files:** `docker-compose.yml`
- **Verification:** После down/up данные остаются в DATA_DIR на хосте.
- **Complexity:** Low

#### Task 1.4: COMPOSE_PROJECT_NAME и изоляция
- **Description:** В документации и .env.example задать использование COMPOSE_PROJECT_NAME для изоляции контейнеров/сетей (значение из .env на сервере).
- **Files:** `docker-compose.yml` (при необходимости явно не менять, т.к. project name задаётся через env), `.env.example`
- **Verification:** Два окружения на одном хосте не пересекаются по именам ресурсов.
- **Complexity:** Low

### Phase 2: Environment Configuration

#### Task 2.1: Создание .env.example
- **Description:** Шаблон с BIND_IP, DATA_DIR, портами, GATEWAY_WORKER_TOKENS, GRAFANA_PASSWORD и примерами для Linux/macOS.
- **Files:** `.env.example` (Create)
- **Verification:** Копия в .env позволяет запустить docker-compose с корректными путями.
- **Complexity:** Low

#### Task 2.2: .gitignore
- **Description:** Убедиться, что `.env` в .gitignore.
- **Files:** `.gitignore`
- **Verification:** .env не коммитится.
- **Complexity:** Low

### Phase 3: GitHub Actions Workflow

#### Task 3.1: Базовый deploy.yml
- **Description:** Триггеры: push в prod/dev/stage и workflow_dispatch. Job на self-hosted с label по окружению.
- **Files:** `.github/workflows/deploy.yml` (Create)
- **Verification:** Workflow виден в GitHub Actions.
- **Complexity:** Medium

#### Task 3.2: Проверка DEPLOY_DIR и .env
- **Description:** Step валидации: DEPLOY_DIR задан, в TARGET_DIR есть .env.
- **Files:** `.github/workflows/deploy.yml`
- **Verification:** При отсутствии .env workflow падает с понятной ошибкой.
- **Complexity:** Low

#### Task 3.3: Копирование файлов и деплой
- **Description:** Копировать в TARGET_DIR: docker-compose.yml, Dockerfile.gateway, cmd/, internal/, pkg/, go.mod, go.sum, migrations/ (если нужны для образа), monitoring/. Затем build, down, up. Определение OS для --profile linux при необходимости.
- **Files:** `.github/workflows/deploy.yml`
- **Verification:** Деплой на тестовом runner завершается успешно.
- **Complexity:** Medium

#### Task 3.4: Health check (optional)
- **Description:** После up — sleep и docker-compose ps; при желании curl /health (warning only).
- **Files:** `.github/workflows/deploy.yml`
- **Verification:** Не падает workflow при временной недоступности сервиса.
- **Complexity:** Low

### Phase 4: Documentation & Verification

#### Task 4.1: README
- **Description:** Секция CI/CD: настройка DEPLOY_DIR, структура data/, .env, BIND_IP, пример для Linux и macOS.
- **Files:** `README.md`
- **Verification:** По README можно настроить новый инстанс.
- **Complexity:** Low

#### Task 4.2: Локальная проверка
- **Description:** Локально docker-compose config с .env; при наличии DATA_DIR — up и проверка томов.
- **Files:** —
- **Verification:** config без ошибок, данные пишутся в DATA_DIR.
- **Complexity:** Low

## Dependency Graph

```
Phase 1 (Compose)     Phase 2 (Env)      Phase 3 (Workflow)    Phase 4
1.1 BIND_IP/ports ──┐
1.2 ENV_TAG ────────┼──→ 2.1 .env.example  →  3.1 deploy.yml   →  4.1 README
1.3 DATA_DIR vols ──┤    2.2 .gitignore      3.2 validation      4.2 local test
1.4 COMPOSE_PROJECT ┘                        3.3 deploy step
                                             3.4 health check
```

## File Change Summary

| File                         | Action  | Reason                                    |
|-----------------------------|---------|-------------------------------------------|
| docker-compose.yml          | Modify  | BIND_IP, порты, ENV_TAG, external volumes |
| .env.example                | Create  | Шаблон конфигурации                       |
| .github/workflows/deploy.yml| Create  | Деплой по веткам + workflow_dispatch      |
| .gitignore                  | Modify  | .env (если ещё не добавлен)               |
| README.md                   | Modify  | Секция CI/CD                              |

## Risk Assessment

| Risk                         | Mitigation                                      |
|-----------------------------|--------------------------------------------------|
| Нет прав на DATA_DIR на хосте | Документировать создание каталогов и ownership  |
| BIND_IP не настроен на хосте | Описать в .env.example и README                 |
| Разные версии docker-compose | Использовать синтаксис v2/v3                    |

## Rollback

- Изменения в git; откат через revert.
- На сервере .env и data/ при деплое не перезаписываются; старые контейнеры остаются до успешного up.

## Checkpoints

- После Phase 1: `docker-compose config` с .env без ошибок; volumes указывают на DATA_DIR.
- После Phase 2: .env.example полный; .env в .gitignore.
- После Phase 3: Push в dev триггерит deploy; контейнеры поднимаются.
- После Phase 4: README обновлён; локальный прогон пройден.
