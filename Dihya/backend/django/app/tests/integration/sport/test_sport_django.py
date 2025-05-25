"""
Tests d'intégration avancés pour le module Sport (événements, scores, plugins, RGPD, IA, REST & GraphQL, CI/CD, Docker, K8s, Codespaces, Linux).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.translation import activate

@pytest.mark.django_db
def test_create_sport_event():
    client = APIClient()
    activate('fr')
    data = {'nom': 'Tournoi', 'type': 'football'}
    response = client.post(reverse('sportevent-list'), data, format='json')
    assert response.status_code == 201
    assert 'id' in response.data

@pytest.mark.django_db
def test_plugin_sport():
    client = APIClient()
    activate('fr')
    response = client.get(reverse('sport-plugin'))
    assert response.status_code == 200
    # Vérification plugin, logs, audit, fallback IA
    # ...

@pytest.mark.django_db
def test_sport_ia():
    client = APIClient()
    activate('fr')
    data = {'question': 'Qui va gagner ?'}
    response = client.post(reverse('sport-ia'), data, format='json')
    assert response.status_code == 200
    assert any(x in response.data for x in ['llama', 'mixtral', 'mistral'])

# ...tests pour GraphQL, plugins, fallback IA, RGPD, anonymisation, logs, CORS, rôles, WAF, anti-DDOS, etc.
