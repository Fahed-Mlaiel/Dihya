# 🧪 Exemples de tests & automatisation – Dihya

Ce fichier centralise des exemples de tests unitaires, d’intégration, e2e, audit, RGPD, accessibilité, fallback, monitoring, plugins, CI/CD pour chaque stack et dossier métier du projet.

## Tests unitaires
- Python : `pytest tests/test_module.py`
- Node.js : `npm test`
- React : `npm run test`

## Tests d’intégration
- Django : `pytest tests/integration/`
- Node.js : `npm run test:integration`

## Tests e2e
- Playwright : `npx playwright test`
- Cypress : `npx cypress run`

## Audit & RGPD
- Python : `python3 audit.py` / `python3 export_rgpd.py`
- Node.js : `node audit.js` / `node export_rgpd.js`

## Accessibilité
- Axe CLI : `npx axe . --tags wcag2a,wcag2aa`
- Lighthouse : `npx lighthouse http://localhost:3000 --accessibility`

## Fallback
- `python3 fallback.py` / `node fallback.js`

## Monitoring
- `python3 monitoring.py` / `node monitoring.js`

## Plugins
- `node plugin.js --test` / `python3 plugin.py --test`

## CI/CD
- GitHub Actions : `.github/workflows/*.yml` (tests, audit, export, artefacts)

## Bonnes pratiques
- Automatiser tous les tests et audits à chaque push/PR
- Générer des artefacts et logs pour chaque module
- Documenter toute non-conformité et action corrective
