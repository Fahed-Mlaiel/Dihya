"""
Tests d’intégration Flask pour le module transport : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.transport import bp_transport

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_transport)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='transportuser')

def test_get_routes_authenticated(client, access_token):
    resp = client.get('/api/transport/routes', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_route_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.transport.role_required', lambda role: (lambda f: f))
    data = {'name': 'Test Route', 'type': 'Bus'}
    resp = client.post('/api/transport/routes', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['name'] == 'Test Route'

def test_i18n_get_routes(client, access_token):
    resp = client.get('/api/transport/routes', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
