# Dihya AI – Guide d’intégration avancée

Ce dossier fournit toutes les fonctionnalités IA souveraines, multilingues, RGPD, audit, plugins, REST/GraphQL-ready pour le projet Dihya.

## Intégration Python (Django/Flask/FastAPI)
- Utilisez `generate_ai_response`, `select_engine`, `SUPPORTED_LANGUAGES`, `DihyaAIConfig`.
- Voir `main.py`, `views.py`, `schemas.py`, `urls.py` pour REST/GraphQL.
- Sécurité : CORS, JWT, audit, logs RGPD, plugins, multitenancy, fallback IA open source.

## Intégration Node.js (Express/GraphQL)
- Utilisez `generateAIResponse`, `selectEngine`, `SUPPORTED_LANGUAGES`, `config`.
- Voir `index.js`, `ai.js`, `test_ai.js` pour REST/GraphQL.

## Plugins & automatisation
- Plugins dynamiques (API/CLI), audit, RGPD, export, tests, fallback IA.
- Génération automatique de fixtures/tests, audit, export RGPD.

## CI/CD
- Tests automatisés sur la génération IA, audit, RGPD, plugins, logs, export.
- Intégration GitHub Actions, Docker, K8s, fallback local.

## Historique & audit
- Voir `audit.py`, logs structurés, export RGPD, plugins, tests.

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
