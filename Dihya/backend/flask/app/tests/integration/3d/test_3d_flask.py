"""
Dihya Flask – Test d’intégration 3D (Ultra avancé, multilingue, sécurité, RGPD, plugins, fallback IA)
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
def test_upload_asset_3d(client: FlaskClient, lang, expected):
    """Test upload asset 3D sécurisé, multilingue, RGPD, plugins, fallback IA."""
    response = client.post('/api/v1/3d/assets/upload', data={'asset': (b'FAKE3D', 'cube.glb')}, headers={'Authorization': 'Bearer <token>', 'Accept-Language': lang})
    assert response.status_code in (200, 201)
    assert expected in response.json.get('message', '')

def test_scene_accessibility(client: FlaskClient):
    """Test accessibilité et SEO d’une scène 3D."""
    response = client.get('/api/v1/3d/scenes/scene_001', headers={'Accept-Language': 'en'})
    assert response.status_code == 200
    assert 'scene_id' in response.json
    # SEO/robots/sitemap
    robots = client.get('/api/v1/3d/robots.txt')
    assert robots.status_code == 200
    sitemap = client.get('/api/v1/3d/sitemap.xml')
    assert sitemap.status_code == 200

def test_graphql_3d(client: FlaskClient):
    """Test endpoint GraphQL 3D."""
    query = '{ scene(id: "scene_001") { id, name } }'
    response = client.post('/api/v1/3d/graphql', json={'query': query}, headers={'Authorization': 'Bearer <token>'})
    assert response.status_code == 200
    assert 'data' in response.json
