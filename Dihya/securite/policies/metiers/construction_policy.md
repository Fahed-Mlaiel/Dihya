# Politique Métier Construction

## Objectif
Définir les politiques d'accès, de gestion et de conformité pour les applications construction (REST, GraphQL, plugins, etc.).

## Rôles
- **Admin** : gestion totale, audit, export, anonymisation.
- **Chef de projet** : gestion projets, sécurité.
- **Ouvrier** : accès à ses projets, documents.
- **Invité** : accès aux offres publiques.

## Sécurité
- JWT, CORS, WAF, audit log, RGPD.
- Validation stricte (type hints, docstring, tests).

## Internationalisation
- Support dynamique : fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de routes REST/GraphQL
- `GET /api/construction/projets` (admin, chef de projet, ouvrier)
- `POST /api/construction/projet` (chef de projet)
- `GET /api/construction/offers` (public)

## Plugins & Extensibilité
- IA analyse sécurité, scoring, gestion planning.
- Système de plugins métiers (API/CLI).

## RGPD & Auditabilité
- Export, anonymisation, logs structurés, accès exportable.

## Tests
- Couverture unitaire, intégration, e2e, mocks, fixtures.

## Documentation
- Docstring, exemples, guides multilingues, conformité CI/CD.
