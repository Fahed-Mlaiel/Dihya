"""
Dihya – Django Intelligence Artificielle API Routes Ultra Avancé
---------------------------------------------------------------
- Endpoints REST pour modèles, prédictions, analyses, entraînements, datasets, agents, pipelines, logs, audit
- Sécurité, RBAC, logs, chiffrement, conformité RGPD/NIS2, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

🇫🇷 Routes Django REST IA (sécurité, multilingue, souveraineté)
🇬🇧 Django REST AI routes (security, multilingual, sovereignty)
🇦🇪 مسارات Django REST للذكاء الاصطناعي (الأمان، متعدد اللغات، السيادة)
ⵣ Iwalen Django REST n tazwart n tafat n tnekra (amatu, multilingual, sovereignty)
"""

from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'modeles', views.ModeleViewSet, basename='modele')
router.register(r'predictions', views.PredictionViewSet, basename='prediction')
router.register(r'analyses', views.AnalyseViewSet, basename='analyse')
router.register(r'entrainements', views.EntrainementViewSet, basename='entrainement')
router.register(r'datasets', views.DatasetViewSet, basename='dataset')
router.register(r'agents', views.AgentViewSet, basename='agent')
router.register(r'pipelines', views.PipelineViewSet, basename='pipeline')
router.register(r'ia', views.IAOpenSourceViewSet, basename='ia-open-source')
router.register(r'notifications', views.NotificationViewSet, basename='notification')
router.register(r'audit/logs', views.AuditLogViewSet, basename='audit-log')

urlpatterns = [
    path('', include(router.urls)),
]

# Sécurité : endpoints protégés JWT, RBAC, logs, chiffrement, audit, conformité RGPD/NIS2
# Multilingue : tous les messages d’erreur/succès sont traduits (voir serializers.py)
# Fallback IA open source : tous les endpoints critiques disposent d’un fallback open source
# Extensible : ajoutez vos endpoints (analyse IA, open data, génération doc, etc.)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
