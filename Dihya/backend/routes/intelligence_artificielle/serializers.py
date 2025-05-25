"""
Serializers ultra avancés pour Intelligence Artificielle (Django routes)
REST, GraphQL, multilingue, RGPD, plugins, audit, sécurité maximale.
"""
from rest_framework import serializers
from .models import AIProject, AIAsset

class AIProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIProject
        fields = ['id', 'name', 'description', 'lang', 'created_by', 'created_at', 'updated_at']

class AIAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIAsset
        fields = ['id', 'project', 'file', 'type', 'lang', 'uploaded_at']
