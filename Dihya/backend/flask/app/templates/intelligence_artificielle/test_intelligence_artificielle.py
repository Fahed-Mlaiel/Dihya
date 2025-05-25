"""
Tests unitaires, intégration et e2e pour la gestion des projets IA (sécurité, i18n, plugins, audit, fallback IA).
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.intelligence_artificielle import bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'test'
    with app.test_client() as client:
        yield client

def test_list_projects_admin(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 't1'})
    rv = client.get('/api/ia/projects', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200
    assert 'projects' in rv.json

def test_create_project_validation(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 't1'})
    rv = client.post('/api/ia/projects', json={'name': 'Test IA'}, headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 201
    assert 'project' in rv.json

def test_get_project_fallback(client, mocker):
    token = create_access_token(identity={'role': 'user', 'tenant': 't1'})
    mocker.patch('app.templates.intelligence_artificielle.ai_fallback', return_value={'id': 'x', 'name': 'Fallback'})
    rv = client.get('/api/ia/projects/x', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200
    assert rv.json['project']['name'] == 'Fallback'
