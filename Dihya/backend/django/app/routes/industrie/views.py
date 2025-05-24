"""
Views Industrie (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import SiteIndustriel
from .serializers import SiteIndustrielSerializer
from .permissions import IsResponsable

class SiteIndustrielViewSet(viewsets.ModelViewSet):
    queryset = SiteIndustriel.objects.all()
    serializer_class = SiteIndustrielSerializer
    permission_classes = [IsResponsable]
