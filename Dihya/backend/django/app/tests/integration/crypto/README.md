# 🧪 Dihya – Tests d’Intégration Crypto

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules crypto de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités cryptographiques (chiffrement, signatures, gestion de clés, wallets, paiements…).

---

## 🚀 Ce qui est testé

- **Gestion des clés et wallets** : création, import/export, rotation, rôles (utilisateur, admin, auditeur…)
- **Transactions et paiements cryptos** : envoi, réception, audit, notifications, conformité KYC/AML
- **Interopérabilité** : API REST/GraphQL, intégration exchanges souverains, bridges multi-crypto
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/crypto, gestion MFA/2FA
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, détection de fraude automatisée
- **Compatibilité** : web, mobile, PWA, intégration wallets, cold storage, hardware wallets

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_wallet_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créé"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("crypto:create_wallet"), {
            "utilisateur": "Testeur",
            "type": "bitcoin"
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")

@pytest.mark.django_db
def test_transaction_crypto():
    client = Client()
    resp = client.post(reverse("crypto:envoyer_crypto"), {
        "wallet_id": 1,
        "to": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        "montant": 0.01
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp.status_code == 201
    assert "envoyée" in resp.json().get("message", "") or "sent" in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests crypto, sécurité, accessibilité
- **English**: Crypto tests, security, accessibility
- **العربية**: اختبارات التشفير، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_wallets.py` : tests gestion des wallets, rôles, sécurité
- `test_transactions.py` : tests envoi/réception crypto, audit, notifications
- `test_accessibility.py` : tests accessibilité, multilingue, RGAA/WCAG
- `test_security.py` : tests permissions, audit, conformité RGPD/KYC/AML

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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules crypto de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
