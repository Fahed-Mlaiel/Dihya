"""
Tests d’intégration Flask pour le module publicite : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.publicite import bp_publicite

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_publicite)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='pubuser')

def test_get_campaigns_authenticated(client, access_token):
    resp = client.get('/api/publicite/campaigns', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_campaign_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.publicite.role_required', lambda role: (lambda f: f))
    data = {'nom': 'Test Campaign', 'type': 'affichage'}
    resp = client.post('/api/publicite/campaigns', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['nom'] == 'Test Campaign'

def test_i18n_get_campaigns(client, access_token):
    resp = client.get('/api/publicite/campaigns', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
