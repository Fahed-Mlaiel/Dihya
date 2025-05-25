# Politique Métier Beauté

## Objectif
Définir les politiques d'accès, de gestion et de conformité pour les applications beauté (REST, GraphQL, plugins, etc.).

## Rôles
- **Admin** : gestion totale, audit, export, anonymisation.
- **Pro** : gestion salons, réservations, clients.
- **Client** : accès à ses réservations, historique.
- **Invité** : accès aux offres publiques.

## Sécurité
- JWT, CORS, WAF, audit log, RGPD.
- Validation stricte (type hints, docstring, tests).

## Internationalisation
- Support dynamique : fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.

## Exemples de routes REST/GraphQL
- `GET /api/beaute/salons` (admin, pro, client)
- `POST /api/beaute/reservation` (pro, client)
- `GET /api/beaute/offers` (public)

## Plugins & Extensibilité
- IA recommandation, scoring, analyse satisfaction.
- Système de plugins métiers (API/CLI).

## RGPD & Auditabilité
- Export, anonymisation, logs structurés, accès exportable.

## Tests
- Couverture unitaire, intégration, e2e, mocks, fixtures.

## Documentation
- Docstring, exemples, guides multilingues, conformité CI/CD.
