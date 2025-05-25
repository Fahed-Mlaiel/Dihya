"""
Fichier d'initialisation du module Django routes/intelligence_artificielle
Expose toutes les fonctionnalités REST, GraphQL, plugins, sécurité, i18n, audit, RGPD, multitenancy, etc.
Ultra avancé, production-ready, multilingue, souverain, extensible, sécurisé.
"""
from .routes import urlpatterns
from .views import AIProjectViewSet, AIAssetViewSet
from .schemas import AIProjectSchema, AIAssetSchema, AIProjectListSchema, AIAssetListSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *
from .models import *
from .serializers import *
from .templates import *

__all__ = [
    'AIProjectViewSet', 'AIAssetViewSet', 'urlpatterns',
    'AIProjectSchema', 'AIAssetSchema', 'AIProjectListSchema', 'AIAssetListSchema',
    'plugins', 'audit', 'i18n', 'permissions', 'models', 'serializers', 'templates'
]
