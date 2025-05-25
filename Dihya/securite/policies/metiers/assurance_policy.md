# Politique Métier Assurance

## Objectif
Définir les politiques d'accès, de gestion et de conformité pour les applications d'assurance (REST, GraphQL, plugins, etc.).

## Rôles
- **Admin** : gestion complète, audit, export, anonymisation.
- **User** : gestion de ses contrats, sinistres, documents.
- **Invité** : accès aux offres publiques, simulateurs.

## Sécurité
- JWT obligatoire, CORS, WAF, anti-DDOS, audit log, RGPD.
- Validation stricte des entrées (type hints, docstring, tests).

## Internationalisation
- Support dynamique : fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de routes REST/GraphQL
- `GET /api/assurance/contracts` (admin, user)
- `POST /api/assurance/claim` (user)
- `GET /api/assurance/offers` (public)

## Plugins & Extensibilité
- Ajout de modules IA (LLaMA, Mistral, Mixtral) pour scoring, détection fraude.
- Système de plugins métiers (API/CLI).

## RGPD & Auditabilité
- Export, anonymisation, logs structurés, accès exportable.

## Tests
- Couverture unitaire, intégration, e2e, mocks, fixtures.

## Documentation
- Docstring, exemples, guides multilingues, conformité CI/CD.
