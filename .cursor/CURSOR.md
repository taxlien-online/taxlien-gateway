# Sub-Project Rules: Swipe App Implementation

## Coding Standards
- **Interceptors:** Все запросы только через `GatewayClient` с инъекцией Firebase Token.
- **Testing:** Начинай каждую задачу с написания теста (TDD).
- **Models:** Используй `FVI` и `Annotation` модели из общей спецификации.

## Context
- Этот проект не имеет доступа к БД напрямую.
- Все данные поступают от API Gateway (порт :8080).
