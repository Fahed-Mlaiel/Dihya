"""
Dihya – VR/AR Images URLs
Définition des routes REST/GraphQL pour la gestion des images IA, VR, AR.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_vrar_image, name='upload_vrar_image'),
    path('list/', views.list_vrar_images, name='list_vrar_images'),
    path('get/<str:filename>/', views.get_vrar_image, name='get_vrar_image'),
]
