"""
Initialisation des blueprints de routes pour l'application Dihya Coding.
Chaque module de routes (main, auth, user, etc.) est importé ici pour
être enregistré dans l'application principale.
"""

from flask import Blueprint

# Blueprint principal (routes publiques, healthcheck, accueil, info, echo, SEO)
main = Blueprint('main', __name__)

# Blueprint Auth (authentification, inscription, refresh, logout)
auth = Blueprint('auth', __name__)

# Blueprint User (gestion des utilisateurs, rôles, profil, CRUD)
user = Blueprint('user', __name__)

# À compléter si de nouveaux modules de routes sont ajoutés (ex: admin, plugins, etc.)

# Les fichiers main.py, auth.py, user.py doivent définir les routes
# et attacher les fonctions à ces blueprints respectifs.
# Chaque blueprint doit être importé dans app/__init__.py pour l'enregistrement.