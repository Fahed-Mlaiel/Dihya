# Tests d'intégration : Intelligence Artificielle

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés à l'intelligence artificielle dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques IA

## Structure
- `test_intelligence_artificielle_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Integration tests: Artificial Intelligence

This folder contains advanced integration tests for AI routes and modules in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n
- Multitenancy, roles
- GDPR, auditability
- AI plugins/extensions

## Structure
- `test_intelligence_artificielle_routes.py`: API, security, i18n, plugins
- Fixtures, mocks, logs

## Run
```bash
pytest --tb=short --maxfail=1
```
