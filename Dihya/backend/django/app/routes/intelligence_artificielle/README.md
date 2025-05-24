# 🤖 Dihya – Django Intelligence Artificielle API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/intelligence_artificielle`](#rôle-du-dossier-routesintelligence_artificielle)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API IA](#exemples-dapi-ia)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🤖 Rôle du dossier `routes/intelligence_artificielle`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à l’IA, l’automatisation, l’analyse avancée et la souveraineté algorithmique via l’API Django Dihya.

- **Multi-stack** : Django REST, FastAPI, plugins Python/Node, cloud souverain, IA open source, ML, NLP, vision, agents, LLM
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable, fallback IA open source
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, auditabilité
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST IA** : gestion des modèles, prédictions, analyses, entraînements, datasets, agents, pipelines, logs, audit
- **Interopérabilité** : intégration avec HuggingFace, ONNX, TensorFlow, PyTorch, OpenAI, LLM open source, webhooks, open data
- **Gestion des droits d’accès** : RBAC (admin, data scientist, analyste, utilisateur, auditeur, guest)
- **Traçabilité et logs** : audit des accès, prédictions, entraînements, suppressions, exports
- **Automatisation** : notifications, rappels, génération de rapports, IA explainability, monitoring, fallback open source
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, modèles, agents, pipelines

---

## 📁 Structure recommandée

```
intelligence_artificielle/
├── views.py           # Vues Django REST pour modèles, prédictions, entraînements, datasets, agents, pipelines
├── serializers.py     # Serializers pour modèles, prédictions, entraînements, datasets, agents, pipelines
├── urls.py            # Routage des endpoints IA
├── permissions.py     # Permissions RBAC pour l’accès aux services IA
├── tasks.py           # Tâches asynchrones (entraînements, monitoring, notifications)
├── assets/            # Exemples de modèles, datasets, notebooks, scripts, rapports
├── tests/             # Tests unitaires et d’intégration API IA
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, data scientist, analyste, utilisateur, guest)
- **Logs d’accès** et d’opérations critiques (prédiction, entraînement, suppression)
- **Chiffrement** des données sensibles (datasets, modèles, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité, explainability
- **Fallback IA open source** : tous les endpoints critiques disposent d’un fallback open source (ex : transformers, spaCy, llama.cpp)
- **Scripts de vérification d’intégrité** pour chaque modèle, dataset ou asset IA

---

## 🛠️ Exemples d’API IA

### Prédiction via un modèle NLP

```http
POST /api/intelligence_artificielle/predictions/
Authorization: Bearer <token>
Content-Type: application/json

{
  "modele_id": 1,
  "texte": "Dihya révolutionne l’IA souveraine."
}
```

### Entraînement d’un modèle

```http
POST /api/intelligence_artificielle/entrainements/
Authorization: Bearer <token>
Content-Type: application/json

{
  "modele_id": 1,
  "dataset_id": 3,
  "parametres": {"epochs": 10, "batch_size": 32}
}
```

### Déploiement d’un agent IA

```http
POST /api/intelligence_artificielle/agents/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Agent Amazigh",
  "type": "chatbot",
  "modele_id": 2
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, entraînement) aux rôles autorisés
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
- [API IA (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – IA souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
