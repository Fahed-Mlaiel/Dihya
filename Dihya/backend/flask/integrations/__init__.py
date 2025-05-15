"""
Module d’intégration pour les webhooks et APIs externes dans Dihya Coding.

Ce package permet de connecter le backend à des services tiers (paiement, analytics, CMS, mailing, etc.)
et de gérer les webhooks entrants ou sortants de façon sécurisée et modulaire.

Bonnes pratiques :
- Centraliser ici toutes les intégrations externes pour faciliter la maintenance.
- Documenter chaque intégration (API, endpoints, sécurité, quotas).
- Valider et sécuriser chaque payload reçu ou envoyé (signature, validation de schéma, etc.).
- Prévoir des tests unitaires pour chaque intégration critique.
- Ne jamais exposer de secrets ou de tokens dans le code : utiliser les variables d’environnement.
- Logger les événements importants pour audit et traçabilité.

Exemple d’utilisation :
    from integrations import send_webhook, handle_incoming_webhook

"""

def send_webhook(url, payload, headers=None):
    """
    Envoie un webhook POST vers un service externe.
    :param url: URL du service externe
    :param payload: Données à envoyer (dict)
    :param headers: En-têtes HTTP optionnels
    :return: Réponse du service externe
    """
    import requests
    try:
        response = requests.post(url, json=payload, headers=headers or {})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        # À améliorer : gestion fine des erreurs et logs
        print(f"Erreur lors de l'envoi du webhook : {e}")
        return None

def handle_incoming_webhook(request):
    """
    Exemple de gestion d’un webhook entrant (à adapter selon le framework utilisé).
    :param request: Objet requête (Flask, etc.)
    :return: dict avec le statut et les données validées
    """
    # TODO: Ajouter validation de signature, schéma, etc.
    data = request.get_json()
    # Valider et traiter le payload ici
    return {"status": "received", "data": data}