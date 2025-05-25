# Tests d'intégration pour le module Mode

Ce dossier contient les tests d'intégration pour les routes et fonctionnalités mode (API, sécurité, plugins, RGPD, IA, multilingue).

- REST & GraphQL
- JWT, CORS, rôles, audit
- RGPD, logs, anonymisation
- Plugins mode
- Multilingue

---

# Guide d'intégration avancé – Module Mode Dihya

## Objectif
Valider l'intégration complète du module mode : API, sécurité (CORS, JWT, WAF, anti-DDOS), multilingue, RGPD, plugins, audit, accessibilité, SEO, fallback IA, CI/CD, Docker, K8s, fallback local.

## Procédure
- Lancer les tests avec `pytest` ou via CI/CD
- Vérifier la conformité RGPD, audit, accessibilité, multilingue, plugins, SEO
- Couverture : 100% des endpoints mode, logs, anonymisation, export, fallback IA

## Exemples de tests
- Création, lecture, modification, suppression d'articles, anonymisation, export RGPD
- Tests multilingues (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Tests de sécurité (JWT, CORS, WAF, anti-DDOS, RBAC, plugins, audit)
- Tests RGPD (anonymisation, export, logs, auditabilité)
- Tests accessibilité (a11y, ARIA, navigation clavier, contrastes)
- Tests SEO (robots.txt, sitemap.xml dynamiques)
- Tests plugins (ajout dynamique, fallback IA open source)

## Pour aller plus loin
- Voir les tests mode, guides CI/CD, RGPD, audit, accessibilité, plugins, SEO, fallback IA.
- Compatible Codespaces, Linux, CI, production.

---

# Integration Tests for Fashion Module

(English, العربية, Deutsch, 中文, Español, ...)
