"""
Dihya – Views utilitaires pour API Utils
- Pour logs, conversions, monitoring, etc.
"""
from rest_framework import viewsets, permissions
from .models import LogEntry
from .serializers import LogEntrySerializer

class LogUtilsViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

# TODO: Ajouter UUIDViewSet, ConversionViewSet, ValidateEmailViewSet, MonitoringViewSet, IAUtilsViewSet, NotificationViewSet, RapportViewSet, AuditLogViewSet, BackupViewSet, RestoreViewSet, MigrationViewSet
