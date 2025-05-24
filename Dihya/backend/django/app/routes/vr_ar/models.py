from django.db import models
from django.conf import settings

class Scene(models.Model):
    title = models.CharField(max_length=256, help_text="Titre de la scène VR/AR")
    description = models.TextField(help_text="Description de la scène")
    lang = models.CharField(max_length=16, default='fr', help_text="Langue de la scène")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scenes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.lang})"

class Asset(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, related_name='assets')
    file = models.FileField(upload_to='vr_ar/assets/', help_text="Fichier 3D/VR/AR")
    type = models.CharField(max_length=32, help_text="Type d’asset (3D, audio, vidéo, etc.)")
    lang = models.CharField(max_length=16, default='fr', help_text="Langue de l’asset")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file} ({self.type})"
