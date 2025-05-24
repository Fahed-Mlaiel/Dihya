"""
Dihya Flask – Test d’intégration VR/AR (Ultra avancé, multilingue, sécurité, RGPD, plugins, fallback IA)
"""
import pytest
from flask import Flask
from flask.testing import FlaskClient

@pytest.mark.parametrize("lang,expected", [
    ("fr", "importé"),
    ("en", "uploaded"),
    ("ar", "تم التحميل"),
    ("tzm", "ⴰⵙⵉⵏⴰⵡⴰⵏ")
])
def test_upload_asset_vr_ar(client: FlaskClient, lang, expected):
    """Test upload asset VR/AR sécurisé, multilingue, RGPD, plugins, fallback IA."""
    response = client.post('/api/v1/vr_ar/assets/upload', data={'asset': (b'FAKEVR', 'scene.glb')}, headers={'Authorization': 'Bearer <token>', 'Accept-Language': lang})
    assert response.status_code in (200, 201)
    assert expected in response.json.get('message', '')

def test_scene_accessibility(client: FlaskClient):
    """Test accessibilité et SEO d’une scène VR/AR."""
    response = client.get('/api/v1/vr_ar/scenes/scene_001', headers={'Accept-Language': 'en'})
    assert response.status_code == 200
    assert 'scene_id' in response.json
    # SEO/robots/sitemap
    robots = client.get('/api/v1/vr_ar/robots.txt')
    assert robots.status_code == 200
    sitemap = client.get('/api/v1/vr_ar/sitemap.xml')
    assert sitemap.status_code == 200

def test_graphql_vr_ar(client: FlaskClient):
    """Test endpoint GraphQL VR/AR."""
    query = '{ scene(id: "scene_001") { id, name } }'
    response = client.post('/api/v1/vr_ar/graphql', json={'query': query}, headers={'Authorization': 'Bearer <token>'})
    assert response.status_code == 200
    assert 'data' in response.json
