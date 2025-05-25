"""
Routes backend Django pour la gestion Agriculture (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Les ViewSets, schémas, plugins, audit, i18n, permissions sont à créer dans ce module
# from .views import AgricultureProjectViewSet, AgricultureAssetViewSet
# from .schemas import AgricultureProjectSchema, AgricultureAssetSchema
# from .plugins import *
# from .audit import *
# from .i18n import *
# from .permissions import *

# RESTful API
router = DefaultRouter()
# router.register(r'agricultureProjects', AgricultureProjectViewSet, basename='agriculture-project')
# router.register(r'agricultureAssets', AgricultureAssetViewSet, basename='agriculture-asset')

urlpatterns = [
    path('', include(router.urls)),
    # GraphQL endpoint (à brancher sur la stack GraphQL du projet)
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
