# scheduler/ — Gestion des tâches planifiées et jobs périodiques (Dihya Coding)

Ce dossier centralise la déclaration, la planification et la gestion sécurisée des tâches planifiées (cron jobs, jobs périodiques, maintenance automatique, etc.) pour le backend Flask Dihya Coding.

## Objectif

- Permettre l’exécution automatique de tâches à intervalles réguliers ou différés (nettoyage, rapports, notifications, etc.).
- Garantir la sécurité, la traçabilité et la robustesse des traitements planifiés.
- Faciliter l’extension à de nouveaux jobs ou tâches récurrentes.

## Bonnes pratiques

- Déclarer chaque tâche planifiée dans un fichier dédié (`cleanup_jobs.py`, `report_jobs.py`, etc.).
- Documenter chaque job avec une docstring claire (fréquence, but, sécurité).
- Protéger les jobs critiques par des vérifications de permissions et de contexte.
- Logger l’exécution, les succès et les erreurs pour audit et monitoring.
- Prévoir des tests unitaires pour chaque job planifié.
- Ne jamais traiter de données sensibles sans validation ou chiffrement préalable.
- Utiliser des outils robustes (APScheduler, Celery Beat, cron) pour la production.

## Exemple de structure

- `cleanup_jobs.py` : tâches de nettoyage automatique (logs, fichiers temporaires, etc.).
- `report_jobs.py` : génération périodique de rapports.
- `notification_jobs.py` : envoi programmé de notifications.

## Exemple d’utilisation

```python
from app.scheduler.cleanup_jobs import schedule_cleanup
from app.scheduler.report_jobs import generate_daily_report

schedule_cleanup()
generate_daily_report()