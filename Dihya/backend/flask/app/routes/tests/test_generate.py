"""
Tests unitaires pour la route de génération automatique (generate) de Dihya Coding.

Vérifie la conformité de l’API, la validation des entrées, la sécurité (auth, rôles),
la robustesse de la génération (succès, erreurs, edge cases) et la non-fuite de données sensibles.
"""

import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from app.routes.generate import generate_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "test"
    app.register_blueprint(generate_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user_token():
    return create_access_token(identity={"username": "alice", "role": "user"})

def test_generate_success(client, user_token):
    payload = {
        "spec": "Créer une boutique e-commerce avec paiement et gestion des stocks.",
        "type": "ecommerce"
    }
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 200
    assert "project" in response.json

def test_generate_missing_spec(client, user_token):
    payload = {"type": "ecommerce"}
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 400 or response.status_code == 422

def test_generate_unauthorized(client):
    payload = {"spec": "Créer un blog.", "type": "blog"}
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 401

def test_generate_invalid_type(client, user_token):
    payload = {"spec": "Créer un projet inconnu.", "type": "inconnu"}
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 400 or response.status_code == 422

def test_no_sensitive_data_in_response(client, user_token):
    payload = {"spec": "Créer un site.", "type": "ecommerce"}
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert "password" not in str(response.json).lower()
    assert "secret" not in str(response.json).lower()