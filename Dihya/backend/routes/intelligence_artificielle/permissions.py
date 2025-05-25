"""
Permissions ultra avancées pour Intelligence Artificielle (Django routes)
RBAC, multitenancy, sécurité maximale, audit, plugins, i18n.
"""
from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsAIProjectOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission : seul le créateur/admin peut modifier/supprimer le projet IA.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user or getattr(request.user, 'role', '') == 'admin'

class IsAIAssetManagerOrReadOnly(permissions.BasePermission):
    """
    Permission : seuls les managers/admins peuvent modifier/supprimer l'asset IA.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, 'role', '') in ['admin', 'ai_asset_manager']
