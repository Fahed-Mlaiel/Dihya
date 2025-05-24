# 🧪 Dihya – Tests d’Intégration E-commerce

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules e-commerce de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités de vente en ligne, gestion de catalogue, paiement, logistique et expérience utilisateur.

---

## 🚀 Ce qui est testé

- **Gestion du catalogue produits** : création, modification, suppression, rôles (vendeur, gestionnaire, auditeur…)
- **Commandes et paiements** : panier, validation, paiement, notifications, audit, conformité DSP2/PCI-DSS
- **Interopérabilité** : API REST/GraphQL, intégration marketplaces, ERP, plateformes souveraines
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/e-commerce, gestion MFA/2FA
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, recommandation produits automatisée
- **Compatibilité** : web, mobile, PWA, intégration IoT, logistique, paiement mobile

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_produit_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("ecommerce:create_produit"), {
            "nom": "Produit Test",
            "prix": 99.99,
            "stock": 10
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")

@pytest.mark.django_db
def test_commande_et_paiement():
    client = Client()
    # Création produit pour commande
    resp_prod = client.post(reverse("ecommerce:create_produit"), {
        "nom": "Produit Commande",
        "prix": 49.99,
        "stock": 5
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp_prod.status_code == 201
    produit_id = resp_prod.json().get("id")
    # Création commande
    resp_cmd = client.post(reverse("ecommerce:create_commande"), {
        "produit_id": produit_id,
        "quantite": 2,
        "client": "Testeur"
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp_cmd.status_code == 201
    commande_id = resp_cmd.json().get("id")
    # Paiement
    resp_pay = client.post(reverse("ecommerce:payer_commande", kwargs={"commande_id": commande_id}), {
        "methode": "carte",
        "details": "4111111111111111"
    })
    assert resp_pay.status_code == 200
    assert "payée" in resp_pay.json().get("message", "") or "paid" in resp_pay.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests e-commerce, sécurité, accessibilité
- **English**: E-commerce tests, security, accessibility
- **العربية**: اختبارات التجارة الإلكترونية، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_produits.py` : tests gestion des produits, rôles, sécurité
- `test_commandes.py` : tests commandes, paiements, notifications, audit
- `test_accessibility.py` : tests accessibilité, multilingue, RGAA/WCAG
- `test_security.py` : tests permissions, audit, conformité RGPD/PCI-DSS

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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules e-commerce de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
