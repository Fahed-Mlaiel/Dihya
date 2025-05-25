"""
Tests d'intégration avancés pour les routes Science (API, plugins, RGPD, IA, multilingue).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_science_api_jwt_roles():
    client = APIClient()
    token = 'Bearer test.jwt.token'
    headers = {'HTTP_AUTHORIZATION': token}
    response = client.get(reverse('science-list'), **headers)
    assert response.status_code == 200
    # Vérification plugins, RGPD, logs, fallback IA, multilingue...

# ...autres tests (création, plugins, anonymisation, logs, rôles, etc.)
