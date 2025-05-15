# integrations/ — Webhooks & APIs externes (Dihya Coding)

Ce dossier centralise les modules et scripts permettant d’intégrer le backend Dihya Coding à des services tiers (paiement, analytics, CMS, mailing, etc.) et de gérer les webhooks entrants ou sortants.

## Objectif

- Faciliter l’intégration de services externes de façon sécurisée et modulaire.
- Centraliser la gestion des webhooks pour audit, traçabilité et maintenance.

## Bonnes pratiques

- Documenter chaque intégration (API, endpoints, sécurité, quotas, dépendances).
- Valider et sécuriser chaque payload reçu ou envoyé (signature, schéma, etc.).
- Utiliser les variables d’environnement pour tous les secrets et tokens.
- Logger les événements importants pour audit et traçabilité.
- Prévoir des tests unitaires pour chaque intégration critique.
- Ne jamais exposer de secrets ou de tokens dans le code ou les logs.

## Exemple d’utilisation

```python
from integrations import send_webhook, handle_incoming_webhook

# Envoi d’un webhook
send_webhook("https://api.exemple.com/webhook", {"event": "test"})

# Gestion d’un webhook entrant (dans une route Flask)
@app.route("/webhook", methods=["POST"])
def webhook():
    return handle_incoming_webhook(request)