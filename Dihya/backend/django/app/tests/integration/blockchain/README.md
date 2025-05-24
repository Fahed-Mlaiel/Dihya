# 🧪 Dihya – Tests d’Intégration Blockchain

---

## 🇫🇷 Présentation

Ce dossier regroupe les **tests d’intégration avancés** pour les modules blockchain de la plateforme Dihya.
Il garantit la robustesse, la sécurité, la conformité réglementaire, l’accessibilité et la souveraineté numérique des fonctionnalités blockchain (transactions, smart contracts, NFT, identité décentralisée…).

---

## 🚀 Ce qui est testé

- **Gestion des transactions** : création, validation, audit, rôles (utilisateur, validateur, auditeur…)
- **Déploiement et interaction avec smart contracts** : création, appel, audit, logs
- **Interopérabilité** : API REST/GraphQL, intégration réseaux souverains, bridges multi-blockchains
- **Sécurité** : permissions, audit, chiffrement, conformité RGPD/blockchain, gestion des clés
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue (fr, en, ar, amazigh)
- **Fallback IA open source** : suggestion, validation, correction automatisée de transactions ou contrats
- **Compatibilité** : web, mobile, PWA, intégration wallets, nodes, DApps

---

## 🛠️ Exemple de test d’intégration (Pytest + Django)

```python
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_creation_transaction_multilingue():
    client = Client()
    for lang, attendu in [
        ("fr", "créée"),
        ("en", "created"),
        ("ar", "تم الإنشاء"),
        ("ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⴰⴷⴷⴰⵔⴰⵏ")
    ]:
        resp = client.post(reverse("blockchain:create_transaction"), {
            "from": "0xABCDEF",
            "to": "0x123456",
            "amount": 10
        }, HTTP_ACCEPT_LANGUAGE=lang)
        assert resp.status_code == 201
        assert attendu in resp.json().get("message", "")

@pytest.mark.django_db
def test_deploiement_smart_contract():
    client = Client()
    resp = client.post(reverse("blockchain:deploy_contract"), {
        "code": "contract Test { function hello() public {} }"
    }, HTTP_ACCEPT_LANGUAGE="fr")
    assert resp.status_code == 201
    assert "déployé" in resp.json().get("message", "") or "deployed" in resp.json().get("message", "")
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Tests blockchain, sécurité, accessibilité
- **English**: Blockchain tests, security, accessibility
- **العربية**: اختبارات البلوكشين، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵙⴻⵏⴰⵡⴰⵏ ⴷ ⵜⴰⵎⴰⵏⵜⴰⵡⴰⵏ

---

## 🧩 Structure recommandée

- `test_transactions.py` : tests gestion des transactions, rôles, sécurité
- `test_contracts.py` : tests déploiement/interactions smart contracts, audit
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

> Ces tests garantissent la robustesse, la sécurité, l’accessibilité et la souveraineté des modules blockchain de Dihya.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
