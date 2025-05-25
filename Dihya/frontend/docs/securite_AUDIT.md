# Audit Sécurité – Dihya

## Objectif
Garantir la sécurité maximale de l’API, du frontend, des plugins et des données (CORS, JWT, WAF, anti-DDOS, audit, RGPD, SEO, accessibilité).

## Checklist Sécurité
- CORS strict (origines autorisées dynamiques)
- JWT (expiration, rotation, blacklist, scopes)
- WAF (Web Application Firewall, signatures personnalisées)
- Anti-DDOS (rate limiting, captchas, logs)
- RBAC (admin, user, invité, multitenancy)
- Plugins sécurité (API/CLI, auditables)
- Logs structurés, auditables, exportables
- RGPD (anonymisation, export, consentement)
- Tests sécurité (unitaires, intégration, e2e, CI/CD)
- SEO (robots.txt, sitemap, logs SEO)
- Accessibilité (WCAG, logs, tests automatiques)

## Procédures d’audit
- Audit automatisé (CI/CD, GitHub Actions, Docker, K8s)
- Audit manuel (scripts, checklist, export logs)
- Audit RGPD (export, anonymisation, consentement)

## Exemples de tests
```bash
# Test CORS
curl -H "Origin: https://example.com" https://api.dihya.local/api/tourisme/sites
# Test JWT
curl -H "Authorization: Bearer <token>" https://api.dihya.local/api/transport/flottes
```

## Structure
- Code, tests, assets, configs, docs, plugins, policies, etc.
