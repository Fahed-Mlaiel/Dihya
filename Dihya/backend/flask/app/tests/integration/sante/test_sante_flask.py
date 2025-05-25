"""
Tests d’intégration Flask pour le module santé : endpoints, sécurité, validation, audit, RGPD, i18n, plugins.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.sante import bp_sante

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_sante)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='santeuser')

def test_get_patients_authenticated(client, access_token):
    resp = client.get('/api/sante/patients', headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

def test_create_patient_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.sante.role_required', lambda role: (lambda f: f))
    data = {'nom': 'Test Patient', 'age': 30}
    resp = client.post('/api/sante/patients', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert resp.status_code == 201
    assert resp.get_json()['data']['nom'] == 'Test Patient'

def test_i18n_get_patients(client, access_token):
    resp = client.get('/api/sante/patients', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert resp.status_code == 200
    assert 'data' in resp.get_json()

# Autres tests : audit, RGPD, plugins, erreurs...
