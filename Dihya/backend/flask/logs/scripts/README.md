# logs/scripts/ — Scripts de purge & rotation des logs (Dihya Coding)

Ce dossier contient les scripts permettant de gérer la purge, l’archivage et la rotation des fichiers de logs du backend Dihya Coding.

## Objectif

- Limiter l’encombrement disque et garantir la confidentialité des logs.
- Respecter la conformité RGPD et la souveraineté numérique par une gestion maîtrisée des traces.

## Bonnes pratiques

- Ne jamais supprimer de logs critiques sans backup préalable.
- Logger chaque opération de purge ou d’archivage avec horodatage.
- Prévoir une politique de rétention configurable (nombre de jours, taille max, etc.).
- Restreindre l’accès à ces scripts aux administrateurs.
- Tester la validité des archives après rotation.
- Documenter chaque script et sa politique de gestion.

## Exemple d’utilisation

```bash
python purge_logs.py