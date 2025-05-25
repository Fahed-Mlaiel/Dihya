# Dihya Migrations Scripts

Ce dossier contient les scripts de migration de données pour Dihya Coding.

## Fonctionnalités
- Migration automatisée, rollback, audit, RGPD
- Sécurité maximale (validation, anonymisation, logs)
- Multitenancy, rôles, plugins
- Compatible CI/CD, Docker, K8s, Codespaces

## Structure
- `index.js` : orchestrateur principal
- Un script par migration (ex: `2025-05-25_add_projects.js`)

## Utilisation
1. Ajouter un script dans ce dossier
2. Lancer `node index.js up` ou `node index.js down`

## Tests
- Couverture unitaire et intégration

---

# Dihya Migrations Scripts (English)

This folder contains all data migration scripts for Dihya Coding.

See above for features and usage.
