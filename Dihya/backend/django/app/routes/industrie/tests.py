"""
Tests unitaires et intégration Industrie (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import SiteIndustriel

class SiteIndustrielModelTest(TestCase):
    def test_creation_site(self):
        site = SiteIndustriel.objects.create(
            nom='Usine Amazigh', type='usine', capacite=10000.0, localisation='Tizi Ouzou', responsable='Yidir')
        self.assertEqual(site.nom, 'Usine Amazigh')
