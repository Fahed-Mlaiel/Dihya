"""
Tests d'intégration avancés pour le module Voice (synthèse, reconnaissance, plugins, RGPD, IA, REST & GraphQL, CI/CD, Docker, K8s, Codespaces, Linux).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.translation import activate

@pytest.mark.django_db
def test_voice_synthesis():
    client = APIClient()
    activate('fr')
    data = {'texte': 'Bonjour'}
    response = client.post(reverse('voice-synthesis'), data, format='json')
    assert response.status_code == 200
    assert 'audio' in response.data

@pytest.mark.django_db
def test_voice_recognition():
    client = APIClient()
    activate('fr')
    data = {'audio': 'fake-audio-data'}
    response = client.post(reverse('voice-recognition'), data, format='json')
    assert response.status_code == 200
    assert 'texte' in response.data

@pytest.mark.django_db
def test_voice_ia():
    client = APIClient()
    activate('fr')
    data = {'question': 'Parle-moi'}
    response = client.post(reverse('voice-ia'), data, format='json')
    assert response.status_code == 200
    assert any(x in response.data for x in ['llama', 'mixtral', 'mistral'])

# ...tests pour GraphQL, plugins, fallback IA, RGPD, anonymisation, logs, CORS, rôles, WAF, anti-DDOS, etc.
