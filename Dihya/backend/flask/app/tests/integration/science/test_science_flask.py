"""
Tests d’intégration Flask pour le module science : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.science import bp_science

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_science)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='scienceuser')

def test_get_recherches_authenticated(client, access_token):
    resp = client.get('/api/science/recherches', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_recherche_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.science.role_required', lambda role: (lambda f: f))
    data = {'titre': 'Test Recherche', 'domaine': 'physique'}
    resp = client.post('/api/science/recherches', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['titre'] == 'Test Recherche'

def test_i18n_get_recherches(client, access_token):
    resp = client.get('/api/science/recherches', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
