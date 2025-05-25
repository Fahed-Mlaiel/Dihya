# Politique Métier BTP

## Objectif
Définir les politiques d'accès, de gestion et de conformité pour les applications BTP (REST, GraphQL, plugins, etc.).

## Rôles
- **Admin** : gestion totale, audit, export, anonymisation.
- **Chef de projet** : gestion chantiers, sécurité.
- **Ouvrier** : accès à ses chantiers, documents.
- **Invité** : accès aux offres publiques.

## Sécurité
- JWT, CORS, WAF, audit log, RGPD.
- Validation stricte (type hints, docstring, tests).

## Internationalisation
- Support dynamique : fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de routes REST/GraphQL
- `GET /api/btp/chantiers` (admin, chef de projet, ouvrier)
- `POST /api/btp/chantier` (chef de projet)
- `GET /api/btp/offers` (public)

## Plugins & Extensibilité
- IA analyse sécurité, scoring, gestion planning.
- Système de plugins métiers (API/CLI).

## RGPD & Auditabilité
- Export, anonymisation, logs structurés, accès exportable.

## Tests
- Couverture unitaire, intégration, e2e, mocks, fixtures.

## Documentation
- Docstring, exemples, guides multilingues, conformité CI/CD.
