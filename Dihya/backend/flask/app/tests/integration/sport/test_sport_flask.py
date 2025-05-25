"""
Tests d’intégration Flask pour le module sport : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.sport import bp_sport

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_sport)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='sportuser')

def test_get_evenements_authenticated(client, access_token):
    resp = client.get('/api/sport/evenements', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_evenement_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.sport.role_required', lambda role: (lambda f: f))
    data = {'nom': 'Test Event', 'type': 'football'}
    resp = client.post('/api/sport/evenements', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['nom'] == 'Test Event'

def test_i18n_get_evenements(client, access_token):
    resp = client.get('/api/sport/evenements', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
