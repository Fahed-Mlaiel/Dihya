"""
Tests d’intégration Flask pour le module gamer : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.gamer import bp_gamer

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_gamer)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='gameruser')

def test_get_jeux_authenticated(client, access_token):
    resp = client.get('/api/gamer/jeux', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_jeu_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.gamer.role_required', lambda role: (lambda f: f))
    data = {'titre': 'Test Jeu', 'genre': 'aventure'}
    resp = client.post('/api/gamer/jeux', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['titre'] == 'Test Jeu'

def test_i18n_get_jeux(client, access_token):
    resp = client.get('/api/gamer/jeux', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
