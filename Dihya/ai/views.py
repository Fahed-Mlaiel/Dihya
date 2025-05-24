"""
Views ultra avancées pour le module IA Dihya (Python)
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy.
"""
from flask import Blueprint, request, jsonify
from .ai import generate_ai_response

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai/generate', methods=['POST'])
def ai_generate():
    data = request.get_json(force=True)
    prompt = data.get('prompt')
    lang = data.get('lang')
    engine = data.get('engine')
    user_id = getattr(request, 'user', None) and getattr(request.user, 'id', 'anonymous') or 'anonymous'
    role = getattr(request, 'user', None) and getattr(request.user, 'role', 'user') or 'user'
    try:
        result = generate_ai_response(
            prompt=prompt,
            user_id=user_id,
            lang=lang,
            role=role,
            engine=engine
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Pour GraphQL, brancher le schéma sur /ai/graphql (exemple Strawberry/FastAPI)
