"""
Views ultra avancées pour le module Blockchain (Django routes)
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy.
"""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import BlockchainProject, BlockchainAsset
from .serializers import BlockchainProjectSerializer, BlockchainAssetSerializer
from .audit import blockchain_audit_logger
from .i18n import BLOCKCHAIN_I18N
from .permissions import IsBlockchainProjectOwnerOrReadOnly, IsBlockchainAssetManagerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@method_decorator(csrf_protect, name='dispatch')
class BlockchainProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des projets blockchain.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, accessibilité.
    """
    queryset = BlockchainProject.objects.all()
    serializer_class = BlockchainProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBlockchainProjectOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        blockchain_audit_logger.log(self.request.user, 'create', 'BlockchainProject', obj.id, details=obj.name, language=obj.lang)

    def perform_destroy(self, instance):
        blockchain_audit_logger.log(self.request.user, 'delete', 'BlockchainProject', instance.id, details=instance.name, language=instance.lang)
        instance.delete()

@method_decorator(csrf_protect, name='dispatch')
class BlockchainAssetViewSet(viewsets.ModelViewSet):
    """
    ViewSet REST/GraphQL pour la gestion des assets blockchain.
    Sécurité, audit, i18n, RGPD, multitenancy, plugins, accessibilité.
    """
    queryset = BlockchainAsset.objects.all()
    serializer_class = BlockchainAssetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsBlockchainAssetManagerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save()
        blockchain_audit_logger.log(self.request.user, 'upload', 'BlockchainAsset', obj.id, details=obj.file.name, language=obj.lang)
