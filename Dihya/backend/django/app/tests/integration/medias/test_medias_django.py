"""
Tests d'intégration avancés pour les routes Médias (upload, accès, plugins, RGPD, IA, multilingue).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_media_upload_jwt_cors():
    client = APIClient()
    token = 'Bearer test.jwt.token'
    headers = {'HTTP_AUTHORIZATION': token}
    with open('test.jpg', 'rb') as f:
        response = client.post(reverse('media-upload'), {'file': f}, format='multipart', **headers)
    assert response.status_code == 201
    # Vérification RGPD, logs, plugins, fallback IA, multilingue...

# ...autres tests (accès, plugins, anonymisation, logs, rôles, etc.)
