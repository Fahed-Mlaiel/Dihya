# Voyage API routes

Ce module expose des routes REST et GraphQL pour la gestion des voyages (planification, réservation, IA, etc.)

- Sécurité maximale (CORS, JWT, WAF, audit, anti-DDOS)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Support plugins IA (LLaMA, Mixtral, Mistral, fallback open source)
- Multitenant, gestion des rôles (admin, user, invité)
- Documentation OpenAPI intégrée
- Exemples d'appels API et GraphQL
- Prêt pour production, CI/CD, Docker, K8s, Codespaces

## Exemples d'utilisation

### REST
POST /api/voyage/plan

### GraphQL
POST /api/voyage/graphql

## Sécurité
- JWT obligatoire
- Audit log
- WAF, anti-abus

## Extensibilité
- Ajout de plugins voyage via API/CLI

## Tests
- Couverture unitaire, intégration, e2e

## Multilingue
- Toutes les réponses sont localisées dynamiquement

---

# Voyage API routes

This module exposes REST and GraphQL routes for travel management (planning, booking, AI, etc.)

- Maximum security (CORS, JWT, WAF, audit, anti-DDOS)
- Multilingual (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- AI plugin support (LLaMA, Mixtral, Mistral, open source fallback)
- Multitenant, role management (admin, user, guest)
- Integrated OpenAPI documentation
- API and GraphQL usage examples
- Production-ready, CI/CD, Docker, K8s, Codespaces

## Usage examples

### REST
POST /api/voyage/plan

### GraphQL
POST /api/voyage/graphql

## Security
- JWT required
- Audit log
- WAF, anti-abuse

## Extensibility
- Add travel plugins via API/CLI

## Tests
- Unit, integration, e2e coverage

## Multilingual
- All responses are dynamically localized
