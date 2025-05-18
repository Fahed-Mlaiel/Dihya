# Architecture Frontend — Dihya Coding

Ce document décrit l’architecture technique et fonctionnelle du frontend Dihya Coding, en garantissant : design moderne, SEO, génération dynamique, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 1. Principes d’architecture

- **Modularité** : chaque fonctionnalité (génération, auth, IA, plugins, i18n…) est isolée dans un dossier dédié.
- **Modernité** : React (ou Next.js), Tailwind CSS, composants réutilisables, hooks personnalisés.
- **SEO** : balises meta dynamiques, sitemap, robots.txt, manifest, accessibilité.
- **Sécurité** : validation/sanitation côté client, gestion JWT/OAuth, anti-XSS, CORS, gestion des rôles.
- **RGPD** : consentement cookies, anonymisation, export/purge des données utilisateur.
- **Extensibilité** : architecture ouverte pour plugins, templates, thèmes, multilingue.
- **Auditabilité** : logs front (actions critiques), traçabilité des générations, monitoring UX.

---

## 2. Structure des dossiers
frontend/
├── public/         # SEO, manifest, favicon, robots.txt, sitemap.xml
├── src/
│   ├── assets/     # Images, icônes, illustrations
│   ├── components/ # UI réutilisable (Navbar, Footer, SEO, etc.)
│   ├── layout/     # Layouts globaux (MainLayout, etc.)
│   ├── pages/      # Pages principales (Home, Generate, Preview, Auth, etc.)
│   ├── styles/     # Tailwind config, CSS global
│   ├── features/   # Logique métier (génération, auth, IA, plugins)
│   ├── contexts/   # Contextes React (auth, langue, thème)
│   ├── hooks/      # Hooks personnalisés (useAuth, useAI, useTheme)
│   ├── utils/      # Fonctions utilitaires (API, validation, sécurité)
│   ├── api/        # Appels API (génération, auth, etc.)
│   ├── i18n/       # Multilingue (locales, gestion dynamique)
│   └── tests/      # Tests unitaires et e2e
└── docs/           # Documentation utilisateur et dev


---

## 3. Flux fonctionnels principaux

### a. Génération de projet

- **Entrée utilisateur** : page Generate (texte libre, vocal, options stack, multilingue)
- **Validation & sanitation** : côté client avant envoi à l’API
- **Appel API** : `/api/generate` (backend sécurisé)
- **Affichage** : page Preview (code généré, live demo, partage)
- **Logs UX** : chaque génération est tracée côté front (sans données sensibles)

### b. Authentification & rôles

- **Pages Login/Register/Profile**
- **Gestion JWT/OAuth** : stockage sécurisé, vérification rôle (admin, user, invité)
- **Context Auth** : accessible dans toute l’app, hooks personnalisés

### c. Multilingue (i18n)

- **Fichiers de traduction** : `src/i18n/locales/`
- **LanguageSwitcher** : composant pour changer de langue à la volée
- **Détection automatique** : langue navigateur, fallback configurable

### d. Plugins & templates

- **Architecture ouverte** : chaque plugin/feature dans `src/features/plugins.js`
- **Templates UI** : sélection dynamique selon domaine (e-commerce, éducation…)

---

## 4. Sécurité & conformité RGPD

- **Validation/sanitation** : toutes les entrées utilisateur sont validées et nettoyées côté client
- **Anti-XSS/anti-injection** : via utilitaires et bonnes pratiques React
- **Consentement cookies** : bannière RGPD, gestion du consentement
- **Export/purge** : interface utilisateur pour demander l’export ou la suppression des données
- **Logs front** : actions critiques loggées (jamais de données sensibles)
- **Accessibilité** : respect des standards WCAG (contrastes, navigation clavier, ARIA)

---

## 5. SEO & accessibilité

- **Composant SEO** : balises meta dynamiques, OpenGraph, titre, description, canonical
- **Fichiers SEO** : `public/robots.txt`, `public/sitemap.xml`, `public/manifest.json`
- **Accessibilité** : labels, aria, navigation clavier, images décrites

---

## 6. Extensibilité & robustesse

- **Ajout de plugins** : analytics, CMS, Stripe, etc. via architecture modulaire
- **Templates** : UI/UX adaptables selon le domaine métier
- **Hooks & contextes** : pour chaque logique transversale (auth, thème, langue, IA)
- **Tests** : unitaires pour chaque composant/feature, e2e pour les parcours critiques

---

## 7. Documentation & bonnes pratiques

- **Docstring** : chaque composant, hook, feature doit être documenté
- **README & guides** : docs utilisateur et dev à jour dans `/docs`
- **Commentaires** : code commenté pour chaque logique métier ou point critique
- **Respect du cahier des charges** : chaque évolution doit être conforme à la sécurité, la souveraineté, la RGPD et la philosophie Dihya Coding

---

**Pour toute évolution, respecter la sécurité, la souveraineté, la conformité RGPD et la philosophie Dihya Coding.**