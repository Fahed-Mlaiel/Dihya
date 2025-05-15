# monitoring/ — Monitoring & Alerting Backend Dihya Coding

Ce dossier regroupe les modules pour la surveillance de l’état du backend (healthcheck, alerting, etc.).

## Objectif

- Vérifier la disponibilité et l’intégrité des services critiques (base de données, API, stockage…).
- Détecter et alerter en cas d’incident ou d’indisponibilité.
- Centraliser la logique de monitoring pour audit et maintenance.

## Bonnes pratiques

- Ne jamais exposer d’informations sensibles dans les réponses de healthcheck ou les alertes.
- Logger chaque incident ou healthcheck KO avec horodatage.
- Prévoir plusieurs canaux d’alerte (logs, email, webhook).
- Tester régulièrement le bon fonctionnement des alertes et des checks.
- Restreindre l’accès aux endpoints de monitoring en production.

## Contenu

- **healthcheck.py** : Vérification de l’état des services critiques.
- **alerting.py** : Envoi d’alertes en cas d’incident (logs, email, webhook).

## Exemple d’utilisation

```python
from monitoring.healthcheck import check_all_services
status = check_all_services()

from monitoring.alerting import send_alert
send_alert("Erreur critique détectée", level="CRITICAL")