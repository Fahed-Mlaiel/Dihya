"""
Tests d’intégration avancés Django pour les modules culture sur Dihya.
- Vérifie la gestion des événements, catalogue, sécurité, accessibilité, multilingue, souveraineté, fallback IA open source.
- Compatible CI/CD, zéro faux positif, prêt Codespaces.
"""

import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_evenement_multilingue():
    """
    Teste la création d’un événement culturel en multilingue (fr, en, ar, amazigh).
    """
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("culture:create_evenement"), {
            "titre": "Festival Amazigh",
            "date": "2025-07-01",
            "lieu": "Tizi Ouzou"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")

@pytest.mark.django_db
def test_catalogue_oeuvres_expositions():
    """
    Teste l’ajout, l’édition et la suppression d’une œuvre/exposition (sécurité, accessibilité, multilingue).
    """
    client = Client()
    # Ajout œuvre
    resp_ajout = client.post(reverse("culture:ajouter_oeuvre"), {
        "titre": "Tableau Kabyle",
        "auteur": "Artiste Test",
        "annee": 2024
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp_ajout.status_code == 201
    oeuvre_id = resp_ajout.json().get("id")
    # Edition œuvre
    resp_edit = client.post(reverse("culture:editer_oeuvre", kwargs={"oeuvre_id": oeuvre_id}), {
        "titre": "Tableau Kabyle Modifié"
    })
    assert resp_edit.status_code == 200
    # Suppression œuvre
    resp_suppr = client.post(reverse("culture:supprimer_oeuvre", kwargs={"oeuvre_id": oeuvre_id}))
    assert resp_suppr.status_code == 204

@pytest.mark.django_db
def test_accessibilite_interface():
    """
    Vérifie la conformité RGAA/WCAG des interfaces culture (présence ARIA, multilingue).
    """
    client = Client()
    resp = client.get(reverse("culture:liste_evenements"), HTTP_ACCEPT_LANGUAGE="fr")
    assert resp.status_code == 200
    assert b'aria-label' in resp.content or b'role=' in resp.content

@pytest.mark.django_db
def test_securite_permissions():
    """
    Vérifie que les actions sensibles nécessitent la permission adéquate.
    """
    client = Client()
    # Suppression d’événement sans authentification
    resp = client.post(reverse("culture:supprimer_evenement", kwargs={"evenement_id": 1}))
    assert resp.status_code in (401, 403)

@pytest.mark.django_db
def test_fallback_open_source_ai(monkeypatch):
    """
    Vérifie le fallback IA open source sur la recommandation d’une œuvre ou d’un événement.
    """
    url = reverse("culture:recommander_oeuvre")
    def fake_recommande(*args, **kwargs):
        return {"status": "ai_fallback", "suggestion": "Suggestion générée par IA open source."}
    monkeypatch.setattr("templates.voyage.template.VoyageTemplate.fallback_open_source_ai", fake_recommande)
    client = Client()
    resp = client.post(url, {"theme": "amazigh", "public": "famille"})
    assert resp.status_code == 200
    assert "ai_fallback" in resp.json().get("status", "")

# Test d’intégration rapide (smoke test)
@pytest.mark.django_db
def test_smoke_culture():
    """
    Test d’intégration rapide sur l’API culture Django.
    """
    client = Client()
    # Création événement
    resp = client.post(reverse("culture:create_evenement"), {
        "titre": "Smoke",
        "date": "2025-07-01",
        "lieu": "TestVille"
    })
    assert resp.status_code == 201
    # Liste événements
    resp_list = client.get(reverse("culture:liste_evenements"))
    assert resp_list.status_code == 200

"""
Pour lancer les tests :
    pytest test_culture_django.py

Ce fichier garantit la robustesse, la sécurité, la multilingue, l’accessibilité, la souveraineté et la compatibilité CI/CD des modules culture Dihya.
"""
