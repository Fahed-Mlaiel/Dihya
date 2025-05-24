# 🧪 Dihya – Tests d’Intégration Banque & Finance

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules banque et finance de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités financières (comptes, transactions, paiements, audit…).

---

## 🚀 Ce qui est testé

- **Gestion des comptes** : création, modification, clôture, rôles (client, gestionnaire, auditeur…)
- **Transactions et paiements** : virements, paiements, notifications, audit, conformité DSP2
- **Interopérabilité** : API REST/GraphQL, intégration partenaires, open banking souverain
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/finance, SCA (authentification forte)
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, détection de fraude automatisée
- **Compatibilité** : web, mobile, PWA, intégration SI bancaire

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_compte():
    client = Client()
    response = client.post(reverse("banque:create_compte"), {
        "titulaire": "Dihya User",
        "type": "courant",
        "solde_initial": 1000
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
        resp = client.post(reverse("banque:create_compte"), {
            "titulaire": "Test",
            "type": "épargne",
            "solde_initial": 10
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests banque & finance, sécurité, accessibilité
- **English**: Banking & finance tests, security, accessibility
- **العربية**: اختبارات البنوك والمالية، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_comptes.py` : tests gestion des comptes, rôles, sécurité
- `test_transactions.py` : tests virements, paiements, notifications, audit
- `test_accessibility.py` : tests accessibilité, multilingue, RGAA/WCAG
- `test_security.py` : tests permissions, audit, conformité RGPD/DSP2

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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules banque & finance de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
