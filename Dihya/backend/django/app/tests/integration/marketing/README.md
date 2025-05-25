# Tests d'intégration pour le module Marketing

Ce dossier contient les tests d'intégration pour les routes et fonctionnalités marketing du backend Dihya.

## Objectifs
- Vérifier l'intégration complète des endpoints marketing (REST & GraphQL)
- Tester la sécurité (CORS, JWT, rôles, audit)
- Couverture multilingue (fr, en, ar, etc.)
- Mock des services IA (LLaMA, Mixtral, fallback)
- Validation RGPD, logs, anonymisation

## Exécution

```bash
pytest --tb=short --disable-warnings
```

## Structure
- `test_marketing_django.py` : tests d'intégration complets

## Multilingue
Les tests vérifient la réponse dans toutes les langues supportées.

## Sécurité
- JWT obligatoire
- CORS strict
- Audit log vérifié

## Plugins
Les plugins marketing sont testés via des fixtures dynamiques.

---

# Integration Tests for Marketing Module

This folder contains integration tests for the marketing backend routes and features.

(English, العربية, Deutsch, 中文, Español, ...)
