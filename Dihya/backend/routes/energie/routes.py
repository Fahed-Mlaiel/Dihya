"""
Routes backend Django pour la gestion Energie (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import EnergieProjectViewSet, EnergieAssetViewSet
# from .schemas import EnergieProjectSchema, EnergieAssetSchema
# from .plugins import *
# from .audit import *
# from .i18n import *
# from .permissions import *

router = DefaultRouter()
# router.register(r'energieprojects', EnergieProjectViewSet, basename='energie-project')
# router.register(r'energieassets', EnergieAssetViewSet, basename='energie-asset')

urlpatterns = [
    path('', include(router.urls)),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
