"""
Models ultra avancés pour Intelligence Artificielle (Django routes)
Souverain, multilingue, RGPD, audit, plugins, multitenancy, sécurité maximale.
"""
from django.db import models
from django.conf import settings

class AIProject(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    lang = models.CharField(max_length=16, default='fr')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'AI Project'
        verbose_name_plural = 'AI Projects'
        permissions = [
            ("export_aiproject", "Can export AI project data (RGPD)")
        ]

    def __str__(self):
        return f"{self.name} ({self.lang})"

class AIAsset(models.Model):
    project = models.ForeignKey(AIProject, on_delete=models.CASCADE, related_name='assets')
    file = models.FileField(upload_to='ai/assets/')
    type = models.CharField(max_length=64)
    lang = models.CharField(max_length=16, default='fr')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'AI Asset'
        verbose_name_plural = 'AI Assets'
        permissions = [
            ("export_aiasset", "Can export AI asset data (RGPD)")
        ]

    def __str__(self):
        return f"{self.file.name} ({self.type})"
