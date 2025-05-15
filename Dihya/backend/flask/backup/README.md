# backup/ — Sauvegardes avancées Backend Dihya Coding

Ce dossier regroupe les modules et scripts permettant la sauvegarde automatique et manuelle des données critiques du backend Dihya Coding.

## Objectif

- Assurer la résilience et la traçabilité du projet par des backups réguliers et multi-supports.
- Permettre la sauvegarde sur différents supports : local, cloud, Notion API, etc.

## Bonnes pratiques

- Ne jamais inclure de données sensibles ou de secrets dans les backups publics.
- Protéger les tokens/API keys via les variables d’environnement.
- Logger chaque opération de backup/restauration avec horodatage.
- Gérer les erreurs, quotas API et la confidentialité des données.
- Tester régulièrement la restauration à partir des backups.

## Contenu

- **notion.py** : Module pour sauvegarder des logs/métadonnées dans une base Notion via l’API officielle.
- (Ajouter ici d’autres modules pour d’autres supports de backup si besoin.)

## Exemple d’utilisation

```python
from backup.notion import backup_to_notion

backup_to_notion("Backup automatique du 2025-05-15", {"type": "db", "status": "ok"})