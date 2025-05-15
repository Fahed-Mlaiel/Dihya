# seed/ — Seed avancé & données de démonstration (Dihya Coding)

Ce dossier contient les scripts pour injecter des données de démonstration dans la base du backend Dihya Coding.

## Objectif

- Faciliter les tests, la démo et l’onboarding avec des jeux de données réalistes et multilingues.
- Permettre la validation rapide des fonctionnalités (utilisateurs, projets, contenus, etc.).

## Bonnes pratiques

- Ne jamais inclure de données sensibles ou de vrais secrets dans les seeds.
- Logger chaque opération de seed avec horodatage dans un fichier dédié.
- Prévoir des seeds multilingues (français, anglais, dialectes…).
- Valider la cohérence des données après injection.
- Utiliser ces scripts uniquement en environnement de développement ou de test.
- Documenter chaque type de seed dans ce README.

## Exemple d’utilisation

```bash
python demo_data.py