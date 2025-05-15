# migrations/scripts/ — Scripts de migration personnalisée (Dihya Coding)

Ce dossier contient des scripts Python pour effectuer des migrations manuelles ou avancées sur la base de données du backend Dihya Coding, en complément des outils ORM classiques.

## Objectif

- Permettre des migrations spécifiques (ajout de colonne, migration de données, corrections, etc.) non couvertes par les migrations automatiques.
- Assurer la traçabilité, la sécurité et la robustesse des évolutions de schéma.

## Bonnes pratiques

- Toujours sauvegarder la base de données avant toute migration (voir scripts de backup).
- Logger chaque opération de migration avec horodatage dans un fichier dédié.
- Valider le schéma et les données après chaque migration.
- Ne jamais inclure de données sensibles dans les logs ou les scripts.
- Documenter chaque étape de la migration dans le script et dans ce README.
- Tester chaque script sur une base de test avant production.

## Exemple de script

Voir `example_migration.py` pour un ajout de colonne simple.

## Exécution

```bash
python example_migration.py