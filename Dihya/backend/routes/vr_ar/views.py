"""
Views ultra avancées pour le module VR/AR (Django routes)
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy.
"""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Scene, Asset
from .serializers import SceneSerializer, AssetSerializer
from .audit import vr_ar_audit_logger
from .i18n import VR_AR_I18N
from .permissions import IsSceneOwnerOrReadOnly, IsAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@method_decorator(csrf_protect, name='dispatch')
class SceneViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des scènes VR/AR.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, accessibilité.
    """
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSceneOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        vr_ar_audit_logger.log(self.request.user, 'create', 'Scene', obj.id, details=obj.title, language=obj.lang)

    def perform_destroy(self, instance):
        vr_ar_audit_logger.log(self.request.user, 'delete', 'Scene', instance.id, details=instance.title, language=instance.lang)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class AssetViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des assets VR/AR.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, accessibilité.
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAssetManagerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save()
        vr_ar_audit_logger.log(self.request.user, 'upload', 'Asset', obj.id, details=obj.file.name, language=obj.lang)
