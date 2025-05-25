"""
Tests d’intégration Flask pour le module automobile : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.automobile import bp_automobile

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_automobile)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='autouser')

def test_get_vehicules_authenticated(client, access_token):
    resp = client.get('/api/automobile/vehicules', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_vehicule_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.automobile.role_required', lambda role: (lambda f: f))
    data = {'marque': 'Test', 'modele': 'TestModel'}
    resp = client.post('/api/automobile/vehicules', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['marque'] == 'Test'

def test_i18n_get_vehicules(client, access_token):
    resp = client.get('/api/automobile/vehicules', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
