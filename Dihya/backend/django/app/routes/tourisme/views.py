"""
Dihya – Views avancées pour le module Tourisme
- Sécurité, accessibilité, multilingue, RGPD, audit, documentation
"""
from rest_framework import viewsets, permissions
from .models import Destination, Offre, Reservation, Avis
from .serializers import DestinationSerializer, OffreSerializer, ReservationSerializer, AvisSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticated]

class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer
    permission_classes = [permissions.IsAuthenticated]

# TODO: Ajouter GuideViewSet, EvenementViewSet, PartenairesViewSet, IATourismeViewSet, NotificationViewSet, RapportViewSet, LogTourismeViewSet, AuditLogViewSet
