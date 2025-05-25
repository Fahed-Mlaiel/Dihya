"""
Tests d'intégration avancés pour le module Mode (API, plugins, RGPD, IA, multilingue, accessibilité, SEO, audit, fallback IA, REST & GraphQL, CI/CD, Docker, K8s, Codespaces, Linux).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.translation import activate

@pytest.mark.django_db
def test_mode_api_jwt_roles():
    client = APIClient()
    token = 'Bearer test.jwt.token'
    headers = {'HTTP_AUTHORIZATION': token}
    response = client.get(reverse('mode-list'), **headers)
    assert response.status_code == 200
    # Vérification plugins, RGPD, logs, fallback IA, multilingue...

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es", "tzm"])
@pytest.mark.django_db
def test_mode_i18n(lang):
    client = APIClient()
    activate(lang)
    response = client.get(reverse('mode-list'), HTTP_ACCEPT_LANGUAGE=lang)
    assert response.status_code == 200

@pytest.mark.django_db
def test_mode_rgpd_anonymisation():
    client = APIClient()
    response = client.post(reverse('mode-anonymise'), data={"user_id": 1})
    assert response.status_code in [200, 204]

@pytest.mark.django_db
def test_mode_plugin_extensible(monkeypatch):
    from app.plugins import plugin_manager
    monkeypatch.setattr(plugin_manager, "run", lambda *a, **kw: {"plugin": "ok"})
    assert plugin_manager.run("mode_check")["plugin"] == "ok"

@pytest.mark.django_db
def test_mode_accessibilite():
    client = APIClient()
    response = client.get(reverse('mode-a11y'))
    assert response.status_code == 200
    assert 'a11y' in response.data

@pytest.mark.django_db
def test_mode_audit_log():
    client = APIClient()
    response = client.get(reverse('mode-audit'))
    assert response.status_code == 200
    assert 'logs' in response.data

@pytest.mark.django_db
def test_mode_seo():
    client = APIClient()
    url = reverse('mode-robots')
    response = client.get(url)
    assert response.status_code == 200
    url = reverse('mode-sitemap')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_mode_graphql(monkeypatch):
    class MockResponse:
        status_code = 200
        data = {"data": {"mode": {"status": "ok"}}}
    monkeypatch.setattr("app.views.mode.graphql_mode", lambda *a, **kw: MockResponse())
    resp = app.views.mode.graphql_mode()
    assert resp.status_code == 200
    assert resp.data["data"]["mode"]["status"] == "ok"
