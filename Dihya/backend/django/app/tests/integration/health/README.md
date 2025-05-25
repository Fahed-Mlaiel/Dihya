# Tests d'intégration – Module Health Dihya

## Objectif
Valider l'intégration complète du module health (API, sécurité, multilingue, RGPD, plugins, audit, accessibilité, CI/CD, Docker, K8s, fallback local).

## Procédure
- Lancer les tests avec `pytest` ou via CI/CD
- Vérifier la conformité RGPD, audit, accessibilité, multilingue, plugins
- Couverture : 100% des endpoints health, logs, anonymisation, export, fallback IA

## Exemples de tests
- Création, lecture, modification, suppression de dossiers patients
- Tests multilingues (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Tests de sécurité (JWT, CORS, WAF, anti-DDOS, RBAC, plugins, audit)
- Tests RGPD (anonymisation, export, logs, auditabilité)
- Tests accessibilité (a11y, ARIA, navigation clavier, contrastes)

## Pour aller plus loin
- Voir les tests health, guides CI/CD, RGPD, audit, accessibilité, plugins, SEO, fallback IA.
