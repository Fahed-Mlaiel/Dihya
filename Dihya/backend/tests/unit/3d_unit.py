"""
Tests unitaires avancés pour le module 3D (sécurité, i18n, plugins, audit, RGPD, fallback IA)
"""
import pytest
from backend.modules.three_d import create_3d_model, export_3d_model, audit_3d_action

def test_create_3d_model():
    model = create_3d_model(name="Test3D", lang="fr")
    assert model.name == "Test3D"
    assert hasattr(model, 'id')

def test_export_3d_model():
    model = create_3d_model(name="Export3D", lang="en")
    export = export_3d_model(model.id, format="obj")
    assert export.startswith("# OBJ")

def test_audit_3d_action():
    logs = audit_3d_action(action="create", model_id=1)
    assert any("create" in l['action'] for l in logs)

def test_3d_i18n():
    model = create_3d_model(name="نموذج أمازيغي", lang="ar")
    assert model.lang == "ar"

def test_3d_plugin_integration():
    from backend.plugins import get_active_plugins
    plugins = get_active_plugins()
    assert "3d" in plugins

def test_3d_fallback_ia():
    from backend.ia import fallback_ia
    answer = fallback_ia(question="Génère un modèle 3D", lang="fr")
    assert "3D" in answer
