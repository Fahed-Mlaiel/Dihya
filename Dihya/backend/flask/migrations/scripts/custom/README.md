# custom/ — Scripts de migration personnalisés (Dihya Coding)

Ce dossier regroupe les scripts de migration personnalisés pour le backend Flask Dihya Coding.

## Objectif

- Permettre la gestion fine des évolutions de schéma, des migrations de données ou des opérations spécifiques non couvertes par les outils standards.
- Faciliter la maintenance, la traçabilité et la reproductibilité des changements de structure ou de données.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, dépendances, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Logger les actions importantes pour audit et conformité.
- Prévoir des tests ou des dry-run pour les scripts à effet destructeur.
- Ne jamais inclure de données sensibles ou de secrets dans les scripts ou les logs.
- Versionner chaque script et documenter l’ordre d’exécution si nécessaire.

## Exemple de structure

- `add_indexes.py` : ajout d’index spécifiques.
- `migrate_custom_data.py` : migration de données métier.
- `cleanup_legacy_fields.py` : suppression de champs obsolètes.

## Exemple d’utilisation

```bash
python add_indexes.py
python migrate_custom_data.py --dry-run