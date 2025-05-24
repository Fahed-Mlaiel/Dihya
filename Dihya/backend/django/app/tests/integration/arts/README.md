# 🧪 Dihya – Tests d’Intégration Arts

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules artistiques de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées aux arts (visuels, sonores, interactifs, IA générative…).

---

## 🚀 Ce qui est testé

- **Gestion des œuvres** : création, import/export, édition, suppression, rôles (artiste, curateur, visiteur, auditeur…)
- **Interopérabilité** : API REST/GraphQL, intégration galeries, plateformes souveraines, NFT open source
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/arts
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh), fallback audio/texte
- **Fallback IA open source** : suggestion, validation, correction automatisée d’œuvres ou de métadonnées
- **Compatibilité** : web, mobile, PWA, VR/AR, intégration moteurs 3D/2D

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_oeuvre():
    client = Client()
    response = client.post(reverse("arts:create_oeuvre"), {
        "titre": "Tableau Demo",
        "type": "peinture",
        "artiste": "A. Dihya"
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert response.status_code == 201
    assert "créée" in response.json().get("message", "")

@pytest.mark.django_db
def test_accessibilite_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créée"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("arts:create_oeuvre"), {
            "titre": "Test",
            "type": "photo",
            "artiste": "Testeur"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests arts, sécurité, accessibilité
- **English**: Arts tests, security, accessibility
- **العربية**: اختبارات الفنون، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_oeuvres.py` : tests gestion des œuvres, rôles, sécurité
- `test_interoperabilite.py` : tests API, intégration plateformes, NFT
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules artistiques de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
