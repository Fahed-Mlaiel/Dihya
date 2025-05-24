# 🧪 Dihya – Tests d’Intégration BTP (Bâtiment & Travaux Publics)

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules BTP de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées au secteur du bâtiment, de la construction et des travaux publics.

---

## 🚀 Ce qui est testé

- **Gestion des chantiers** : création, modification, suivi, clôture, rôles (maître d’ouvrage, chef de chantier, ouvrier, auditeur…)
- **Suivi des interventions et incidents** : saisie, analyse, notifications, alertes IA open source
- **Interopérabilité** : API REST/GraphQL, intégration partenaires, plateformes souveraines, IoT BTP
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/BTP
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration capteurs IoT, BIM, SIG

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_chantier_multilingue():
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
def test_accessibilite_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("btp:create_chantier"), {
            "nom": "Test",
            "adresse": "Rue Test",
            "date_debut": "2025-06-01"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests BTP, sécurité, accessibilité
- **English**: Construction tests, security, accessibility
- **العربية**: اختبارات البناء والأشغال، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_chantiers.py` : tests gestion des chantiers, rôles, sécurité
- `test_interventions.py` : tests interventions, incidents, notifications, IA
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules BTP de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
