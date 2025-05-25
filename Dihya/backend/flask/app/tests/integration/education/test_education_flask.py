"""
Tests d’intégration Flask pour le module education : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.education import bp_education

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_education)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='eduuser')

def test_get_cours_authenticated(client, access_token):
    resp = client.get('/api/education/cours', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_cours_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.education.role_required', lambda role: (lambda f: f))
    data = {'titre': 'Test Cours', 'niveau': 'débutant'}
    resp = client.post('/api/education/cours', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['titre'] == 'Test Cours'

def test_i18n_get_cours(client, access_token):
    resp = client.get('/api/education/cours', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
