# Guide Développeur Frontend — Dihya Coding

Ce guide détaille les bonnes pratiques, l’architecture, la sécurité, la génération, le design moderne, le SEO et la conformité RGPD pour le développement du frontend Dihya Coding.

---

## 1. Objectifs & philosophie

- **Modernité** : React, Tailwind CSS, composants réutilisables, responsive, thèmes amazigh/moderne.
- **SEO** : balises structurées, sitemap, robots.txt, composant SEO dédié, accessibilité.
- **Génération** : pages et composants dynamiques pour la génération automatique de projets.
- **Sécurité** : validation côté client, sanitation, gestion JWT/OAuth, CORS, anti-XSS.
- **RGPD** : consentement cookies, anonymisation, export/purge données utilisateur.
- **Extensibilité** : architecture modulaire, plugins, hooks, contextes, i18n.
- **Auditabilité** : logs front (actions critiques), traçabilité des générations, monitoring UX.

---

## 2. Structure du projet
frontend/ ├── public/ # SEO, manifest, favicon, robots.txt, sitemap.xml ├── src/ │ ├── assets/ # Images, icônes, illustrations │ ├── components/ # UI réutilisable (Navbar, Footer, SEO, etc.) │ ├── layout/ # Layouts globaux (MainLayout, etc.) │ ├── pages/ # Pages principales (Home, Generate, Preview, Auth, etc.) │ ├── styles/ # Tailwind config, CSS global │ ├── features/ # Logique métier (génération, auth, IA, plugins) │ ├── contexts/ # Contextes React (auth, langue, thème) │ ├── hooks/ # Hooks personnalisés (useAuth, useAI, useTheme) │ ├── utils/ # Fonctions utilitaires (API, validation, sécurité) │ ├── api/ # Appels API (génération, auth, etc.) │ ├── i18n/ # Multilingue (locales, gestion dynamique) │ └── tests/ # Tests unitaires et e2e └── docs/ # Documentation utilisateur et dev


---

## 3. Design & UI/UX

- **Tailwind CSS** : pour un design moderne, responsive, personnalisable.
- **Thèmes** : support du thème amazigh et thèmes personnalisés (via ThemeSwitcher).
- **Accessibilité** : contrastes, navigation clavier, ARIA, responsive mobile/tablette.
- **Composants** : Navbar, Footer, Sidebar, ChatAssistant, ProjectCard, SEO, VoiceInput, etc.
- **Pages clés** : Home, Generate, Preview, Login, Register, Profile, NotFound.

---

## 4. Génération frontend

- **Page Generate*

---

## 3. Design & UI/UX

- **Tailwind CSS** : pour un design moderne, responsive, personnalisable.
- **Thèmes** : support du thème amazigh et thèmes personnalisés (via ThemeSwitcher).
- **Accessibilité** : contrastes, navigation clavier, ARIA, responsive mobile/tablette.
- **Composants** : Navbar, Footer, Sidebar, ChatAssistant, ProjectCard, SEO, VoiceInput, etc.
- **Pages clés** : Home, Generate, Preview, Login, Register, Profile, NotFound.

---

## 4. Génération frontend

- **Page Generate** : formulaire intelligent (texte libre, vocal, options stack), validation dynamique.
- **Assistant IA** : composant ChatAssistant pour suggestions, correction, aide à la génération.
- **Preview** : page Preview pour tester le projet généré (iframe, live demo, partage).
- **API** : appels sécurisés à `/api/generate` (backend), gestion des erreurs, loading, logs UX.

---

## 5. SEO & accessibilité

- **Composant SEO** : balises meta, OpenGraph, titre dynamique, description, canonical.
- **Fichiers SEO** : `public/robots.txt`, `public/sitemap.xml`, `public/manifest.json`.
- **Accessibilité** : labels, aria, navigation clavier, focus visible, images décrites.

---

## 6. Sécurité & RGPD

- **Authentification** : JWT/OAuth, stockage sécurisé (httpOnly si possible), vérification rôle.
- **Validation** : toutes les entrées utilisateur sont validées côté client avant envoi.
- **Sanitation** : nettoyage des entrées (anti-XSS, anti-injection).
- **CORS** : géré côté backend, mais attention aux appels API.
- **Consentement cookies** : bannière RGPD, gestion du consentement.
- **Export/Purge** : interface pour demander l’export ou la suppression des données utilisateur.

---

## 7. Extensibilité & plugins

- **Architecture modulaire** : chaque feature/plugin dans son dossier, hooks documentés.
- **Ajout de plugins** : analytics, CMS, Stripe, etc. via `src/features/plugins.js`.
- **Templates** : support de templates UI selon le domaine (e-commerce, éducation…).

---

## 8. Multilingue (i18n)

- **Gestion dynamique** : fichiers de traduction dans `src/i18n/locales/`, support dialectes.
- **LanguageSwitcher** : composant pour changer de langue à la volée.
- **Détection automatique** : langue navigateur, fallback configurable.

---

## 9. Tests & auditabilité

- **Tests unitaires** : pour chaque composant, feature, hook.
- **Tests e2e** : scénarios utilisateur critiques (génération, auth, preview).
- **Logs front** : actions critiques (génération, login, erreurs) loggées côté client (sans données sensibles).
- **Monitoring UX** : hooks pour mesurer la performance et l’usage (respect RGPD).

---

## 10. Documentation & bonnes pratiques

- **Docstring** : chaque composant, hook, feature doit être documenté.
- **README & guides** : docs utilisateur et dev à jour dans `/docs`.
- **Commentaires** : code commenté pour chaque logique métier ou point critique.
- **Respect du cahier des charges** : chaque évolution doit être conforme à la sécurité, la souveraineté, la RGPD et la philosophie Dihya Coding.

---

**Pour toute contribution, suivez ce guide et respectez la charte Dihya Coding (sécurité, souveraineté, extensibilité, RGPD).**