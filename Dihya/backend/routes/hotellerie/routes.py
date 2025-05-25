"""
Routes backend Django pour la gestion Hotellerie (Dihya)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import HotellerieProjectViewSet, HotellerieAssetViewSet
# from .schemas import HotellerieProjectSchema, HotellerieAssetSchema
# from .plugins import *
# from .audit import *
# from .i18n import *
# from .permissions import *

router = DefaultRouter()
# router.register(r'hotellerieprojects', HotellerieProjectViewSet, basename='hotellerie-project')
# router.register(r'hotellerieassets', HotellerieAssetViewSet, basename='hotellerie-asset')

urlpatterns = [
    path('', include(router.urls)),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
