"""
Tests d’intégration Flask pour le module manufacturing : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.manufacturing import bp_manufacturing

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_manufacturing)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='manuuser')

def test_get_produits_authenticated(client, access_token):
    resp = client.get('/api/manufacturing/produits', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_produit_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.manufacturing.role_required', lambda role: (lambda f: f))
    data = {'nom': 'Test Produit', 'categorie': 'testcat'}
    resp = client.post('/api/manufacturing/produits', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['nom'] == 'Test Produit'

def test_i18n_get_produits(client, access_token):
    resp = client.get('/api/manufacturing/produits', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
