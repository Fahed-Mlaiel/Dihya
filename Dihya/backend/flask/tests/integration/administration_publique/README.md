# Tests d'intégration : Administration Publique

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés à l'administration publique dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques secteur public

## Structure
- `test_admin_publique_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Integration tests: Public Administration

This folder contains advanced integration tests for public administration routes and modules in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n
- Multitenancy, roles
- GDPR, auditability
- Public sector plugins/extensions

## Structure
- `test_admin_publique_routes.py`: API, security, i18n, plugins
- Fixtures, mocks, logs

## Run
```bash
pytest --tb=short --maxfail=1
```
