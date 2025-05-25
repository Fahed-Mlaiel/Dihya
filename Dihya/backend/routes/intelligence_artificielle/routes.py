"""
Routes backend Django pour la gestion Intelligence Artificielle (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AIProjectViewSet, AIAssetViewSet
from .schemas import AIProjectSchema, AIAssetSchema
from .plugins import *
from .audit import *
from .i18n import *
from .permissions import *

# RESTful API
router = DefaultRouter()
router.register(r'aiprojects', AIProjectViewSet, basename='intelligenceartificielle-aiproject')
router.register(r'aiassets', AIAssetViewSet, basename='intelligenceartificielle-aiasset')

urlpatterns = [
    path('', include(router.urls)),
    # GraphQL endpoint (à brancher sur la stack GraphQL du projet)
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
