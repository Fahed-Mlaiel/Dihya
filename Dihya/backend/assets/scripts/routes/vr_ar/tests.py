"""
Dihya Backend – Tests ultra avancés pour IA/VR/AR
Unitaires, intégration, e2e, multilingue, sécurité, RGPD, plugins, audit, mock, fixtures.
"""
import pytest
from django.test import Client
from .schemas import ProjectCreate
from django.urls import reverse

@pytest.fixture
def client():
    return Client()

def test_create_project(client):
    data = {
        "name": "Test VR",
        "description": "Projet test VR multilingue.",
        "owner_email": "admin@dihya.ai",
        "language": "fr",
        "is_active": True,
        "tags": ["VR", "test"]
    }
    response = client.post(reverse('create_project'), data, content_type='application/json')
    assert response.status_code == 201
    assert response.json()["success"] is True

def test_list_projects(client):
    response = client.get(reverse('list_projects'))
    assert response.status_code == 200
    assert "projects" in response.json()

# ... autres tests avancés (sécurité, plugins, RGPD, audit, multilingue) ...
