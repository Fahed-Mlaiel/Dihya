# 🧪 Dihya – Tests d’Intégration Administration Publique

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules d’administration publique sur la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités dédiées au secteur public.

---

## 🚀 Ce qui est testé

- **Gestion des usagers** : création, modification, suppression, rôles (agent, citoyen, auditeur…)
- **Traitement des démarches administratives** : dépôt, suivi, validation, notifications multicanal
- **Interopérabilité** : API REST/GraphQL, échanges inter-plateformes souveraines
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/administration
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée
- **Compatibilité** : web, mobile, PWA, intégration SI public

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_usager():
    client = Client()
    response = client.post(reverse("admin_publique:create_usager"), {
        "nom": "Dupont",
        "prenom": "Alice",
        "email": "alice@exemple.fr"
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
        resp = client.post(reverse("admin_publique:create_usager"), {
            "nom": "Test",
            "prenom": "Test",
            "email": f"test_{lang}@exemple.fr"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests administration publique, sécurité, accessibilité
- **English**: Public administration tests, security, accessibility
- **العربية**: اختبارات الإدارة العمومية، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_usagers.py` : tests gestion des usagers, rôles, sécurité
- `test_demandes.py` : tests démarches, workflow, notifications
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules d’administration publique de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
