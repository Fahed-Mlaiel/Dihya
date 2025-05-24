"""
Fichier d'initialisation du module Django routes/vr_ar
Expose toutes les fonctionnalités REST, GraphQL, plugins, sécurité, i18n, audit, RGPD, multitenancy, etc.
Ultra avancé, production-ready, multilingue, souverain, extensible, sécurisé.
"""
from .routes import urlpatterns
from .views import SceneViewSet, AssetViewSet
from .schemas import SceneSchema, AssetSchema, SceneListSchema, AssetListSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *
from .models import *
from .serializers import *
from .templates import *

__all__ = [
    'SceneViewSet', 'AssetViewSet', 'urlpatterns',
    'SceneSchema', 'AssetSchema', 'SceneListSchema', 'AssetListSchema',
    'plugins', 'audit', 'i18n', 'permissions', 'models', 'serializers', 'templates'
]
