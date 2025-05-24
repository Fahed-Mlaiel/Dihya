# 📚 Exemples d’intégration – Dihya

Ce fichier centralise des exemples d’intégration backend, frontend, API, CLI, Node, Django, GraphQL, SEO, I18N, RBAC, Monitoring, Marketplace, Plugins, Fallback pour chaque stack et dossier métier du projet.

## Backend (Django, Flask, Node.js)
- Django : `python3 manage.py runserver` + intégration API REST/GraphQL
- Flask : `python3 app.py` + endpoints sécurisés JWT, RBAC, RGPD
- Node.js : `node index.js` + plugins, audit, export RGPD, fallback

## Frontend (React, Next.js, Vue)
- React : `npm start` + intégration API sécurisée, i18n, SEO, accessibilité
- Next.js : `npm run build && npm start` + SSR, SEO, RGPD, monitoring

## API/CLI
- Appel API : `curl -H "Authorization: Bearer <token>" https://api.dihya.com/endpoint`
- CLI : `python3 cli.py --export-rgpd` ou `node cli.js --audit`

## GraphQL
- Query : `query { user(id: 1) { name, email } }`
- Mutation : `mutation { updateUser(id: 1, input: {email: "x@x.com"}) { id } }`

## SEO
- Balises meta dynamiques, sitemap.xml, robots.txt, audit Lighthouse

## I18N
- Fichiers de traduction, LanguageSwitcher, fallback multilingue

## RBAC
- Gestion des rôles, permissions, endpoints sécurisés, tests RBAC

## Monitoring
- Intégration Prometheus/Grafana, logs, alertes, dashboards

## Marketplace/Plugins
- Ajout de plugins : `node plugin.js --install analytics`
- Publication marketplace : `python3 publish.py --marketplace`

## Fallback
- Fallback IA open source : `python3 fallback.py` ou `node fallback.js`

## Bonnes pratiques
- Toujours valider la conformité RGPD, accessibilité, auditabilité, modularité, extensibilité, souveraineté numérique pour chaque intégration.
