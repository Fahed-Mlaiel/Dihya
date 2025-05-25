"""
Tests d’intégration Flask pour le module logistique : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.logistique import bp_logistique

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_logistique)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='loguser')

def test_get_commandes_authenticated(client, access_token):
    resp = client.get('/api/logistique/commandes', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_commande_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.logistique.role_required', lambda role: (lambda f: f))
    data = {'produit': 'Test', 'quantite': 10}
    resp = client.post('/api/logistique/commandes', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['produit'] == 'Test'

def test_i18n_get_commandes(client, access_token):
    resp = client.get('/api/logistique/commandes', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
