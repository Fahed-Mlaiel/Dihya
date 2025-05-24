"""
Définition des routes API IA Dihya (Flask/GraphQL-ready)
Ultra avancé, sécurisé, multilingue, REST & GraphQL, plugins, audit, RGPD, multitenancy.
"""
from .views import ai_bp

# Pour Flask :
# app.register_blueprint(ai_bp)

# Pour GraphQL :
# Brancher le schéma GraphQL sur /ai/graphql
