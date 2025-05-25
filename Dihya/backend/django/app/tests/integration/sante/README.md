# Tests d'intégration pour le module Santé

Ce dossier contient les tests d'intégration pour les routes et fonctionnalités santé (API, sécurité, plugins, RGPD, IA, multilingue).

- REST & GraphQL
- JWT, CORS, rôles, audit
- RGPD, logs, anonymisation
- Plugins santé
- Multilingue

---

# Guide d'intégration avancé – Module Santé Dihya

## Objectif
Valider l'intégration complète du module santé : API, sécurité (CORS, JWT, WAF, anti-DDOS), multilingue, RGPD, plugins, audit, accessibilité, SEO, fallback IA, CI/CD, Docker, K8s, fallback local.

## Procédure
- Lancer les tests avec `pytest` ou via CI/CD
- Vérifier la conformité RGPD, audit, accessibilité, multilingue, plugins, SEO
- Couverture : 100% des endpoints santé, logs, anonymisation, export, fallback IA

## Exemples de tests
- Création, lecture, modification, suppression de dossiers santé, anonymisation, export RGPD
- Tests multilingues (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Tests de sécurité (JWT, CORS, WAF, anti-DDOS, RBAC, plugins, audit)
- Tests RGPD (anonymisation, export, logs, auditabilité)
- Tests accessibilité (a11y, ARIA, navigation clavier, contrastes)
- Tests SEO (robots.txt, sitemap.xml dynamiques)
- Tests plugins (ajout dynamique, fallback IA open source)

## Pour aller plus loin
- Voir les tests santé, guides CI/CD, RGPD, audit, accessibilité, plugins, SEO, fallback IA.
- Compatible Codespaces, Linux, CI, production.

---

# Integration Tests for Health Module

(English, العربية, Deutsch, 中文, Español, ...)
