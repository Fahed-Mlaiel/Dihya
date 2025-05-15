# tests/ — Tests unitaires métriques (Dihya Coding)

Ce dossier regroupe les tests unitaires pour tous les collecteurs de métriques du backend Flask Dihya Coding.

## Objectif

- Vérifier la robustesse, la sécurité et la conformité RGPD/OWASP des modules de collecte et d’exposition des métriques (performance, usage, sécurité, etc.).
- Garantir la non-régression et la fiabilité du monitoring applicatif.
- Faciliter l’audit, la maintenance et l’évolution des collecteurs de métriques.

## Bonnes pratiques

- Un fichier de test par type de métrique (`test_performance_metrics.py`, `test_usage_metrics.py`, etc.).
- Couvrir tous les cas d’usage, y compris les erreurs, pics, accès non autorisés, etc.
- Ne jamais stocker ou logguer de secrets réels ou de données personnelles dans les tests.
- Utiliser des mocks ou des fixtures pour isoler les dépendances externes.
- Documenter chaque test avec une docstring claire.
- Exécuter les tests automatiquement en CI/CD.

## Exemple de structure

- `test_performance_metrics.py` : tests pour la collecte des temps de réponse, taux d’erreur, etc.
- `test_usage_metrics.py` : tests pour la collecte des appels API, utilisateurs actifs, etc.
- `test_security_metrics.py` : tests pour la collecte des accès refusés, alertes sécurité, etc.

## Exemple d’exécution

```bash
pytest .