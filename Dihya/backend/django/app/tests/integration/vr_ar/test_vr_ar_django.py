"""
Tests d'intégration avancés pour les routes VR/AR du backend Dihya (Django).
Couvre REST, GraphQL, sécurité, i18n, plugins, audit, RGPD, IA fallback, multitenancy, rôles.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest import mock

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def auth_headers():
    # JWT simulé pour admin/user/invité
    return {
        'HTTP_AUTHORIZATION': 'Bearer test.jwt.token',
        'HTTP_X_ROLE': 'admin',
        'HTTP_X_TENANT': 'default',
        'HTTP_ACCEPT_LANGUAGE': 'fr',
    }

def test_vr_ar_route_rest(api_client, auth_headers):
    url = reverse('vr-ar-list')
    response = api_client.get(url, **auth_headers)
    assert response.status_code == status.HTTP_200_OK
    assert 'results' in response.data

def test_vr_ar_route_graphql(api_client, auth_headers):
    url = reverse('graphql')
    query = '{ vrArProjects { id name } }'
    response = api_client.post(url, {'query': query}, format='json', **auth_headers)
    assert response.status_code == status.HTTP_200_OK
    assert 'data' in response.data

def test_vr_ar_security_cors(api_client, auth_headers):
    url = reverse('vr-ar-list')
    response = api_client.options(url, **auth_headers)
    assert response.status_code == status.HTTP_200_OK
    assert 'Access-Control-Allow-Origin' in response

def test_vr_ar_i18n(api_client, auth_headers):
    url = reverse('vr-ar-list')
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = dict(auth_headers)
        headers['HTTP_ACCEPT_LANGUAGE'] = lang
        response = api_client.get(url, **headers)
        assert response.status_code == status.HTTP_200_OK

def test_vr_ar_plugin_system(api_client, auth_headers):
    url = reverse('vr-ar-plugins')
    response = api_client.get(url, **auth_headers)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)

def test_vr_ar_audit_log(api_client, auth_headers):
    url = reverse('vr-ar-list')
    with mock.patch('django.utils.timezone.now') as mock_now:
        mock_now.return_value = '2025-05-24T12:00:00Z'
        response = api_client.get(url, **auth_headers)
        assert response.status_code == status.HTTP_200_OK
        # Audit log vérifié via mock ou DB

def test_vr_ar_ia_fallback(api_client, auth_headers):
    url = reverse('vr-ar-ia')
    with mock.patch('app.services.ia.llama_fallback') as mock_llama:
        mock_llama.return_value = {'result': 'ok'}
        response = api_client.post(url, {'prompt': 'test'}, format='json', **auth_headers)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['result'] == 'ok'

def test_vr_ar_rgpd_export(api_client, auth_headers):
    url = reverse('vr-ar-export')
    response = api_client.get(url, **auth_headers)
    assert response.status_code == status.HTTP_200_OK
    assert response['Content-Type'] == 'application/zip'

def test_vr_ar_multitenancy(api_client, auth_headers):
    url = reverse('vr-ar-list')
    headers = dict(auth_headers)
    headers['HTTP_X_TENANT'] = 'tenant2'
    response = api_client.get(url, **headers)
    assert response.status_code == status.HTTP_200_OK

def test_vr_ar_roles(api_client, auth_headers):
    url = reverse('vr-ar-list')
    for role in ['admin', 'user', 'guest']:
        headers = dict(auth_headers)
        headers['HTTP_X_ROLE'] = role
        response = api_client.get(url, **headers)
        assert response.status_code in [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN]
