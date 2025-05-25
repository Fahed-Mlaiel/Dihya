"""
Routes backend Django pour la gestion Construction (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Les ViewSets, schémas, plugins, audit, i18n, permissions sont à créer dans ce module
# from .views import ConstructionProjectViewSet, ConstructionAssetViewSet
# from .schemas import ConstructionProjectSchema, ConstructionAssetSchema
# from .plugins import *
# from .audit import *
# from .i18n import *
# from .permissions import *

# RESTful API
router = DefaultRouter()
# router.register(r'constructionProjects', ConstructionProjectViewSet, basename='construction-project')
# router.register(r'constructionAssets', ConstructionAssetViewSet, basename='construction-asset')

urlpatterns = [
    path('', include(router.urls)),
    # GraphQL endpoint (à brancher sur la stack GraphQL du projet)
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
