"""
Initialisation du module IA Dihya (Python)
Ultra avancé, multilingue, souverain, extensible, sécurisé, production-ready.
Expose toutes les fonctionnalités IA (REST, GraphQL, plugins, sécurité, i18n, audit, RGPD, multitenancy, etc.).
"""
from .ai import generate_ai_response, select_engine, SUPPORTED_LANGUAGES, DihyaAIConfig
from .views import ai_bp
from .schemas import AIRequestSchema, AIResponseSchema
from .plugins import *
from .audit import *
from .i18n import *

__all__ = [
    'generate_ai_response', 'select_engine', 'SUPPORTED_LANGUAGES', 'DihyaAIConfig',
    'ai_bp', 'AIRequestSchema', 'AIResponseSchema', 'plugins', 'audit', 'i18n'
]
# Ce fichier rend le dossier ai importable comme module Python
