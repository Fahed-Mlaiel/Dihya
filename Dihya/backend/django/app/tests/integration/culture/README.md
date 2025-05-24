# 🧪 Dihya – Tests d’Intégration Culture

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules culture de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées à la culture, au patrimoine, à l’événementiel et à la médiation culturelle.

---

## 🚀 Ce qui est testé

- **Gestion des événements et contenus culturels** : création, modification, publication, rôles (organisateur, médiateur, visiteur…)
- **Catalogue d’œuvres, expositions, festivals** : ajout, édition, suppression, recommandations IA open source
- **Interopérabilité** : API REST/GraphQL, intégration partenaires, plateformes souveraines, open data culturel
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/culture
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration IoT, dispositifs muséographiques

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_evenement_multilingue():
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
def test_accessibilite_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("culture:create_evenement"), {
            "titre": "Test",
            "date": "2025-07-01",
            "lieu": "TestVille"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests culture, sécurité, accessibilité
- **English**: Culture tests, security, accessibility
- **العربية**: اختبارات الثقافة، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_evenements.py` : tests gestion des événements, rôles, sécurité
- `test_catalogue.py` : tests gestion des œuvres, expositions, recommandations IA
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules culture de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
