"""
Tests unitaires, intégration et e2e pour la gestion des projets juridiques.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.templates.juridique import bp

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
    rv = client.get('/api/juridique/projects', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200
    assert 'projects' in rv.json

def test_create_project_validation(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 't1'})
    rv = client.post('/api/juridique/projects', json={'name': 'Test Juridique'}, headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 201
    assert 'project' in rv.json

def test_get_project(client):
    token = create_access_token(identity={'role': 'user', 'tenant': 't1'})
    rv = client.get('/api/juridique/projects/x', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code in (200, 404)
