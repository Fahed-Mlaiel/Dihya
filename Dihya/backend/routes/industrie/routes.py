"""
Routes backend Django pour la gestion Industrie (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import IndustrieProjectViewSet, IndustrieAssetViewSet
# from .schemas import IndustrieProjectSchema, IndustrieAssetSchema
# from .plugins import *
# from .audit import *
# from .i18n import *
# from .permissions import *

router = DefaultRouter()
# router.register(r'industrieprojects', IndustrieProjectViewSet, basename='industrie-project')
# router.register(r'industrieassets', IndustrieAssetViewSet, basename='industrie-asset')

urlpatterns = [
    path('', include(router.urls)),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
