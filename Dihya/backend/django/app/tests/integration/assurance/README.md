# 🧪 Dihya – Tests d’Intégration Assurance

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules d’assurance de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées à l’assurance (contrats, sinistres, gestion des assurés…).

---

## 🚀 Ce qui est testé

- **Gestion des contrats** : création, modification, résiliation, rôles (assuré, gestionnaire, auditeur…)
- **Déclaration et suivi des sinistres** : dépôt, traitement, notifications, audit
- **Interopérabilité** : API REST/GraphQL, échanges inter-plateformes souveraines, intégration partenaires
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/assurance
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration SI assurance

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_contrat():
    client = Client()
    response = client.post(reverse("assurance:create_contrat"), {
        "assure": "Dupont",
        "type": "auto",
        "montant": 1200
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
        resp = client.post(reverse("assurance:create_contrat"), {
            "assure": "Test",
            "type": "santé",
            "montant": 100
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests assurance, sécurité, accessibilité
- **English**: Insurance tests, security, accessibility
- **العربية**: اختبارات التأمين، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_contrats.py` : tests gestion des contrats, rôles, sécurité
- `test_sinistres.py` : tests déclaration/suivi sinistres, notifications, audit
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules assurance de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
