# 🧪 Dihya – Tests d’Intégration Beauté & Bien-être

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules beauté et bien-être de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées à la beauté, au bien-être, à la cosmétique et à la santé holistique.

---

## 🚀 Ce qui est testé

- **Gestion des clients et rendez-vous** : création, modification, annulation, rôles (client, praticien, gestionnaire…)
- **Catalogue de soins et produits** : ajout, édition, suppression, recommandations IA open source
- **Interopérabilité** : API REST/GraphQL, intégration partenaires, plateformes souveraines
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/santé
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration IoT bien-être

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_rdv_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("beaute:create_rdv"), {
            "client": "Testeur",
            "date": "2025-06-01T10:00:00Z",
            "prestation": "Massage"
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
        resp = client.post(reverse("beaute:create_rdv"), {
            "client": "Testeur",
            "date": "2025-06-01T10:00:00Z",
            "prestation": "Soin visage"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests beauté & bien-être, sécurité, accessibilité
- **English**: Beauty & wellness tests, security, accessibility
- **العربية**: اختبارات الجمال والعافية، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_rdv.py` : tests gestion des rendez-vous, rôles, sécurité
- `test_catalogue.py` : tests gestion des soins/produits, recommandations IA
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules beauté & bien-être de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)

