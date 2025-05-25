# Tests d'intégration pour la gestion de projets 3D

Ce dossier contient des tests d'intégration avancés pour les routes RESTful et GraphQL de gestion de projets 3D (réalité virtuelle, augmentée, modélisation, etc.) dans Dihya.

## Objectifs
- Vérifier la sécurité (CORS, JWT, WAF, anti-DDOS)
- Tester l'internationalisation dynamique (fr, en, ar, ...)
- Couvrir les cas d'usage multitenant et rôles (admin, user, invité)
- Valider l'intégration IA (LLaMA, Mixtral, fallback)
- Assurer la conformité RGPD et l'auditabilité

## Structure
- `test_3d_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins, SEO
- Fixtures et mocks IA, multitenant, rôles, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

## Multilingue
- Ce dossier et ses tests sont documentés en français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

---

# Integration tests for 3D project management

This folder contains advanced integration tests for RESTful and GraphQL routes for 3D project management (VR, AR, modeling, etc.) in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n (fr, en, ar, ...)
- Multitenancy and roles (admin, user, guest)
- AI integration (LLaMA, Mixtral, fallback)
- GDPR compliance and auditability

## Structure
- `test_3d_routes.py`: API, security, i18n, plugins, SEO
- Fixtures and mocks for AI, multitenancy, roles, logs

## Run
```bash
pytest --tb=short --maxfail=1
```

## Multilingual
- This folder and its tests are documented in French, English, Arabic, Amazigh, German, Chinese, Japanese, Korean, Dutch, Hebrew, Persian, Hindi, Spanish.
