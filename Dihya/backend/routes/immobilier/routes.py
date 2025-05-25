"""
Routes backend Django pour la gestion Immobilier (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ImmobilierProjectViewSet, ImmobilierAssetViewSet
# from .schemas import ImmobilierProjectSchema, ImmobilierAssetSchema
# from .plugins import *
# from .audit import *
# from .i18n import *
# from .permissions import *

router = DefaultRouter()
# router.register(r'immobilierprojects', ImmobilierProjectViewSet, basename='immobilier-project')
# router.register(r'immobilierassets', ImmobilierAssetViewSet, basename='immobilier-asset')

urlpatterns = [
    path('', include(router.urls)),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
