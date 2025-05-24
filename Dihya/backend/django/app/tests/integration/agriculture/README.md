# 🧪 Dihya – Tests d’Intégration Agriculture

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules agricoles de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées à l’agriculture intelligente, durable et souveraine.

---

## 🚀 Ce qui est testé

- **Gestion des exploitations** : création, suivi, modification, suppression, rôles (agriculteur, coopérative, auditeur…)
- **Suivi des cultures et élevages** : saisie, analyse, notifications, alertes IA open source
- **Interopérabilité** : API REST/GraphQL, échanges inter-plateformes souveraines, IoT agricole
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/agri
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration capteurs IoT

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_exploitation():
    client = Client()
    response = client.post(reverse("agriculture:create_exploitation"), {
        "nom": "Ferme Demo",
        "type": "biologique",
        "superficie": 42
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
        resp = client.post(reverse("agriculture:create_exploitation"), {
            "nom": "Test",
            "type": "bio",
            "superficie": 1
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests agriculture, sécurité, accessibilité
- **English**: Agriculture tests, security, accessibility
- **العربية**: اختبارات الزراعة، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_exploitations.py` : tests gestion des exploitations, rôles, sécurité
- `test_cultures.py` : tests suivi des cultures, notifications, IA
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules agricoles de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
