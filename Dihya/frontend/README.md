# 🚀 Dihya Coding – Frontend (Version Finale)

Plateforme No-Code/Low-Code multi-métiers : génération automatique de projets numériques (web, mobile, IA, DevOps, Blockchain) à partir d’un cahier des charges écrit ou vocal. Design moderne, souveraineté numérique, sécurité, conformité RGPD, extensibilité, auditabilité.

---

## 🎯 Objectif

- Générer tout type de projet numérique (frontend + backend) à partir d’un cahier des charges écrit ou dicté.
- Démocratiser la création d’applications web, mobiles, scripts IA, DevOps, Blockchain, etc., sans expérience en programmation.
- Offrir une interface moderne, multilingue (dialectes inclus), responsive, accessible et personnalisable.

---

## 👥 Public cible

- Débutants, entrepreneurs, makers, freelancers, créateurs de contenu, activistes numériques
- Écoles de code, ONG tech, associations

---

## 🛠️ Fonctionnalités principales

- **Entrée intelligente** : texte libre multilingue, entrée vocale (Speech-to-Text + GPT-4o)
- **Assistant IA** : suggestions, correction, mémoire longue, chat contextuel
- **Génération multi-stack** : Web App (React/Vue/Svelte), Backend API (Flask/Node.js/Django), Mobile (React Native/Flutter), IA (Python/ML/NLP), DevOps (Docker/K8s/Terraform), Blockchain (Solidity)
- **Templates métiers** : Santé, Juridique, Immobilier, Banque, Assurance, RH, Industrie, Logistique, Transport, Énergie, Tourisme, IT, Blockchain, IA, Recherche, etc.
- **UI/UX moderne** : Tailwind/Material UI, responsive, thèmes amazighs ou personnalisables
- **Backend sécurisé** : Auth JWT/OAuth, gestion des rôles, REST/GraphQL
- **Déploiement automatique** : GitHub Codespaces, Actions CI/CD, Pages, Replit/Render fallback
- **SEO & Sécurité** : balises, sitemap, robots.txt, validation, CORS, anti-DDoS, rate limiting
- **Mailing & Traduction** : API (SendGrid, Mailgun), i18n dynamique, support dialectes
- **Preview instantanée** : démo live, lien partageable
- **Extensible** : plugins custom, marketplace, import/export de templates, documentation claire
- **Souveraineté numérique** : fallback modèles open-source (Mixtral, LLaMA, Mistral), hébergement décentralisé (IPFS), backups auto, licence AGPL

---

## 🏗️ Structure du frontend

```
/src
  App.js                # Composant principal, navigation, RGPD, auditabilité
  index.js              # Point d’entrée, initialisation, logs, fallback souverain
  /templates            # Modules métiers (e-commerce, éducation, social…)
  /utils                # Sécurité, RGPD, logs, API, export, fallback, SEO
  /voice                # Reconnaissance/synthèse vocale, accessibilité, logs
  /tests                # Tests unitaires, intégration, E2E, auditabilité
/public                 # Fichiers statiques, index.html, favicon, manifest
.env                    # Variables d’environnement (jamais de secrets en prod)
postcss.config.js       # Design moderne, accessibilité, SEO, auditabilité
```

---

## 🗺️ Routes principales

- `/` : Accueil, présentation, accès à la génération
- `/generate` : Génération de projet (texte/vocal, assistant IA, import/export)
- `/templates` : Marketplace de templates métiers (import/export)
- `/plugins` : Marketplace de plugins (analytics, paiement, CMS…)
- `/demo` : Preview live, lien partageable
- `/admin` : Gestion utilisateurs, templates, plugins, logs
- `/auth` : Connexion/Inscription (OAuth/JWT)
- `/docs` : Documentation utilisateur et contribution
- `/dashboard-global` : Dashboard global (conformité, monitoring)

---

## 🚦 Dashboard global conformité/monitoring

- Accessible via `/dashboard-global` (composant React, badges SVG dynamiques, rendu Markdown, iframe)
- Rafraîchissement automatique, accessibilité, i18n-ready
- Intégration directe dans la navigation principale

---

## 🛡️ Sécurité, RGPD & Auditabilité

- **Consentement RGPD obligatoire** (bannière, logs anonymisés, droit à l’oubli)
- **Logs** : chaque action est traçable, effaçable, documentée, anonymisée
- **Sécurité** : validation stricte, anti-DDoS, rate limiting, CORS, headers, tokens sécurisés
- **Auditabilité** : chaque module/fonction/log est commenté, traçable, effaçable

---

## 🌍 Multilingue & Accessibilité

- Support natif : français, anglais, arabe, berbère (dialectes inclus)
- UI/UX accessible (WCAG), responsive, thèmes personnalisables

---

## 🧩 Extensibilité & Plugins

- Architecture modulaire : ajout facile de modules, routes, templates, plugins
- Marketplace de plugins et templates métiers (contribution externe)
- Documentation claire pour ajout de métier, import/export, contribution

---

## 📝 Exemples d’utilisation

```js
import { apiGet } from './utils/api';
import { startSpeechToText } from './voice/speechToText';

apiGet('/status').then(res => console.log(res));
startSpeechToText({ lang: 'fr-FR', onResult: txt => alert(txt) });
```

---

## 📚 Documentation associée

- [src/](./src/)
- [utils/README.md](./src/utils/README.md)
- [voice/README.md](./src/voice/README.md)
- [tests/README.md](./src/tests/README.md)
- [Cahier des charges Dihya Coding](../docs/user_guide/README.md)

---

## 🧪 Tests & auditabilité

- **Unitaires** : `src/tests/unit/`
- **Intégration** : `src/tests/integration/`
- **E2E** : `src/tests/e2e/`
- **Logs** : anonymisés, effaçables, traçables

---

## 🏷️ Variables d’environnement

Voir `.env` et `.env.example` pour la configuration RGPD, SEO, sécurité, auditabilité, robustesse.

---

## 🏆 Branding & souveraineté

- **Nom** : Dihya Coding
- **Slogan** : "De l’idée au code, en toute souveraineté."
- **Thème** : héritage amazigh + modernité tech
- **Licence** : AGPL (open-source, souveraineté garantie)

---

> **Dihya Coding : frontend moderne, robuste, extensible, souverain et conforme RGPD pour chaque génération.**

# README – Dihya Frontend

Ce dossier contient le frontend du projet Dihya : UI/UX, i18n, accessibilité, sécurité, plugins, tests, CI/CD, documentation, etc.

- Architecture modulaire, React/Vue/Svelte, multilingue, responsive
- Exemples d’utilisation, composants, scripts, tests
- Contribution, extension, personnalisation

Voir [../../README.md](../../README.md), [../README.md](../README.md)
