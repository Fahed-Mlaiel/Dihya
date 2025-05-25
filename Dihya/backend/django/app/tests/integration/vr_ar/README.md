# Tests d'intégration VR/AR pour Dihya Coding

Ce dossier contient les tests d'intégration avancés pour les routes et services liés à la Réalité Virtuelle (VR) et la Réalité Augmentée (AR) dans le backend Django du projet Dihya.

## Objectifs
- Vérifier l'intégration REST/GraphQL des endpoints VR/AR
- Tester la sécurité (authentification JWT, rôles, CORS, WAF, anti-DDOS)
- Valider l'internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Couvrir les cas d'usage métier (création, gestion, export, audit, anonymisation)
- Mock des services IA (LLaMA, Mixtral, Mistral)
- Vérifier la conformité RGPD et l'auditabilité

## Structure
- `test_vr_ar_django.py` : tests d'intégration complets (REST, GraphQL, sécurité, i18n, plugins, audit)
- Fixtures et mocks intégrés

## Exécution

```bash
pytest --maxfail=1 --disable-warnings -v ./Dihya/backend/django/app/tests/integration/vr_ar/
```

## Multilingue
- Ce README est disponible en français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol (voir docs racine)

---

# Integration Tests VR/AR for Dihya Coding

This folder contains advanced integration tests for VR/AR routes and services in the Dihya Django backend.

(See above for objectives, structure, and execution)
