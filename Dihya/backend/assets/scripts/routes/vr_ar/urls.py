"""
Dihya Backend – Définition des routes Django REST/GraphQL pour IA/VR/AR
CORS, WAF, SEO, sécurité, plugins, multilingue, RGPD.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.list_projects, name='list_projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/update/', views.update_project, name='update_project'),
    # ... autres endpoints avancés ...
]

# GraphQL endpoint (exemple)
# from graphene_django.views import GraphQLView
# urlpatterns += [
#     path('graphql/', GraphQLView.as_view(graphiql=True)),
# ]
