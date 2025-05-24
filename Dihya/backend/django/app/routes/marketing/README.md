# 📈 Dihya – Django Marketing API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/marketing`](#rôle-du-dossier-routesmarketing)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API marketing](#exemples-dapi-marketing)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 📈 Rôle du dossier `routes/marketing`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’automatisation et l’innovation marketing via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration CRM, cloud souverain, IA marketing, automation, analytics
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST marketing** : gestion des campagnes, leads, audiences, canaux, contenus, analytics, IA marketing, A/B testing, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, marketeur, analyste, client, auditeur, guest)
- **Traçabilité et logs** : audit des accès, campagnes, modifications, suppressions, exports
- **Interopérabilité** : intégration avec CRM, plateformes emailing, réseaux sociaux, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, scoring, segmentation dynamique
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
marketing/
├── views.py           # Vues Django REST pour campagnes, leads, audiences, canaux, contenus, analytics, rapports
├── serializers.py     # Serializers pour campagnes, leads, audiences, canaux, contenus, analytics, rapports
├── urls.py            # Routage des endpoints marketing
├── permissions.py     # Permissions RBAC pour l’accès aux services marketing
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, scoring)
├── assets/            # Exemples de campagnes, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API marketing
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, marketeur, analyste, client, guest)
- **Logs d’accès** et d’opérations critiques (création, campagne, suppression)
- **Chiffrement** des données sensibles (leads, audiences, analytics)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque campagne ou asset marketing

---

## 🛠️ Exemples d’API marketing

### Création d’une campagne

```http
POST /api/marketing/campagnes/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Campagne Été 2025",
  "canal": "email",
  "audience_id": 2,
  "contenu": "Découvrez nos nouveautés estivales !"
}
```

### Ajout d’un lead

```http
POST /api/marketing/leads/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Amina",
  "email": "amina@example.com",
  "source": "landing_page"
}
```

### Génération d’un rapport analytics

```http
GET /api/marketing/analytics/?campagne_id=1
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, scoring) aux rôles autorisés
- **Exporter** tous les logs et rapports d’audit (CSV, JSON)
- **Automatiser** l’exécution en CI/CD (GitHub Actions, Codespaces)
- **Séparer** scripts Python et Node.js pour compatibilité maximale

---

## 🌍 Multilingue

- **Français** : Ce dossier est documenté en français.
- **English** : This folder is documented in English.
- **العربية** : هذا المجلد موثق باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Afaylu agi yettwarnan s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📚 Documentation associée

- [Architecture backend](../../../../docs/architecture.md)
- [API Marketing (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Marketing souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
