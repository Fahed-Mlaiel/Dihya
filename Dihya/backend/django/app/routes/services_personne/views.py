"""
Dihya – Views avancées pour le module Services à la Personne
- Sécurité, accessibilité, multilingue, RGPD, audit, documentation
"""
from rest_framework import viewsets, permissions
from .models import Beneficiaire, Intervenant, Prestation
from .serializers import BeneficiaireSerializer, IntervenantSerializer, PrestationSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Beneficiaire.objects.all()
    serializer_class = BeneficiaireSerializer
    permission_classes = [permissions.IsAuthenticated]

class IntervenantViewSet(viewsets.ModelViewSet):
    queryset = Intervenant.objects.all()
    serializer_class = IntervenantSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrestationViewSet(viewsets.ModelViewSet):
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer
    permission_classes = [permissions.IsAuthenticated]

# TODO: Ajouter PlanningViewSet, ReservationViewSet, FactureViewSet, AvisViewSet, IAServicesViewSet, NotificationViewSet, RapportViewSet, AuditLogViewSet
