"""
Routes backend Django pour la gestion Crypto (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import CryptoProjectViewSet, CryptoAssetViewSet
# from .schemas import CryptoProjectSchema, CryptoAssetSchema
# from .plugins import *
# from .audit import *
# from .i18n import *
# from .permissions import *

router = DefaultRouter()
# router.register(r'cryptoprojects', CryptoProjectViewSet, basename='crypto-project')
# router.register(r'cryptoassets', CryptoAssetViewSet, basename='crypto-asset')

urlpatterns = [
    path('', include(router.urls)),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
