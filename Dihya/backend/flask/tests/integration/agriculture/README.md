# Tests d'intégration : Agriculture

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés à l'agriculture dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques agriculture

## Structure
- `test_agriculture_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Integration tests: Agriculture

This folder contains advanced integration tests for agriculture routes and modules in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n
- Multitenancy, roles
- GDPR, auditability
- Agriculture plugins/extensions

## Structure
- `test_agriculture_routes.py`: API, security, i18n, plugins
- Fixtures, mocks, logs

## Run
```bash
pytest --tb=short --maxfail=1
```
