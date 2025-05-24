# Backend Python (Flask) – Onboarding utilisateur sécurisé, multilingue, RGPD, audit, fallback
from flask import Flask, request, jsonify
import logging, os
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/api/onboarding/', methods=['POST'])
def onboarding():
    data = request.json or {}
    email = data.get('email')
    lang = data.get('lang', 'fr')
    if not email:
        return jsonify({'error': 'Email requis', 'lang': lang}), 400
    # RGPD: log anonymisé
    logging.info(f"[ONBOARDING] {datetime.utcnow()} - {email[:2]}***@*** - {lang}")
    # Fallback IA open source simulé
    if os.environ.get('FALLBACK_IA', '0') == '1':
        return jsonify({'message': 'Réponse fallback IA', 'lang': lang, 'fallback': True})
    return jsonify({'message': f'Bienvenue {email}!', 'lang': lang, 'fallback': False})

if __name__ == '__main__':
    app.run(port=8001)
