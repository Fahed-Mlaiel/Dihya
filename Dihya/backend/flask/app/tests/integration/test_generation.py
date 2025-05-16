"""
Tests d'intégration pour la génération automatique – Dihya Coding

Ce module teste l'intégration complète de la génération automatique :
- Appel de l'API /generate
- Orchestration du service de génération
- Validation de la traçabilité (logs)
- Sécurité (pas de fuite de données sensibles)
- Robustesse sur différents scénarios (succès, erreurs, plugins, edge cases)

Bonnes pratiques :
- Ne jamais utiliser de données réelles ou sensibles dans les tests.
- Vérifier la conformité RGPD (pas de fuite d'identité, de secrets, etc.).
- Documenter chaque scénario de test.
- Couvrir les cas de succès, d'échec, de plugins, d'edge cases et de sécurité.
"""

import pytest
from flask import Flask
from flask.testing import FlaskClient

from app.routes.generate import generate_bp
from app.services import generation_service

@pytest.fixture
def client():
    """Fixture Flask test client pour l'API."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["JWT_SECRET_KEY"] = "test"
    app.register_blueprint(generate_bp)
    return app.test_client()

def test_generate_success(client):
    """Test génération réussie avec un cahier des charges valide."""
    payload = {
        "spec": "Créer une app de blog avec authentification et SEO.",
        "type": "webapp",
        "stack": "react+flask"
    }
    # Simuler authentification JWT (mock ou bypass selon config)
    headers = {"Authorization": "Bearer testtoken"}
    response = client.post("/api/generate", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "code" in data
    assert "README.md" in data["code"]

def test_generate_invalid_spec(client):
    """Test génération avec un cahier des charges trop court (erreur attendue)."""
    payload = {"spec": "Trop court", "type": "webapp"}
    headers = {"Authorization": "Bearer testtoken"}
    response = client.post("/api/generate", json=payload, headers=headers)
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "cahier des charges" in data["error"].lower()

def test_generate_invalid_project_name(monkeypatch, client):
    """Test génération avec un nom de projet invalide (mock analyse)."""
    def fake_analyze_spec(_):
        return {
            "project_name": "!!",
            "stack": ["fullstack"],
            "modules": [],
            "owner": "user",
            "created_at": "2025-01-01T00:00:00Z"
        }
    monkeypatch.setattr(generation_service, "analyze_spec", fake_analyze_spec)
    payload = {"spec": "Projet bidon", "type": "webapp"}
    headers = {"Authorization": "Bearer testtoken"}
    response = client.post("/api/generate", json=payload, headers=headers)
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "nom de projet" in data["error"].lower()

def test_generate_with_plugin(monkeypatch, client):
    """Test génération avec application d'un plugin custom."""
    def fake_analyze_spec(_):
        return {
            "project_name": "PluginTest",
            "stack": ["fullstack"],
            "modules": [],
            "owner": "user",
            "created_at": "2025-01-01T00:00:00Z",
            "plugins": ["analytics"]
        }
    def fake_apply_plugins(code, plugins):
        code["README.md"] += "\nPlugin analytics appliqué."
        return code
    monkeypatch.setattr(generation_service, "analyze_spec", fake_analyze_spec)
    monkeypatch.setattr(generation_service, "apply_plugins", fake_apply_plugins)
    payload = {"spec": "Projet avec plugin", "type": "webapp"}
    headers = {"Authorization": "Bearer testtoken"}
    response = client.post("/api/generate", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert "Plugin analytics appliqué" in data["code"]["README.md"]

def test_generate_no_sensitive_data_in_logs(monkeypatch, client, caplog):
    """Vérifie qu'aucune donnée sensible n'est loggée lors de la génération."""
    payload = {"spec": "Créer une app confidentielle", "type": "webapp"}
    headers = {"Authorization": "Bearer testtoken"}
    with caplog.at_level("INFO"):
        client.post("/api/generate", json=payload, headers=headers)
    for record in caplog.records:
        assert "mot de passe" not in record.getMessage().lower()
        assert "secret" not in record.getMessage().lower()
        assert "token" not in record.getMessage().lower()