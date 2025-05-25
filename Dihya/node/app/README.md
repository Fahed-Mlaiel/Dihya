# Dossier `app` – Backend Node.js Dihya

## Objectif
Contient l’application principale Node.js : routes métiers, middlewares, gestion multitenancy, plugins, génération automatique, audit, RGPD, accessibilité, SEO, multilingue.

- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, audit, anonymisation RGPD)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Plugins métiers, fallback IA open source (LLaMA, Mixtral, Mistral)
- Auditabilité, logs structurés, export RGPD
- API RESTful + GraphQL, multitenancy, gestion des rôles (admin, user, invité)
- Extensible via API ou CLI (ajout de modules, plugins, middlewares)
- Tests unitaires, intégration, e2e, mocks, fixtures
- CI/CD GitHub Actions, Docker, Codespaces
- Accessibilité, SEO backend

## Structure
- `routes/` : routes métiers (services_personne, social, sport, tourisme, transport, utils, validators, voice, voyage, etc.)
- `middlewares/` : sécurité, validation, audit, i18n, plugins, RGPD
- `plugins/` : plugins métiers, extensions, fallback IA
- `templates/` : templates métiers, configs, assets, docs, tests
- `graphql/` : schémas, resolvers, sécurité, i18n, plugins
- `utils/` : helpers, validation, sécurité, i18n, audit

## Exemples d’utilisation

### API REST
```http
GET /api/services_personne
Authorization: Bearer <jwt>
Accept-Language: fr
```

### GraphQL
```graphql
query {
  servicesPersonne(lang: "en") {
    id
    name
    type
  }
}
```

## Plugins & Extensions
- Ajout dynamique de modules métiers, middlewares, plugins via API/CLI
- Support de plugins métiers, fallback IA open source

## Audit & RGPD
- Logs structurés, anonymisation, export CSV/JSON
- Suppression/anonymisation sur demande utilisateur

## Accessibilité & SEO
- Conformité accessibilité (API, docs, logs)
- SEO backend (robots, sitemap, logs)

## CI/CD & Déploiement
- Compatible GitHub Actions, Docker, K8s, Codespaces
- Aucun warning, fail CI/lint/test/build/doc/accessibilité/sécurité/SEO

## Documentation intégrée
- Docstring, type hints, guides multilingues, exemples API/CLI
- Prêt à l’emploi, production, démo, contribution

---

# Dihya Node App – English

*See French section above for full details. All features are multilingual, secure, RGPD-compliant, plugin-ready, CI/CD, accessible, SEO-optimized, extensible.*
