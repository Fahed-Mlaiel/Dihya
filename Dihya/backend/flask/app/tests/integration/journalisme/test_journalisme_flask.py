"""
Tests d’intégration Flask pour le module journalisme : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.journalisme import bp_journalisme

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_journalisme)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='journouser')

def test_get_articles_authenticated(client, access_token):
    resp = client.get('/api/journalisme/articles', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_article_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.journalisme.role_required', lambda role: (lambda f: f))
    data = {'titre': 'Test Article', 'contenu': 'Lorem ipsum'}
    resp = client.post('/api/journalisme/articles', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['titre'] == 'Test Article'

def test_i18n_get_articles(client, access_token):
    resp = client.get('/api/journalisme/articles', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
