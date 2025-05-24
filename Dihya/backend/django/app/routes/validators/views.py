"""
Dihya – Views pour Validators
- Pour logs, schémas, validations, etc.
"""
from rest_framework import viewsets, permissions
from .models import ValidationLog
from .serializers import ValidationLogSerializer

class LogValidatorViewSet(viewsets.ModelViewSet):
    queryset = ValidationLog.objects.all()
    serializer_class = ValidationLogSerializer
    permission_classes = [permissions.IsAuthenticated]

# TODO: Ajouter EmailValidatorViewSet, FileValidatorViewSet, SchemaValidatorViewSet, IdentiteValidatorViewSet, IBANValidatorViewSet, SIRETValidatorViewSet, FluxValidatorViewSet, UploadValidatorViewSet, IAValidatorViewSet, RapportViewSet, AuditLogViewSet
