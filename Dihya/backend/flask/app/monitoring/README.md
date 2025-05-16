# Dossier `monitoring/` — Backend Dihya Coding

Ce dossier regroupe les modules et scripts dédiés à la supervision, au suivi de la santé et à l’audit du backend Dihya Coding.

## Bonnes pratiques Dihya Coding

- **Centralisation** : tous les outils de monitoring (healthcheck, alerting, métriques, etc.) sont regroupés ici pour une gestion claire et évolutive.
- **Sécurité** : ne jamais exposer d’informations sensibles dans les réponses ou logs de monitoring.
- **Extensibilité** : prévoir l’ajout facile de nouveaux modules (vérification DB, cache, dépendances externes, alertes…).
- **Auditabilité** : logger les checks échoués et les alertes pour permettre un audit ultérieur.
- **Interopérabilité** : concevoir les endpoints pour être compatibles avec les outils de CI/CD, load balancers, Prometheus, etc.

## Exemples de contenu

- `healthcheck.py` : expose une route `/api/health` pour vérifier la disponibilité du backend.
- `alerting.py` : gestion des alertes et notifications en cas d’incident ou d’anomalie.
- `README.md` : documentation sur l’usage et les bonnes pratiques de monitoring.

## Utilisation

Dans votre app Flask principale :

```python
from app.monitoring.healthcheck import bp as healthcheck_bp
app.register_blueprint(healthcheck_bp)
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*