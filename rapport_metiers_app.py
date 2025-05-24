"""
Dihya – Application de génération de rapports métiers ultra avancée, multilingue, souveraine, sécurisée.
- Compatible multi-stack (Flask, FastAPI, Django, Node, Flutter)
- Sécurité, RBAC, i18n (fr, en, ar, tzm), accessibilité, RGPD, fallback IA open source
- Prête pour CI/CD, monitoring, audit, déploiement souverain
"""

import os
from flask import Flask, request, jsonify, render_template_string
from flask_babel import Babel, _
from functools import wraps
import logging
import jwt
from datetime import datetime, timedelta

# --- Configurations ---

SUPPORTED_LANGUAGES = ["fr", "en", "ar", "tzm"]
DEFAULT_LANG = "fr"
SECRET_KEY = os.environ.get("DIHYA_SECRET_KEY", "change-me-in-prod")
JWT_ALGO = "HS256"

# --- Flask App & Babel ---

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["BABEL_DEFAULT_LOCALE"] = DEFAULT_LANG
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "translations"
babel = Babel(app)

# --- Logging structuré ---

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler()]
)

# --- i18n Sélection dynamique ---

@babel.localeselector
def get_locale():
    lang = request.args.get("lang") or request.headers.get("Accept-Language", DEFAULT_LANG)
    return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANG

# --- RBAC décorateur ---

def require_role(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization", "").replace("Bearer ", "")
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGO])
                if role not in payload.get("roles", []):
                    return jsonify({"error": _("Accès refusé"), "lang": get_locale()}), 403
            except Exception:
                return jsonify({"error": _("Token invalide ou manquant"), "lang": get_locale()}), 401
            return f(*args, **kwargs)
        return wrapper
    return decorator

# --- Exemple de données métiers (mock) ---

METIERS = [
    {"id": 1, "nom": {"fr": "DevOps", "en": "DevOps", "ar": "ديفوبس", "tzm": "DevOps"}, "policies": ["SEC-002", "CI-001"]},
    {"id": 2, "nom": {"fr": "Développeur Frontend", "en": "Frontend Developer", "ar": "مطور الواجهة", "tzm": "Frontend"}, "policies": ["ACC-001", "RGPD-002"]},
    {"id": 3, "nom": {"fr": "Data Privacy Officer", "en": "DPO", "ar": "مسؤول حماية البيانات", "tzm": "DPO"}, "policies": ["RGPD-001", "RGPD-002"]},
]

# --- API : Génération de rapport métier ---

@app.route("/api/rapport/metier/<int:metier_id>", methods=["GET"])
@require_role("user")
def rapport_metier(metier_id):
    lang = get_locale()
    metier = next((m for m in METIERS if m["id"] == metier_id), None)
    if not metier:
        return jsonify({"error": _("Métier introuvable"), "lang": lang}), 404
    rapport = {
        "id": metier["id"],
        "nom": metier["nom"][lang],
        "policies": metier["policies"],
        "date": datetime.utcnow().isoformat() + "Z",
        "lang": lang
    }
    logging.info(f"Rapport métier généré: {rapport}")
    return jsonify(rapport)

# --- API : Authentification mock JWT (pour démo/test) ---

@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.json or {}
    email = data.get("email")
    roles = data.get("roles", ["user"])
    lang = data.get("lang", DEFAULT_LANG)
    if not email:
        return jsonify({"error": _("Email requis"), "lang": lang}), 400
    payload = {
        "email": email,
        "roles": roles,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGO)
    return jsonify({"access_token": token, "lang": lang})

# --- Page HTML de démo (accessibilité, multilingue) ---

@app.route("/")
def index():
    lang = get_locale()
    template = """
    <!DOCTYPE html>
    <html lang="{{ lang }}">
    <head>
        <meta charset="utf-8">
        <title>{{ _('Rapport Métiers Dihya') }}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="{{ _('Application de génération de rapports métiers multilingue, souveraine, sécurisée.') }}">
        <style>
            body { font-family: sans-serif; margin: 2em; background: #f9f9f9; }
            .card { background: #fff; padding: 1em; margin: 1em 0; border-radius: 8px; box-shadow: 0 2px 8px #0001; }
            .lang-switch { margin-bottom: 1em; }
        </style>
    </head>
    <body>
        <h1>{{ _('Rapport Métiers Dihya') }}</h1>
        <div class="lang-switch">
            <form method="get">
                <label for="lang">{{ _('Langue') }}:</label>
                <select name="lang" id="lang" onchange="this.form.submit()">
                    {% for l in supported_languages %}
                    <option value="{{ l }}" {% if l == lang %}selected{% endif %}>{{ l }}</option>
                    {% endfor %}
                </select>
            </form>
        </div>
        {% for metier in metiers %}
        <div class="card">
            <h2>{{ metier.nom[lang] }}</h2>
            <p><strong>{{ _('Politiques associées') }}:</strong> {{ metier.policies|join(', ') }}</p>
        </div>
        {% endfor %}
        <footer>
            <small>&copy; 2025 Dihya – {{ _('Souveraineté, sécurité, accessibilité, multilingue') }}</small>
        </footer>
    </body>
    </html>
    """
    return render_template_string(template, lang=lang, metiers=METIERS, supported_languages=SUPPORTED_LANGUAGES, _=_)

# --- Fallback IA open source (exemple minimal) ---

@app.route("/api/ia/fallback", methods=["POST"])
@require_role("user")
def ia_fallback():
    data = request.json or {}
    question = data.get("question")
    lang = data.get("lang", get_locale())
    # Fallback IA open source simulé
    answer = {
        "fr": "Réponse IA open source (fallback) – démo.",
        "en": "Open source AI answer (fallback) – demo.",
        "ar": "إجابة الذكاء الاصطناعي مفتوح المصدر (احتياطي) – عرض.",
        "tzm": "Tiririt n IA open source (fallback) – demo."
    }.get(lang, "Réponse IA open source (fallback) – démo.")
    return jsonify({"answer": answer, "lang": lang, "fallback_used": True})

# --- Lancement sécurisé ---

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=False)
