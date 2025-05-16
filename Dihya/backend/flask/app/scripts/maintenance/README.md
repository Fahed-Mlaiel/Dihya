# Scripts de maintenance régulière

Ce dossier regroupe les scripts d’automatisation pour la maintenance régulière du backend Dihya Coding.

## Objectif

- Assurer la stabilité, la sécurité et la performance de la plateforme par des tâches planifiées : purge de logs, rotation des backups, nettoyage des données temporaires, vérification de l’intégrité, etc.
- Centraliser la documentation et l’exécution des opérations de maintenance.

## Bonnes pratiques Dihya Coding

- **Sécurité** : ne jamais supprimer de données critiques sans sauvegarde préalable.
- **Documentation** : chaque script doit être documenté (usage, fréquence, sécurité).
- **Auditabilité** : journaliser chaque opération de maintenance pour traçabilité.
- **Validation** : valider les entrées/sorties pour éviter les erreurs destructrices.
- **Extensibilité** : prévoir l’ajout facile de nouveaux scripts ou tâches planifiées.
- **Portabilité** : scripts compatibles Linux, usage de chemins relatifs, pas de dépendances propriétaires.

## Exemples de scripts à inclure

- `purge_logs.py` : suppression sécurisée des anciens logs
- `rotate_backups.py` : rotation et archivage des sauvegardes
- `cleanup_tmp.py` : nettoyage des fichiers temporaires
- `check_integrity.py` : vérification de l’intégrité des données critiques

## Exemple d’utilisation (cron ou CI/CD)

```bash
python scripts/maintenance/purge_logs.py
python scripts/maintenance/rotate_backups.py
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*