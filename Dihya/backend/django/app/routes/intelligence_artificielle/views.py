"""
Views Intelligence Artificielle (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import ModeleIA
from .serializers import ModeleIASerializer
from .permissions import IsProprietaire

class ModeleIAViewSet(viewsets.ModelViewSet):
    queryset = ModeleIA.objects.all()
    serializer_class = ModeleIASerializer
    permission_classes = [IsProprietaire]
