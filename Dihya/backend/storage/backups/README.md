# Backups – Dihya Backend Storage

Ce dossier contient les sauvegardes chiffrées de la base de données et des fichiers critiques.

## Bonnes pratiques
- Toujours chiffrer les backups (AES-256, GPG)
- Versionner et journaliser chaque backup
- Tester la restauration régulièrement
- Stocker hors site pour la résilience

---

> Voir les scripts de backup dans `../../scripts/backup/`.
