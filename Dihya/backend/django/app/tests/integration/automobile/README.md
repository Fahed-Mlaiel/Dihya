# 🧪 Dihya – Tests d’Intégration Automobile

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules automobile de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées à la mobilité intelligente, connectée et souveraine.

---

## 🚀 Ce qui est testé

- **Gestion du parc automobile** : création, modification, suppression, rôles (conducteur, gestionnaire, auditeur…)
- **Suivi des véhicules** : maintenance, incidents, notifications, alertes IA open source
- **Interopérabilité** : API REST/GraphQL, échanges inter-plateformes souveraines, IoT automobile
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/automobile
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration capteurs IoT, systèmes embarqués

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_vehicule():
    client = Client()
    response = client.post(reverse("automobile:create_vehicule"), {
        "marque": "DihyaCar",
        "modele": "2025",
        "immatriculation": "AB-123-CD"
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert response.status_code == 201
    assert "créé" in response.json().get("message", "")

@pytest.mark.django_db
def test_accessibilite_multilingue():
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
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests automobile, sécurité, accessibilité
- **English**: Automobile tests, security, accessibility
- **العربية**: اختبارات السيارات، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_vehicules.py` : tests gestion des véhicules, rôles, sécurité
- `test_maintenance.py` : tests suivi maintenance, notifications, IA
- `test_accessibility.py` : tests accessibilité, multilingue, RGAA/WCAG
- `test_security.py` : tests permissions, audit, conformité RGPD

---

## 🧪 Lancer les tests

```bash
pytest .
```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules automobile de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
