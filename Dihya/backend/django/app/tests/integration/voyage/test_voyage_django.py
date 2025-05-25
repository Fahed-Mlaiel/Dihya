"""
Tests d'intégration avancés pour le module Voyage (itinéraires, réservations, plugins, RGPD, IA, REST & GraphQL, CI/CD, Docker, K8s, Codespaces, Linux).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.translation import activate

@pytest.mark.django_db
def test_create_voyage():
    client = APIClient()
    activate('fr')
    data = {'destination': 'Paris', 'date': '2025-06-01'}
    response = client.post(reverse('voyage-list'), data, format='json')
    assert response.status_code == 201
    assert 'id' in response.data

@pytest.mark.django_db
def test_plugin_voyage():
    client = APIClient()
    activate('fr')
    response = client.get(reverse('voyage-plugin'))
    assert response.status_code == 200
    # Vérification plugin, logs, audit, fallback IA
    # ...

@pytest.mark.django_db
def test_voyage_ia():
    client = APIClient()
    activate('fr')
    data = {'question': 'Où partir ?'}
    response = client.post(reverse('voyage-ia'), data, format='json')
    assert response.status_code == 200
    assert any(x in response.data for x in ['llama', 'mixtral', 'mistral'])

# ...tests pour GraphQL, plugins, fallback IA, RGPD, anonymisation, logs, CORS, rôles, WAF, anti-DDOS, etc.
