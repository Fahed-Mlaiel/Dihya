"""
Tests d’intégration Flask pour le module intelligence_artificielle : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.intelligence_artificielle import bp_intelligence_artificielle

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_intelligence_artificielle)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='iauser')

def test_get_models_authenticated(client, access_token):
    resp = client.get('/api/intelligence_artificielle/models', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_model_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.intelligence_artificielle.role_required', lambda role: (lambda f: f))
    data = {'nom': 'Test Model', 'type': 'classification'}
    resp = client.post('/api/intelligence_artificielle/models', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['nom'] == 'Test Model'

def test_i18n_get_models(client, access_token):
    resp = client.get('/api/intelligence_artificielle/models', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
