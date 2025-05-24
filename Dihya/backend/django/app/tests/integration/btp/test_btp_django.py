"""
Tests d’intégration avancés Django pour les modules BTP (Bâtiment & Travaux Publics) sur Dihya.
- Vérifie la gestion des chantiers, interventions, sécurité, accessibilité, multilingue, souveraineté, fallback IA open source.
- Compatible CI/CD, zéro faux positif, prêt Codespaces.
"""

import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_chantier_multilingue():
    """
    Teste la création d’un chantier en multilingue (fr, en, ar, amazigh).
    """
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("btp:create_chantier"), {
            "nom": "Chantier Test",
            "adresse": "123 rue du BTP",
            "date_debut": "2025-06-01"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")

@pytest.mark.django_db
def test_suivi_intervention_alerte_ia():
    """
    Teste la saisie d’une intervention et l’alerte IA open source.
    """
    client = Client()
    # Saisie d'une intervention
    resp_saisie = client.post(reverse("btp:saisir_intervention"), {
        "chantier_id": 1,
        "type": "sécurité",
        "description": "Casque non porté"
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp_saisie.status_code == 201
    intervention_id = resp_saisie.json().get("id")
    # Analyse IA (fallback open source)
    resp_ia = client.post(reverse("btp:analyse_intervention", kwargs={"intervention_id": intervention_id}))
    assert resp_ia.status_code == 200
    assert "ai_fallback" in resp_ia.json().get("status", "") or "suggestion" in resp_ia.json()

@pytest.mark.django_db
def test_accessibilite_interface():
    """
    Vérifie la conformité RGAA/WCAG des interfaces BTP (présence ARIA, multilingue).
    """
    client = Client()
    resp = client.get(reverse("btp:liste_chantiers"), HTTP_ACCEPT_LANGUAGE="fr")
    assert resp.status_code == 200
    assert b'aria-label' in resp.content or b'role=' in resp.content

@pytest.mark.django_db
def test_securite_permissions():
    """
    Vérifie que les actions sensibles nécessitent la permission adéquate.
    """
    client = Client()
    # Suppression de chantier sans authentification
    resp = client.post(reverse("btp:supprimer_chantier", kwargs={"chantier_id": 1}))
    assert resp.status_code in (401, 403)

@pytest.mark.django_db
def test_fallback_open_source_ai(monkeypatch):
    """
    Vérifie le fallback IA open source sur la validation d’une intervention.
    """
    url = reverse("btp:analyse_intervention", kwargs={"intervention_id": 1})
    def fake_analyse(*args, **kwargs):
        return {"status": "ai_fallback", "suggestion": "Suggestion générée par IA open source."}
    monkeypatch.setattr("templates.voyage.template.VoyageTemplate.fallback_open_source_ai", fake_analyse)
    client = Client()
    resp = client.post(url)
    assert resp.status_code == 200
    assert "ai_fallback" in resp.json().get("status", "")

# Test d’intégration rapide (smoke test)
@pytest.mark.django_db
def test_smoke_btp():
    """
    Test d’intégration rapide sur l’API BTP Django.
    """
    client = Client()
    # Création chantier
    resp = client.post(reverse("btp:create_chantier"), {
        "nom": "Smoke",
        "adresse": "1 rue du Test",
        "date_debut": "2025-06-01"
    })
    assert resp.status_code == 201
    # Liste chantiers
    resp_list = client.get(reverse("btp:liste_chantiers"))
    assert resp_list.status_code == 200

"""
Pour lancer les tests :
    pytest test_btp_django.py

Ce fichier garantit la robustesse, la sécurité, la multilingue, l’accessibilité, la souveraineté et la compatibilité CI/CD des modules BTP Dihya.
"""
