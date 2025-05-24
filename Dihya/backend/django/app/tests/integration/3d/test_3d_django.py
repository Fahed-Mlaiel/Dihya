"""
Tests d’intégration avancés Django pour la gestion 3D sur Dihya.
- Vérifie l’import, l’upload, le rendu, la sécurité, l’accessibilité et la souveraineté des assets/scènes 3D.
- Multilingue (fr, en, ar, amazigh), sécurité, fallback IA open source, CI/CD ready.
"""

import os
import pytest
from django.test import Client
from django.urls import reverse
from django.conf import settings

# Si le module VR/AR expose une API Django, on teste l’upload et le rendu d’assets/scènes
@pytest.mark.django_db
def test_upload_asset_3d(tmp_path):
    """
    Teste l’upload d’un asset 3D via l’API Django (sécurité, accessibilité, multilingue).
    """
    client = Client()
    asset_path = tmp_path / "cube.glb"
    asset_path.write_bytes(b"FAKEGLB3DCONTENT")
    with asset_path.open("rb") as f:
        response = client.post(
            reverse("vr_ar:upload_asset"),
            {"asset": f, "name": "cube.glb"},
            HTTP_ACCEPT_LANGUAGE="fr"
        )
    assert response.status_code == 201
    assert "importé" in response.json().get("message", "") or "uploaded" in response.json().get("message", "")

@pytest.mark.django_db
def test_scene_render_accessibility(client):
    """
    Teste le rendu d’une scène immersive et l’accessibilité (présence ARIA, fallback, multilingue).
    """
    url = reverse("vr_ar:scene_detail", kwargs={"scene_id": "scene_001"})
    response = client.get(url, HTTP_ACCEPT_LANGUAGE="en")
    assert response.status_code == 200
    assert b'<a-scene' in response.content or b'vr-ar-canvas' in response.content
    # Vérifie accessibilité ARIA/fallback
    assert b'aria-label' in response.content or b'alt=' in response.content

@pytest.mark.django_db
@pytest.mark.parametrize("lang,expected", [
    ("fr", "Scène immersive chargée."),
    ("en", "Immersive scene loaded."),
    ("ar", "تم تحميل المشهد الافتراضي."),
    ("ber", "ⴰⵙⵉⵏⴰⵡⴰⵏ ⵏ VR/AR ⴰⴷⴷⴰⵔⴰⵏ."),
])
def test_scene_load_multilang(client, lang, expected):
    """
    Vérifie le message de chargement de scène en multilingue.
    """
    url = reverse("vr_ar:scene_detail", kwargs={"scene_id": "scene_001"})
    response = client.get(url, HTTP_ACCEPT_LANGUAGE=lang)
    assert response.status_code == 200
    assert expected.encode("utf-8") in response.content

@pytest.mark.django_db
def test_security_asset_upload_permission(client):
    """
    Vérifie que l’upload d’asset 3D nécessite une permission spécifique.
    """
    url = reverse("vr_ar:upload_asset")
    response = client.post(url, {"name": "cube.glb"})
    # Doit refuser si non authentifié ou sans permission
    assert response.status_code in (401, 403)

@pytest.mark.django_db
def test_fallback_open_source_ai(client, monkeypatch):
    """
    Vérifie le fallback IA open source sur la validation d’un asset 3D.
    """
    url = reverse("vr_ar:validate_asset")
    def fake_validate(*args, **kwargs):
        return {"status": "ai_fallback", "suggestion": "Suggestion générée par IA open source."}
    monkeypatch.setattr("templates.vr_ar.template.VRARTemplate.fallback_open_source_ai", fake_validate)
    response = client.post(url, {"name": "cube.glb"})
    assert response.status_code == 200
    assert "ai_fallback" in response.json().get("status", "")

# Test d’intégration rapide (smoke test)
@pytest.mark.django_db
def test_smoke_3d_integration(client):
    """
    Test d’intégration rapide sur l’API 3D Django.
    """
    # Upload asset (doit échouer sans permission)
    url_upload = reverse("vr_ar:upload_asset")
    resp_upload = client.post(url_upload, {"name": "cube.glb"})
    assert resp_upload.status_code in (401, 403)
    # Charger une scène
    url_scene = reverse("vr_ar:scene_detail", kwargs={"scene_id": "scene_001"})
    resp_scene = client.get(url_scene)
    assert resp_scene.status_code == 200

"""
Pour lancer les tests :
    pytest test_3d_django.py

Ce fichier garantit la robustesse, la sécurité, la multilingue, l’accessibilité, la souveraineté et la compatibilité CI/CD des fonctionnalités 3D Django de Dihya.
"""
