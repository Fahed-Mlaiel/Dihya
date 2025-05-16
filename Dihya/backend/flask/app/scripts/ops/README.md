# scripts/ops

Documentation interne Dihya Coding.

## Objectif

Ce dossier regroupe les scripts d’opérations manuelles, d’urgence ou de maintenance rapide pour l’équipe technique Dihya Coding.

## Bonnes pratiques

- **Usage restreint** : ces scripts sont réservés aux administrateurs ou DevOps.
- **Auditabilité** : chaque script doit logger ses actions et justifier son usage.
- **Sécurité** : ne jamais inclure de credentials ou secrets en clair.
- **Validation** : toute modification doit être validée par un pair avant exécution en production.
- **Documentation** : chaque script doit contenir une docstring expliquant son but, ses paramètres et ses risques.

## Exemples de scripts présents

- `emergency_migration.py` : appliquer ou restaurer une migration critique en urgence.
- `emergency_backup.py` : (à ajouter) effectuer un backup manuel rapide de la base.
- `emergency_restore.py` : (à ajouter) restaurer un backup en cas de failover.

## Exemple d’utilisation

```bash
python emergency_migration.py upgrade head
python emergency_migration.py downgrade <revision_id>
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*