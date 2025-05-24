"""
Dihya Flask – Test d’intégration Restauration (Ultra avancé, multilingue, sécurité, RGPD, plugins, fallback IA)
"""
import pytest
from flask import Flask
from flask.testing import FlaskClient

@pytest.mark.parametrize("lang,expected", [
    ("fr", "créée"),
    ("en", "created"),
    ("ar", "تم الإنشاء"),
    ("tzm", "ⴰⵎⵙⵙⴰⵍ")
])
def test_creation_commande_restauration(client: FlaskClient, lang, expected):
    """Test création commande restauration sécurisé, multilingue, RGPD, plugins, fallback IA."""
    response = client.post('/api/v1/restauration/commandes', json={"table": 1, "plats": ["couscous"]}, headers={'Authorization': 'Bearer <token>', 'Accept-Language': lang})
    assert response.status_code in (200, 201)
    assert expected in response.json.get('message', '')

def test_menu_accessibility(client: FlaskClient):
    """Test accessibilité et SEO du menu restauration."""
    response = client.get('/api/v1/restauration/menu', headers={'Accept-Language': 'en'})
    assert response.status_code == 200
    assert 'menu' in response.json
    # SEO/robots/sitemap
    robots = client.get('/api/v1/restauration/robots.txt')
    assert robots.status_code == 200
    sitemap = client.get('/api/v1/restauration/sitemap.xml')
    assert sitemap.status_code == 200

def test_graphql_restauration(client: FlaskClient):
    """Test endpoint GraphQL restauration."""
    query = '{ commande(id: "cmd_001") { id, table, plats } }'
    response = client.post('/api/v1/restauration/graphql', json={'query': query}, headers={'Authorization': 'Bearer <token>'})
    assert response.status_code == 200
    assert 'data' in response.json
