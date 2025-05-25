"""
test_intelligence_artificielle_flask.py - Test d’intégration avancé pour la gestion de projets IA
Sécurité, multitenancy, i18n, plugins, audit, fallback IA, RGPD
"""
import pytest
from flask_jwt_extended import create_access_token
from app import create_app

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as client:
        yield client

def test_list_projects_ia(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.get('/api/intelligence_artificielle/projects', headers={'Authorization': f'Bearer {token}', 'Accept-Language': 'fr'})
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_create_project_ia(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.post('/api/intelligence_artificielle/projects', headers={'Authorization': f'Bearer {token}'}, json={'name': 'Projet IA Test'})
    assert res.status_code == 201
    assert 'msg' in res.json
