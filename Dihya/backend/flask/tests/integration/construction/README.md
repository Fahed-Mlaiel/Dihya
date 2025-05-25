# Tests d'intégration : Construction

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés à la construction dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques construction

## Structure
- `test_construction_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Integration tests: Construction

This folder contains advanced integration tests for construction routes and modules in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n
- Multitenancy, roles
- GDPR, auditability
- Construction plugins/extensions

## Structure
- `test_construction_routes.py`: API, security, i18n, plugins
- Fixtures, mocks, logs

## Run
```bash
pytest --tb=short --maxfail=1
```
