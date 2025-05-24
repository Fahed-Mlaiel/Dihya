# 🏝️ Dihya – Django Tourisme API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/tourisme`](#rôle-du-dossier-routestourisme)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API tourisme](#exemples-dapi-tourisme)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🏝️ Rôle du dossier `routes/tourisme`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la valorisation et l’innovation du secteur tourisme via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration CRM/ERP, cloud souverain, IA tourisme, gestion offres, réservations, avis, guides, événements
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST tourisme** : gestion des offres, destinations, réservations, avis, guides, événements, partenaires, IA tourisme, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, agent, guide, voyageur, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Interopérabilité** : intégration avec CRM, ERP, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, gestion planning, réservation dynamique
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
tourisme/
├── views.py           # Vues Django REST pour offres, destinations, réservations, avis, guides, événements, partenaires, IA tourisme
├── serializers.py     # Serializers pour offres, destinations, réservations, avis, guides, événements, partenaires, IA tourisme
├── urls.py            # Routage des endpoints tourisme
├── permissions.py     # Permissions RBAC pour l’accès aux services tourisme
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, gestion planning)
├── assets/            # Exemples d’offres, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API tourisme
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, agent, guide, voyageur, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (réservations, avis, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque offre ou asset tourisme

---

## 🛠️ Exemples d’API tourisme

### Création d’une offre touristique

```http
POST /api/tourisme/offres/
Authorization: Bearer <token>
Content-Type: application/json

{
  "titre": "Séjour Kabylie Authentique",
  "destination_id": 3,
  "prix": 1200,
  "date_debut": "2025-07-01",
  "date_fin": "2025-07-10"
}
```

### Réservation d’un séjour

```http
POST /api/tourisme/reservations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "voyageur_id": 8,
  "offre_id": 2,
  "date": "2025-07-01"
}
```

### Ajout d’un avis

```http
POST /api/tourisme/avis/
Authorization: Bearer <token>
Content-Type: application/json

{
  "voyageur_id": 8,
  "offre_id": 2,
  "note": 5,
  "commentaire": "Expérience inoubliable, guide exceptionnel !"
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, gestion offres) aux rôles autorisés
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
- [API Tourisme (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Tourisme souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
