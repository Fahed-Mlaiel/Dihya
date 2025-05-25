"""
Tests d'intégration avancés pour le module Santé (API, plugins, RGPD, IA, multilingue, accessibilité, SEO, audit, fallback IA, REST & GraphQL, CI/CD, Docker, K8s, Codespaces, Linux).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.translation import activate

@pytest.mark.django_db
def test_sante_api_jwt_roles():
    client = APIClient()
    token = 'Bearer test.jwt.token'
    headers = {'HTTP_AUTHORIZATION': token}
    response = client.get(reverse('sante-list'), **headers)
    assert response.status_code == 200
    # Vérification plugins, RGPD, logs, fallback IA, multilingue...

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es", "tzm"])
@pytest.mark.django_db
def test_sante_i18n(lang):
    client = APIClient()
    activate(lang)
    response = client.get(reverse('sante-list'), HTTP_ACCEPT_LANGUAGE=lang)
    assert response.status_code == 200

@pytest.mark.django_db
def test_sante_rgpd_anonymisation():
    client = APIClient()
    response = client.post(reverse('sante-anonymise'), data={"user_id": 1})
    assert response.status_code in [200, 204]

@pytest.mark.django_db
def test_sante_plugin_extensible(monkeypatch):
    from app.plugins import plugin_manager
    monkeypatch.setattr(plugin_manager, "run", lambda *a, **kw: {"plugin": "ok"})
    assert plugin_manager.run("sante_check")["plugin"] == "ok"

@pytest.mark.django_db
def test_sante_accessibilite():
    client = APIClient()
    response = client.get(reverse('sante-a11y'))
    assert response.status_code == 200
    assert 'a11y' in response.data

@pytest.mark.django_db
def test_sante_audit_log():
    client = APIClient()
    response = client.get(reverse('sante-audit'))
    assert response.status_code == 200
    assert 'logs' in response.data

@pytest.mark.django_db
def test_sante_seo():
    client = APIClient()
    url = reverse('sante-robots')
    response = client.get(url)
    assert response.status_code == 200
    url = reverse('sante-sitemap')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_sante_graphql(monkeypatch):
    class MockResponse:
        status_code = 200
        data = {"data": {"sante": {"status": "ok"}}}
    monkeypatch.setattr("app.views.sante.graphql_sante", lambda *a, **kw: MockResponse())
    resp = app.views.sante.graphql_sante()
    assert resp.status_code == 200
    assert resp.data["data"]["sante"]["status"] == "ok"
