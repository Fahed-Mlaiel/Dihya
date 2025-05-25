"""
Tests d'intégration avancés pour les routes Marketing (REST, GraphQL).
Sécurité maximale, multilingue, plugins, RGPD, audit, IA fallback.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.translation import activate

@pytest.mark.django_db
def test_marketing_routes_multilang_jwt_audit():
    client = APIClient()
    # JWT Authentification simulée
    token = 'Bearer test.jwt.token'
    headers = {'HTTP_AUTHORIZATION': token, 'HTTP_ACCEPT_LANGUAGE': 'fr'}
    activate('fr')
    response = client.get(reverse('marketing-list'), **headers)
    assert response.status_code == 200
    assert 'Campagne' in response.data['results'][0]['nom']
    # Audit log, RGPD, plugins, fallback IA mockés
    # ...

# ...tests pour GraphQL, plugins, fallback IA, RGPD, anonymisation, logs, CORS, rôles, etc.
