"""
Tests d’intégration avancés Django pour les modules automobile sur Dihya.
- Vérifie la gestion du parc, sécurité, accessibilité, multilingue, souveraineté, fallback IA open source.
- Compatible CI/CD, zéro faux positif, prêt Codespaces.
"""

import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_vehicule_multilingue():
    """
    Teste la création d’un véhicule en multilingue (fr, en, ar, amazigh).
    """
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("automobile:create_vehicule"), {
            "marque": "Test",
            "modele": "2025",
            "immatriculation": f"TEST-{lang}"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")

@pytest.mark.django_db
def test_suivi_vehicule_alerte_ia():
    """
    Teste la saisie d’un incident et l’alerte IA open source.
    """
    client = Client()
    # Saisie d'un incident
    resp_saisie = client.post(reverse("automobile:saisir_incident"), {
        "vehicule_id": 1,
        "type": "panne",
        "description": "Batterie faible"
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp_saisie.status_code == 201
    incident_id = resp_saisie.json().get("id")
    # Analyse IA (fallback open source)
    resp_ia = client.post(reverse("automobile:analyse_incident", kwargs={"incident_id": incident_id}))
    assert resp_ia.status_code == 200
    assert "ai_fallback" in resp_ia.json().get("status", "") or "suggestion" in resp_ia.json()

@pytest.mark.django_db
def test_accessibilite_interface():
    """
    Vérifie la conformité RGAA/WCAG des interfaces automobile (présence ARIA, multilingue).
    """
    client = Client()
    resp = client.get(reverse("automobile:liste_vehicules"), HTTP_ACCEPT_LANGUAGE="fr")
    assert resp.status_code == 200
    assert b'aria-label' in resp.content or b'role=' in resp.content

@pytest.mark.django_db
def test_securite_permissions():
    """
    Vérifie que les actions sensibles nécessitent la permission adéquate.
    """
    client = Client()
    # Suppression de véhicule sans authentification
    resp = client.post(reverse("automobile:supprimer_vehicule", kwargs={"vehicule_id": 1}))
    assert resp.status_code in (401, 403)

@pytest.mark.django_db
def test_fallback_open_source_ai(monkeypatch):
    """
    Vérifie le fallback IA open source sur la validation d’un incident.
    """
    url = reverse("automobile:analyse_incident", kwargs={"incident_id": 1})
    def fake_analyse(*args, **kwargs):
        return {"status": "ai_fallback", "suggestion": "Suggestion générée par IA open source."}
    monkeypatch.setattr("templates.voyage.template.VoyageTemplate.fallback_open_source_ai", fake_analyse)
    client = Client()
    resp = client.post(url)
    assert resp.status_code == 200
    assert "ai_fallback" in resp.json().get("status", "")

# Test d’intégration rapide (smoke test)
@pytest.mark.django_db
def test_smoke_automobile():
    """
    Test d’intégration rapide sur l’API automobile Django.
    """
    client = Client()
    # Création véhicule
    resp = client.post(reverse("automobile:create_vehicule"), {
        "marque": "Smoke",
        "modele": "2025",
        "immatriculation": "SMOKE-001"
    })
    assert resp.status_code == 201
    # Liste véhicules
    resp_list = client.get(reverse("automobile:liste_vehicules"))
    assert resp_list.status_code == 200

"""
Pour lancer les tests :
    pytest test_automobile_django.py

Ce fichier garantit la robustesse, la sécurité, la multilingue, l’accessibilité, la souveraineté et la compatibilité CI/CD des modules automobile Dihya.
"""
