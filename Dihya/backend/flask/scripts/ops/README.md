# ops/ — Scripts d’opérations et de maintenance (Dihya Coding)

Ce dossier regroupe tous les scripts d’opérations, de maintenance et d’administration pour le backend Flask Dihya Coding.

## Objectif

- Centraliser les scripts utiles à l’exploitation, la supervision et la maintenance du backend.
- Automatiser les tâches récurrentes pour fiabiliser les opérations.
- Garantir la sécurité et la traçabilité des actions d’administration.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications de permissions ou d’environnement.
- Logger les actions importantes pour audit et conformité.
- Ne jamais inclure de secrets ou de données sensibles en clair dans les scripts.
- Prévoir des tests ou des dry-run pour les scripts à effet destructeur.
- Respecter la conformité RGPD et les bonnes pratiques DevOps.

## Exemples de scripts à placer ici

- `restart_services.sh` : redémarrage contrôlé des services backend.
- `purge_temp_files.sh` : nettoyage des fichiers temporaires.
- `rotate_logs.sh` : rotation et archivage des logs applicatifs.
- `update_dependencies.sh` : mise à jour automatisée des dépendances.
- `check_health.sh` : vérification de l’état de santé des services.

## Exemple d’utilisation

```bash
bash restart_services.sh
bash purge_temp_files.sh --dry-run