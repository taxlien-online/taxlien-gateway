# Status: sdd-taxlien-gateway-cicd

## Current Phase

REQUIREMENTS

## Phase Status

DRAFTED

## Last Updated

2026-02-12

## Blockers

- None

## Progress

- [x] Requirements drafted
- [ ] Requirements approved
- [x] Specifications drafted
- [ ] Specifications approved
- [x] Plan drafted
- [ ] Plan approved
- [ ] Implementation started
- [ ] Implementation complete

## Context Notes

- CI/CD для **taxlien-gateway** (не tor-socks-proxy-service). Доки адаптированы с нуля.
- Целевые ветки: prod, dev, stage → соответствующие инстансы.
- Self-hosted GitHub Runner; запуск возможен на **macOS** и **Unix** (stage иногда на macOS).
- **Базы данных и raw-данные** — через **external Docker volume** (хранение на хосте).
- Docker с **отдельным IP (собственный интерфейс)** — без накладок с другими проектами.

## Fork History

N/A — Refactored from scratch for taxlien-gateway (source: meta-service tor-socks-proxy CI/CD concept).

## Next Actions

1. Уточнить требования через диалог при необходимости
2. Получить approval на requirements → specifications → plan
3. Приступить к реализации по плану
