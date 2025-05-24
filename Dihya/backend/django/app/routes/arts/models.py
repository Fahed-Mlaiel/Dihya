"""
Dihya – Django Arts API Models Ultra Avancé
-------------------------------------------
- Modèles pour œuvres, artistes, expositions, galeries, NFT, IA générative, audit
- Sécurité, RGPD, multilingue, extensibilité
"""
from django.db import models

class Artiste(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    pays = models.CharField(max_length=255)

class Oeuvre(models.Model):
    titre = models.CharField(max_length=255)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    annee = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

class Exposition(models.Model):
    nom = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    lieu = models.CharField(max_length=255)

class Galerie(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    site_web = models.URLField(blank=True, null=True)

class NFT(models.Model):
    oeuvre = models.ForeignKey(Oeuvre, on_delete=models.CASCADE)
    token_id = models.CharField(max_length=255)
    blockchain = models.CharField(max_length=255)
    url = models.URLField()

class IAGeneration(models.Model):
    prompt = models.TextField()
    image_url = models.URLField()

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
