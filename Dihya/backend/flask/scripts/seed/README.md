# seed/ — Scripts de seed et d’initialisation de données (Dihya Coding)

Ce dossier regroupe les scripts de seed permettant d’initialiser ou de réinitialiser les jeux de données pour le backend Flask Dihya Coding.

## Objectif

- Automatiser la création de jeux de données de base pour le développement, les tests ou la démonstration.
- Garantir la reproductibilité des environnements et la cohérence des scénarios de test.
- Faciliter l’onboarding des nouveaux contributeurs et la mise en place d’environnements de test.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Ne jamais inclure de données sensibles ou de secrets réels dans les seeds.
- Prévoir des options pour réinitialiser, compléter ou enrichir les données existantes.
- Logger les opérations de seed pour audit et traçabilité.
- Nettoyer l’environnement cible avant d’injecter de nouveaux jeux de données si besoin.
- Prévoir des seeds adaptés à chaque environnement (développement, test, démo).

## Exemple de structure

- `seed_users.py` : création d’utilisateurs de test.
- `seed_projects.py` : création de projets ou de contenus de démonstration.
- `seed_full_demo.py` : seed complet pour un environnement de démo.

## Exemple d’utilisation

```bash
python seed_users.py
python seed_full_demo.py --reset