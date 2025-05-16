"""
Webhooks CRM pour Dihya Coding.

Ce module gère la réception et le traitement sécurisé des webhooks provenant de systèmes CRM externes (Salesforce, HubSpot, etc.).
Il valide les payloads, vérifie la signature, déclenche les actions backend appropriées et loggue chaque événement pour audit.

Bonnes pratiques :
- Validation stricte du payload (schéma, champs obligatoires)
- Vérification de la signature/secrète du webhook (anti-spoofing)
- Logger chaque réception et traitement (horodatage, statut, source)
- Ne jamais exposer de données sensibles dans les logs ou erreurs
- Protéger toutes les routes par JWT ou clé secrète dédiée
"""

from flask import Blueprint, request, jsonify, current_app
from datetime import datetime
import hmac
import hashlib

bp = Blueprint("crm_webhooks", __name__, url_prefix="/api/integrations/webhooks/crm")

# Exemple de clé secrète (à stocker dans la config sécurisée)
CRM_WEBHOOK_SECRET = "change_me_in_prod"

def validate_payload(data):
    """
    Valide le schéma du payload CRM attendu.
    """
    if not isinstance(data, dict):
        raise ValueError("Payload CRM invalide (dict attendu)")
    if "event_type" not in data or not isinstance(data["event_type"], str):
        raise ValueError("Champ 'event_type' manquant ou invalide")
    if "data" not in data or not isinstance(data["data"], dict):
        raise ValueError("Champ 'data' manquant ou invalide")
    return True

def verify_signature(request):
    """
    Vérifie la signature HMAC du webhook CRM.
    """
    signature = request.headers.get("X-CRM-Signature")
    if not signature:
        return False
    body = request.get_data()
    expected = hmac.new(
        CRM_WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected)

def log_webhook(event_type, status, source, error=None):
    msg = f"[{datetime.utcnow().isoformat()}] [CRM_WEBHOOK] event={event_type} status={status} source={source}"
    if error:
        msg += f" error={error}"
    print(msg)

@bp.route("/", methods=["POST"])
def receive_crm_webhook():
    """
    Endpoint pour recevoir les webhooks CRM.
    Sécurité : signature HMAC obligatoire.
    """
    source = request.remote_addr
    try:
        if not verify_signature(request):
            log_webhook("unknown", "forbidden", source, "Signature invalide")
            return jsonify({"error": "Signature invalide"}), 403
        data = request.get_json(force=True)
        validate_payload(data)
        event_type = data["event_type"]
        # Traitement métier fictif (à adapter selon vos besoins)
        log_webhook(event_type, "received", source)
        # ... traitement du payload ...
        log_webhook(event_type, "processed", source)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log_webhook("unknown", "error", source, str(e))
        return jsonify({"error": str(e)}), 400

# À intégrer dans votre app Flask principale :
# from app.integrations.webhooks.crm_webhooks import bp as crm_webhooks_bp
# app.register_blueprint(crm_webhooks_bp)