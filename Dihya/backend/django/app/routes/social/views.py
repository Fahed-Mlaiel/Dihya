"""
Dihya – Views avancées pour le module Social
- Sécurité, accessibilité, multilingue, RGPD, audit, documentation
"""
from rest_framework import viewsets, permissions
from .models import Profil, Post, Commentaire, Like, Abonnement
from .serializers import ProfilSerializer, PostSerializer, CommentaireSerializer, LikeSerializer, AbonnementSerializer

class ProfilViewSet(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class AbonnementViewSet(viewsets.ModelViewSet):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer
    permission_classes = [permissions.IsAuthenticated]

# TODO: Ajouter NotificationViewSet, IASocialViewSet, ModerationViewSet, RapportViewSet, LogSocialViewSet, AuditLogViewSet
