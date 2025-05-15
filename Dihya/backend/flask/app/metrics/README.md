# metrics/ — Gestion des métriques applicatives (Dihya Coding)

Ce dossier centralise la déclaration, la collecte et l’exposition des métriques personnalisées pour le backend Flask Dihya Coding.

## Objectif

- Permettre le suivi de la performance, de l’usage, de la sécurité et de la santé applicative.
- Faciliter l’intégration avec des outils de monitoring (Prometheus, Grafana, etc.).
- Garantir la conformité, la sécurité et la confidentialité des données exposées.

## Bonnes pratiques

- Déclarer chaque type de métrique dans un fichier dédié (`performance_metrics.py`, `usage_metrics.py`, `security_metrics.py`, etc.).
- Documenter chaque métrique (but, unité, fréquence de collecte, sécurité).
- Protéger l’accès aux endpoints d’exposition des métriques (authentification, IP whitelist, etc.).
- Ne jamais exposer de données sensibles ou personnelles dans les métriques.
- Prévoir des tests unitaires pour chaque collecteur de métriques.
- Logger les anomalies ou pics inhabituels pour audit et amélioration continue.

## Exemple de structure

- `performance_metrics.py` : suivi des temps de réponse, latence, etc.
- `usage_metrics.py` : suivi du nombre d’appels API, utilisateurs actifs, etc.
- `security_metrics.py` : suivi des tentatives d’accès refusées, alertes sécurité, etc.

## Exemple d’utilisation

```python
from app.metrics.performance_metrics import record_response_time
from app.metrics.usage_metrics import increment_api_call_count

record_response_time("/api/generate", 120)
increment_api_call_count("user_123")