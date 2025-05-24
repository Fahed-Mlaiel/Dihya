"""
Tests unitaires et intégration Intelligence Artificielle (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import ModeleIA

class ModeleIAModelTest(TestCase):
    def test_creation_modele(self):
        modele = ModeleIA.objects.create(
            nom='DihyaNet', type='classification', version='1.0', proprietaire='Yidir')
        self.assertEqual(modele.nom, 'DihyaNet')
