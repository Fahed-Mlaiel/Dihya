"""
Routes backend Django pour la gestion Blockchain (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlockchainProjectViewSet, BlockchainAssetViewSet
from .schemas import BlockchainProjectSchema, BlockchainAssetSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *

# RESTful API
router = DefaultRouter()
router.register(r'blockchainprojects', BlockchainProjectViewSet, basename='blockchain-blockchainproject')
router.register(r'blockchainassets', BlockchainAssetViewSet, basename='blockchain-blockchainasset')

urlpatterns = [
    path('', include(router.urls)),
    # GraphQL endpoint (à brancher sur la stack GraphQL du projet)
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
