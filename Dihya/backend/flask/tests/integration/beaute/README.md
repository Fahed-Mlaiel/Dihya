# Tests d'intégration : Beauté

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés à la beauté dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques beauté

## Structure
- `test_beaute_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Integration tests: Beauty

This folder contains advanced integration tests for beauty routes and modules in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n
- Multitenancy, roles
- GDPR, auditability
- Beauty plugins/extensions

## Structure
- `test_beaute_routes.py`: API, security, i18n, plugins
- Fixtures, mocks, logs

## Run
```bash
pytest --tb=short --maxfail=1
```
