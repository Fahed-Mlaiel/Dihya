# Politique Métier Crypto

## Objectif
Définir les politiques d'accès, de gestion et de conformité pour les applications crypto (REST, GraphQL, plugins, etc.).

## Rôles
- **Admin** : gestion totale, audit, export, anonymisation.
- **Trader** : gestion wallets, transactions.
- **Utilisateur** : accès à ses wallets, transactions.
- **Invité** : accès aux offres publiques.

## Sécurité
- JWT, CORS, WAF, audit log, RGPD.
- Validation stricte (type hints, docstring, tests).

## Internationalisation
- Support dynamique : fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de routes REST/GraphQL
- `GET /api/crypto/wallets` (admin, trader, utilisateur)
- `POST /api/crypto/transaction` (trader, utilisateur)
- `GET /api/crypto/offers` (public)

## Plugins & Extensibilité
- IA analyse transactions, scoring, détection fraude.
- Système de plugins métiers (API/CLI).

## RGPD & Auditabilité
- Export, anonymisation, logs structurés, accès exportable.

## Tests
- Couverture unitaire, intégration, e2e, mocks, fixtures.

## Documentation
- Docstring, exemples, guides multilingues, conformité CI/CD.
