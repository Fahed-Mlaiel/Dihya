"""
Dihya – Tests pour le module SEO
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import PageSEO, AuditSEO
from rest_framework.test import APIClient
from rest_framework import status

class SEOAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='seouser', password='testpass', is_seo_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.page = PageSEO.objects.create(url='https://example.com', titre='Accueil', description='Page d’accueil', mots_cles='test,seo', indexable=True)

    def test_create_audit(self):
        data = {'page': self.page.id, 'score': 95, 'rapport': 'OK'}
        response = self.client.post('/api/seo/auditseo/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['score'], 95)

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/seo/pageseo/', {'url': 'https://x.com', 'titre': 'X', 'description': 'Y', 'mots_cles': 'z', 'indexable': True})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
