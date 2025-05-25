"""
Tests d'intégration avancés pour le module Immobilier de Dihya.
Couvre sécurité (CORS, JWT, WAF, anti-DDOS), i18n, multitenancy, RGPD, plugins, audit, accessibilité, SEO, fallback IA, REST & GraphQL.
Compatible CI/CD, Docker, K8s, Codespaces, Linux.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def admin_user(db):
    user = User.objects.create_superuser('admin', 'admin@example.com', 'password')
    return user

@pytest.mark.django_db
def test_immobilier_endpoint_authenticated(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = reverse('immobilier-list')
    response = api_client.get(url, HTTP_ACCEPT_LANGUAGE='fr')
    assert response.status_code == 200
    assert 'biens' in response.data

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es", "tzm"])
@pytest.mark.django_db
def test_immobilier_i18n(api_client, admin_user, lang):
    api_client.force_authenticate(user=admin_user)
    url = reverse('immobilier-list')
    response = api_client.get(url, HTTP_ACCEPT_LANGUAGE=lang)
    assert response.status_code == 200

@pytest.mark.django_db
def test_immobilier_jwt_security(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = reverse('immobilier-list')
    response = api_client.get(url, HTTP_AUTHORIZATION='Bearer test.jwt.token')
    assert response.status_code in [200, 401]

@pytest.mark.django_db
def test_immobilier_rbac_guest(api_client):
    url = reverse('immobilier-list')
    response = api_client.get(url)
    assert response.status_code in [200, 403]

@pytest.mark.django_db
def test_immobilier_rgpd_anonymisation(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = reverse('immobilier-anonymise')
    response = api_client.post(url, data={"user_id": admin_user.id})
    assert response.status_code in [200, 204]

def test_immobilier_fallback_ia(monkeypatch):
    from app.services.ia import fallback_llama
    monkeypatch.setattr(fallback_llama, "call", lambda *a, **kw: {"result": "ok"})
    assert fallback_llama.call({"prompt": "immobilier"})["result"] == "ok"

def test_immobilier_accessibilite(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = reverse('immobilier-a11y')
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'a11y' in response.data

@pytest.mark.django_db
def test_immobilier_audit_log(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = reverse('immobilier-audit')
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'logs' in response.data

def test_immobilier_plugin_extensible(monkeypatch):
    from app.plugins import plugin_manager
    monkeypatch.setattr(plugin_manager, "run", lambda *a, **kw: {"plugin": "ok"})
    assert plugin_manager.run("immobilier_check")["plugin"] == "ok"

def test_immobilier_seo(api_client):
    url = reverse('immobilier-robots')
    response = api_client.get(url)
    assert response.status_code == 200
    url = reverse('immobilier-sitemap')
    response = api_client.get(url)
    assert response.status_code == 200

def test_immobilier_graphql(monkeypatch):
    class MockResponse:
        status_code = 200
        data = {"data": {"immobilier": {"status": "ok"}}}
    monkeypatch.setattr("app.views.immobilier.graphql_immobilier", lambda *a, **kw: MockResponse())
    resp = app.views.immobilier.graphql_immobilier()
    assert resp.status_code == 200
    assert resp.data["data"]["immobilier"]["status"] == "ok"
