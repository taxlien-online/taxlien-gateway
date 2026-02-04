# Status: sdd-taxlien-gateway-legacy-python

## Purpose

**Legacy Python Gateway:** миграция/архивирование кода из `taxlien-gateway/legacy/`. Целевая архитектура — **v3.0 Minimal** (см. `sdd-taxlien-gateway`): один порт :8081, только Worker API; прокси и публичный API не входят в Gateway.

## Current Phase

REQUIREMENTS ✅ | SPECIFICATIONS ✅ | PLAN ✅ | **IMPLEMENTATION** (legacy migration)

## Phase Status

ON HOLD — целевой продукт: Go v3.0 Minimal (sdd-taxlien-gateway)

## Last Updated

2026-02-04

## Blockers

- Нет. Текущий фокус — v3.0 Minimal в основном flow.

## Progress

- [x] Requirements drafted (v1.0, Tri-Port)
- [x] Specifications drafted (v1.0); уточнено: proxy не в зоне Gateway (tor-socks-proxy у воркеров)
- [x] Plan drafted
- [x] Реализация v1.1 (Python) завершена; код в `legacy/`
- [ ] Tri-Port (v1.2) не реализовывать — заменён на v3.0 Minimal

## Context Notes

- **tor-socks-proxy:** Gateway не управляет прокси. Воркеры подключаются к tor-socks-proxy сами; в спеках proxy endpoints помечены как удалённые.
- **Связь с sdd-taxlien-gateway:** основной flow перешёл на v3.0 (Go, один порт). Этот flow описывает существующий Python-код и его возможную миграцию/архивацию.