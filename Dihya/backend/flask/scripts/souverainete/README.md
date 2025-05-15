# souverainete/ — Scripts de souveraineté numérique (Dihya Coding)

Ce dossier regroupe les scripts dédiés à la souveraineté numérique pour le backend Flask Dihya Coding.

## Objectif

- Automatiser la gestion, l’export, l’import et la protection des données pour garantir l’indépendance et la maîtrise des actifs numériques.
- Faciliter la migration, la portabilité et la conformité aux exigences de souveraineté (localisation, contrôle, audit).

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Logger toutes les opérations pour audit et conformité.
- Ne jamais inclure de secrets ou de données sensibles en clair dans les scripts ou les logs.
- Prévoir des tests ou des dry-run pour les scripts à effet destructeur.
- Respecter les politiques internes et réglementaires sur la localisation et la portabilité des données.

## Exemple de structure

- `export_data.py` : export des données pour migration ou sauvegarde souveraine.
- `import_data.py` : import de données dans un nouvel environnement.
- `anonymize_data.py` : anonymisation avancée pour la protection des données.
- `audit_souverainete.py` : audit de la conformité souveraineté.

## Exemple d’utilisation

```bash
python export_data.py --format json --output export_2025-05-15.json
python import_data.py --input export_2025-05-15.json