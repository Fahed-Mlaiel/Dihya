"""
Dihya – Views avancées pour le module Voice
- Sécurité, accessibilité, multilingue, RGPD, audit, documentation
"""
from rest_framework import viewsets, permissions
from .models import AudioFile, Transcription
from .serializers import AudioFileSerializer, TranscriptionSerializer

class AudioFileViewSet(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer
    permission_classes = [permissions.IsAuthenticated]

class TranscriptionViewSet(viewsets.ModelViewSet):
    queryset = Transcription.objects.all()
    serializer_class = TranscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

# TODO: Ajouter TTSViewSet, ASRViewSet, AnalyseAudioViewSet, TraductionAudioViewSet, ModerationAudioViewSet, IAVoiceViewSet, NotificationViewSet, RapportViewSet, AuditLogViewSet
