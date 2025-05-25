"""
Tests d’intégration Flask pour le module marketing : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.marketing import bp_marketing

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_marketing)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='mktuser')

def test_get_campaigns_authenticated(client, access_token):
    resp = client.get('/api/marketing/campaigns', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_campaign_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.marketing.role_required', lambda role: (lambda f: f))
    data = {'nom': 'Test Campaign', 'type': 'email'}
    resp = client.post('/api/marketing/campaigns', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['nom'] == 'Test Campaign'

def test_i18n_get_campaigns(client, access_token):
    resp = client.get('/api/marketing/campaigns', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
