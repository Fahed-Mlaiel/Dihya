# API Routes – 3D, VR, AR, IA

## RESTful Endpoints

### Sécurité maximale (CORS, JWT, WAF, audit, RGPD)

- `GET    /api/3d/projects` – Liste des projets 3D (auth, rôles, i18n)
- `POST   /api/3d/projects` – Créer un projet 3D (admin, validation, audit)
- `GET    /api/3d/projects/:id` – Détail projet (auth, rôles)
- `PUT    /api/3d/projects/:id` – Modifier projet (admin, audit)
- `DELETE /api/3d/projects/:id` – Supprimer projet (admin, audit, anonymisation RGPD)
- `POST   /api/3d/projects/:id/export` – Export multi-format (auth, audit)
- `POST   /api/3d/projects/:id/collaborators` – Gestion des droits (admin, audit)
- `POST   /api/3d/generate` – Génération IA de scènes/scripts (auth, audit, fallback LLaMA/Mixtral/Mistral)

## GraphQL
- `/graphql` – Support complet, schéma extensible, sécurité, rôles, i18n

## Plugins
- `POST /api/plugins/install` – Installer plugin 3D/IA/VR/AR (admin, audit)
- `GET  /api/plugins` – Lister plugins actifs

## Internationalisation
- Tous les endpoints supportent `Accept-Language` (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)

## Exemples de requêtes
```http
GET /api/3d/projects
Accept-Language: fr
Authorization: Bearer <JWT>
```

## Sécurité & RGPD
- JWT, CORS, WAF, audit, anonymisation, logs structurés
- Export des données, suppression/anonymisation sur demande

---
*Routes prêtes à l’emploi, multilingues, sécurisées, extensibles, auditées.*
