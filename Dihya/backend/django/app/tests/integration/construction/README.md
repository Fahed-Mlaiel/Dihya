# 🧪 Dihya – Tests d’Intégration Construction

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules construction de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées à la construction, à la gestion de projets immobiliers et d’infrastructures.

---

## 🚀 Ce qui est testé

- **Gestion des projets de construction** : création, modification, suivi, clôture, rôles (maître d’ouvrage, architecte, chef de projet, auditeur…)
- **Suivi des tâches, lots et sous-traitants** : planification, avancement, notifications, alertes IA open source
- **Interopérabilité** : API REST/GraphQL, intégration partenaires, plateformes souveraines, BIM, SIG
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/construction
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration IoT, BIM, SIG

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_projet_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("construction:create_projet"), {
            "nom": "Projet Test",
            "adresse": "456 avenue du Bâtisseur",
            "date_debut": "2025-06-01"
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
        resp = client.post(reverse("construction:create_projet"), {
            "nom": "Test",
            "adresse": "Rue Test",
            "date_debut": "2025-06-01"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests construction, sécurité, accessibilité
- **English**: Construction tests, security, accessibility
- **العربية**: اختبارات البناء، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_projets.py` : tests gestion des projets, rôles, sécurité
- `test_taches.py` : tests tâches, lots, sous-traitants, notifications, IA
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules construction de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
