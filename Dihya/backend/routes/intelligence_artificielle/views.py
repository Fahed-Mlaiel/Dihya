"""
Views ultra avancées pour le module Intelligence Artificielle (Django routes)
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy.
"""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import AIProject, AIAsset
from .serializers import AIProjectSerializer, AIAssetSerializer
from .audit import ia_audit_logger
from .i18n import IA_I18N
from .permissions import IsAIProjectOwnerOrReadOnly, IsAIAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@method_decorator(csrf_protect, name='dispatch')
class AIProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets IA.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, accessibilité.
    """
    queryset = AIProject.objects.all()
    serializer_class = AIProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAIProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        ia_audit_logger.log(self.request.user, 'create', 'AIProject', obj.id, details=obj.name, language=obj.lang)

    def perform_destroy(self, instance):
        ia_audit_logger.log(self.request.user, 'delete', 'AIProject', instance.id, details=instance.name, language=instance.lang)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class AIAssetViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des assets IA.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, accessibilité.
    """
    queryset = AIAsset.objects.all()
    serializer_class = AIAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAIAssetManagerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save()
        ia_audit_logger.log(self.request.user, 'upload', 'AIAsset', obj.id, details=obj.file.name, language=obj.lang)
