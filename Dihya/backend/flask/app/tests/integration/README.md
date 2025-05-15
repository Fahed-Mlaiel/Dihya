# integration/ — Tests d’intégration backend (Dihya Coding)

Ce dossier regroupe les tests d’intégration pour le backend Flask Dihya Coding.

## Objectif

- Vérifier le bon fonctionnement des modules et composants en interaction réelle (API, base de données, tâches asynchrones, etc.).
- Détecter les régressions et les problèmes d’intégration entre services ou couches applicatives.
- Garantir la robustesse et la conformité des workflows critiques.

## Bonnes pratiques

- Organiser les tests par domaine fonctionnel ou module (`test_auth_integration.py`, `test_api_integration.py`, etc.).
- Utiliser des jeux de données réalistes mais anonymisés.
- Nettoyer l’environnement de test avant/après chaque scénario (base, fichiers, cache…).
- Documenter chaque test (but, prérequis, sécurité, cas limites).
- Prévoir des mocks ou des doubles pour les services externes si besoin.
- Logger les résultats et anomalies pour audit et amélioration continue.

## Exemple de structure

- `test_auth_integration.py` : tests d’intégration du module d’authentification.
- `test_api_integration.py` : tests d’intégration des endpoints API.
- `test_tasks_integration.py` : tests d’intégration des tâches asynchrones.

## Exemple d’utilisation

```bash
pytest app/tests/integration/