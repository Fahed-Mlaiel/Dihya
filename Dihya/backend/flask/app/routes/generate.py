"""
Route API pour la génération automatique de projets (Dihya Coding).

Cette route permet de générer un projet numérique complet (frontend, backend, mobile, etc.)
à partir d’un cahier des charges fourni en texte ou en vocal, en s’appuyant sur l’IA et les modules internes.

Bonnes pratiques :
- Authentifier chaque requête (JWT obligatoire).
- Valider et filtrer le cahier des charges (anti-injection, taille max, etc.).
- Logger chaque génération avec horodatage, utilisateur, type de projet et statut.
- Ne jamais inclure de secrets ou de code sensible dans la réponse.
- Prévoir un fallback IA open source si quota GPT/Cloud dépassé.
- Retourner un lien de prévisualisation ou de téléchargement sécurisé.

Exemple d’utilisation :
    POST /api/generate
    {
        "spec": "Je veux une app de gestion de tâches multilingue...",
        "type": "webapp",
        "stack": "react+flask"
    }
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.validators import validate_generate_payload
from app.utils.security import sanitize_input
from app.ai_fallback.quotas import check_quota, use_fallback_ai
import logging
from datetime import datetime

generate_bp = Blueprint("generate", __name__, url_prefix="/api/generate")

@generate_bp.route("", methods=["POST"])
@jwt_required()
def generate_project():
    """
    Génère un projet à partir d’un cahier des charges fourni par l’utilisateur authentifié.
    """
    user = get_jwt_identity()
    payload = request.get_json()
    if not payload or not validate_generate_payload(payload):
        return jsonify({"success": False, "error": "Spécification invalide."}), 400

    spec = sanitize_input(payload.get("spec", ""))
    project_type = payload.get("type", "webapp")
    stack = payload.get("stack", "react+flask")

    # Vérification quota IA propriétaire
    if not check_quota(user):
        # Fallback IA open source
        code, preview_url = use_fallback_ai(spec, project_type, stack)
        status = "FALLBACK"
    else:
        # Appel à l’IA principale (ex: GPT-4o, API interne)
        # TODO: Intégrer la génération réelle via IA propriétaire
        code, preview_url = "// code généré", "https://preview.dihya.dev/demo123"
        status = "SUCCESS"

    # Log de la génération
    logging.info(f"{datetime.utcnow().isoformat()} | user={user} | type={project_type} | stack={stack} | status={status}")

    return jsonify({
        "success": True,
        "status": status,
        "code": code,
        "preview_url": preview_url
    }), 200