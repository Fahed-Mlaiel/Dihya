"""
Tests d’intégration Flask pour le module arts : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.arts import bp_arts

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_arts)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='artsuser')

def test_get_oeuvres_authenticated(client, access_token):
    resp = client.get('/api/arts/oeuvres', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_oeuvre_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.arts.role_required', lambda role: (lambda f: f))
    data = {'name': 'Test Oeuvre', 'type': 'peinture'}
    resp = client.post('/api/arts/oeuvres', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['name'] == 'Test Oeuvre'

def test_i18n_get_oeuvres(client, access_token):
    resp = client.get('/api/arts/oeuvres', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
