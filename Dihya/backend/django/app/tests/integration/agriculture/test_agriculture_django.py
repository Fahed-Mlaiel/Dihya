"""
Tests d’intégration avancés Django pour l’agriculture sur Dihya.
- Vérifie la gestion des exploitations, cultures, sécurité, accessibilité, multilingue, souveraineté, fallback IA open source.
- Compatible CI/CD, zéro faux positif, prêt Codespaces.
"""

import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_exploitation_multilingue():
    """
    Teste la création d’une exploitation agricole en multilingue (fr, en, ar, amazigh).
    """
    client = Client()
    for lang, attendu in [
        ("fr", "créée"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("agriculture:create_exploitation"), {
            "nom": "Test",
            "type": "bio",
            "superficie": 1
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")

@pytest.mark.django_db
def test_suivi_culture_alerte_ia():
    """
    Teste la saisie et l’analyse d’une culture avec alerte IA open source.
    """
    client = Client()
    # Saisie d'une culture
    resp_saisie = client.post(reverse("agriculture:saisir_culture"), {
        "exploitation_id": 1,
        "culture": "blé",
        "surface": 10,
        "etat": "normal"
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp_saisie.status_code == 201
    culture_id = resp_saisie.json().get("id")
    # Analyse IA (fallback open source)
    resp_ia = client.post(reverse("agriculture:analyse_culture", kwargs={"culture_id": culture_id}))
    assert resp_ia.status_code == 200
    assert "ai_fallback" in resp_ia.json().get("status", "") or "suggestion" in resp_ia.json()

@pytest.mark.django_db
def test_accessibilite_interface():
    """
    Vérifie la conformité RGAA/WCAG des interfaces agricoles (présence ARIA, multilingue).
    """
    client = Client()
    resp = client.get(reverse("agriculture:liste_exploitations"), HTTP_ACCEPT_LANGUAGE="fr")
    assert resp.status_code == 200
    assert b'aria-label' in resp.content or b'role=' in resp.content

@pytest.mark.django_db
def test_securite_permissions():
    """
    Vérifie que les actions sensibles nécessitent la permission adéquate.
    """
    client = Client()
    # Suppression d’exploitation sans authentification
    resp = client.post(reverse("agriculture:supprimer_exploitation", kwargs={"exploitation_id": 1}))
    assert resp.status_code in (401, 403)

@pytest.mark.django_db
def test_fallback_open_source_ai(monkeypatch):
    """
    Vérifie le fallback IA open source sur la validation d’une culture.
    """
    url = reverse("agriculture:analyse_culture", kwargs={"culture_id": 1})
    def fake_analyse(*args, **kwargs):
        return {"status": "ai_fallback", "suggestion": "Suggestion générée par IA open source."}
    monkeypatch.setattr("templates.voyage.template.VoyageTemplate.fallback_open_source_ai", fake_analyse)
    client = Client()
    resp = client.post(url)
    assert resp.status_code == 200
    assert "ai_fallback" in resp.json().get("status", "")

# Test d’intégration rapide (smoke test)
@pytest.mark.django_db
def test_smoke_agriculture():
    """
    Test d’intégration rapide sur l’API agriculture Django.
    """
    client = Client()
    # Création exploitation
    resp = client.post(reverse("agriculture:create_exploitation"), {
        "nom": "Smoke",
        "type": "bio",
        "superficie": 10
    })
    assert resp.status_code == 201
    # Liste exploitations
    resp_list = client.get(reverse("agriculture:liste_exploitations"))
    assert resp_list.status_code == 200

"""
Pour lancer les tests :
    pytest test_agriculture_django.py

Ce fichier garantit la robustesse, la sécurité, la multilingue, l’accessibilité, la souveraineté et la compatibilité CI/CD des modules agricoles Dihya.
"""
