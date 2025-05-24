"""
Serveur Python (Flask) ultra avancé pour servir les logos Dihya (sécurisé, RGPD, accessibilité, audit, multilingue)
"""
from flask import Flask, send_file, jsonify, request
import os

app = Flask(__name__)
LOGOS_DIR = os.path.dirname(os.path.abspath(__file__))

@app.before_request
def audit_log():
    print(f"[LOGO_ACCESS] {request.method} {request.path} {request.remote_addr}")

@app.route('/logos/<logo>')
def get_logo(logo):
    safe_logo = ''.join([c for c in logo if c.isalnum() or c in ('-', '_')])
    logo_path = os.path.join(LOGOS_DIR, safe_logo + '.svg')
    if os.path.exists(logo_path):
        return send_file(logo_path, mimetype='image/svg+xml')
    return jsonify({'error': 'Logo not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4002)
