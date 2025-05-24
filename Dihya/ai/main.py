"""
Dihya AI – Point d'entrée module IA (Python)
Ultra avancé, multilingue, souverain, extensible, sécurisé.
Expose toutes les fonctions et configurations IA pour usage multi-stack (Flask, FastAPI, CLI, etc.).
Prêt pour la production, la démo, la contribution.

@author: Dihya Team
"""

from ai import generate_ai_response, select_engine, SUPPORTED_LANGUAGES, DihyaAIConfig

# Exemple d'intégration Flask (API REST)
def create_flask_ai_blueprint():
    from flask import Blueprint, request, jsonify

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

    return ai_bp

# Exemple d'utilisation CLI
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Dihya AI CLI – Génération IA souveraine, multilingue")
    parser.add_argument('--prompt', type=str, required=True, help="Prompt utilisateur")
    parser.add_argument('--user_id', type=str, default="cli-user", help="ID utilisateur")
    parser.add_argument('--lang', type=str, choices=SUPPORTED_LANGUAGES, help="Langue cible")
    parser.add_argument('--role', type=str, default="admin", help="Rôle utilisateur")
    parser.add_argument('--engine', type=str, choices=['openai', 'mixtral', 'llama', 'mistral'], help="Moteur IA préféré")
    args = parser.parse_args()

    try:
        result = generate_ai_response(
            prompt=args.prompt,
            user_id=args.user_id,
            lang=args.lang,
            role=args.role,
            engine=args.engine
        )
        print(f"[{result['engine']}] ({result['lang']}) {result['text']}")
    except Exception as e:
        print(f"Erreur IA: {e}")

# main.py – Entrée du module IA Dihya

if __name__ == "__main__":
    print("Dihya AI module – NLP, ML, fallback open source, multilingue, sécurité, audit.")
    # ...lancer les tests, les scripts, l’audit, etc.
    main()
