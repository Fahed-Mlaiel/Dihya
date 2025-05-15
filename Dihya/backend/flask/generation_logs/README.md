# generation_logs/ — Traçabilité des générations de code (Dihya Coding)

Ce dossier contient les outils et scripts pour journaliser chaque génération de projet (frontend, backend, assets, etc.) avec horodatage, type, utilisateur et métadonnées.

## Objectif

- Assurer la traçabilité et la transparence de chaque génération de code.
- Faciliter l’audit, la conformité et la résolution d’incidents.
- Respecter la souveraineté numérique et la sécurité des données.

## Bonnes pratiques

- Chaque log doit inclure : date, heure, type de génération, auteur (si connu), identifiant unique, métadonnées.
- Ne jamais stocker de secrets ou de données sensibles dans les logs.
- Prévoir une rotation et une purge régulière des fichiers de logs.
- Restreindre l’accès aux logs aux administrateurs ou à des fins d’audit.
- Utiliser un format structuré (JSON) pour faciliter l’analyse automatisée.

## Exemple d’utilisation

```python
from generation_logs import log_generation_event

log_generation_event("backend", user="alice", meta={"stack": "Flask"})