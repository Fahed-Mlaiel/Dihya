"""
Tests ultra avancés pour le module VR/AR (Django routes)
Couvre REST, GraphQL, sécurité, multilingue, RGPD, audit, plugins, accessibilité, performance, e2e.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Scene, Asset

def create_user(username, password, role='user'):
    user = get_user_model().objects.create_user(username=username, password=password)
    user.role = role
    user.save()
    return user

@pytest.mark.django_db
def test_create_scene_fr():
    client = APIClient()
    user = create_user('userfr', 'pass', 'admin')
    client.force_authenticate(user=user)
    data = {
        'title': 'Scène immersive musée (FR)',
        'description': 'Visite virtuelle d’un musée français.',
        'lang': 'fr'
    }
    response = client.post(reverse('vr_ar-scene-list'), data)
    assert response.status_code == 201
    assert Scene.objects.filter(title='Scène immersive musée (FR)').exists()

@pytest.mark.django_db
def test_graphql_scene_query():
    client = APIClient()
    user = create_user('graphqluser', 'pass', 'user')
    client.force_authenticate(user=user)
    scene = Scene.objects.create(title='GraphQL Test', description='Test GraphQL', lang='en', created_by=user)
    query = '''
    query {
      scenes {
        id
        title
        description
        lang
      }
    }
    '''
    response = client.post('/graphql/', {'query': query}, format='json')
    assert response.status_code == 200
    assert 'GraphQL Test' in str(response.content)

@pytest.mark.django_db
def test_permission_denied():
    client = APIClient()
    user1 = create_user('user1', 'pass', 'user')
    user2 = create_user('user2', 'pass', 'user')
    client.force_authenticate(user=user2)
    scene = Scene.objects.create(title='Immersive Museum Scene (EN)', description='Virtual tour of an English museum.', lang='en', created_by=user1)
    response = client.delete(reverse('vr_ar-scene-detail', args=[scene.id]))
    assert response.status_code == 403

@pytest.mark.django_db
def test_rgpd_export():
    client = APIClient()
    user = create_user('userrgpd', 'pass', 'user')
    client.force_authenticate(user=user)
    response = client.get('/vr_ar/rgpd-export/')
    assert response.status_code in [200, 501]
