# cleaning/ — Scripts de nettoyage et purge (Dihya Coding)

Ce dossier regroupe les scripts de nettoyage et de purge pour le backend Flask Dihya Coding.

## Objectif

- Automatiser le nettoyage des fichiers temporaires, logs obsolètes, données expirées ou inutilisées.
- Garantir la performance, la sécurité et la conformité du système en limitant l’accumulation de données inutiles.
- Faciliter la maintenance régulière et la gestion de l’espace disque.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Logger les opérations de nettoyage pour audit et conformité.
- Prévoir des options de dry-run pour éviter les suppressions accidentelles.
- Ne jamais supprimer de données critiques sans sauvegarde préalable.
- Respecter la conformité RGPD pour la suppression des données personnelles.

## Exemple de structure

- `purge_temp_files.sh` : suppression des fichiers temporaires.
- `clean_old_logs.sh` : nettoyage des logs anciens ou volumineux.
- `delete_expired_data.py` : suppression des données expirées en base.
- `dry_run_example.sh` : exemple de script avec option dry-run.

## Exemple d’utilisation

```bash
bash purge_temp_files.sh --dry-run
python delete_expired_data.py --confirm