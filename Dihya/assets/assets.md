# 🗂️ Dihya – Assets Registry & Guide

Ce dossier regroupe tous les assets du projet **Dihya** : icônes, logos, images, polices, illustrations, vidéos, sons, templates, etc.
Il garantit : cohérence visuelle, accessibilité, performance, multilingue, souveraineté numérique, compatibilité multi-stack (web, mobile, plugins, docs).

---

## 📦 Structure recommandée

- **/icons/**
  Icônes SVG/React accessibles, multilingues, métiers, plugins.
- **/logos/**
  Logos Dihya (clair, sombre, amazigh, métiers, multilingue), favicons.
- **/images/**
  Illustrations, photos, backgrounds, assets UI/UX.
- **/fonts/**
  Polices open source, multilingues (fr, en, ar, tzr), prêtes à l’emploi.
- **/videos/**
  Démos, tutoriels, branding, assets motion.
- **/audio/**
  Sons UI, notifications, voix IA, jingles branding.
- **/templates/**
  Templates métiers, modèles d’UI, wireframes, snippets.
- **/README.md**
  Guide d’utilisation, bonnes pratiques, accessibilité, contribution.

---

## 🌍 Multilingue & Accessibilité

- Tous les assets critiques sont fournis en versions multilingues (fr, en, ar, tzr) et testés pour l’accessibilité (contraste, aria-label, alt, focusable).
- Les polices couvrent tous les alphabets nécessaires (latin, arabe, tifinagh…).
- Les images et vidéos sont optimisées pour le web et le mobile (WebP, SVG, compression lossless).

---

## 🛠️ Utilisation

- **Web/React** : import direct via index.js ou chemin relatif.
- **Mobile** : export des chemins ou composants adaptés (SVG, PNG, etc.).
- **Docs** : utilisez les assets pour illustrer guides, API, branding.
- **Plugins** : assets métiers ou spécifiques à chaque plugin.

---

## ➕ Ajouter un nouvel asset

1. Placez votre asset dans le dossier approprié.
2. Ajoutez-le dans le registre (`index.js` ou équivalent) si besoin.
3. Vérifiez : accessibilité (alt, aria-label), performance (taille, format), souveraineté (open source, pas de tracking).
4. Documentez-le ici si c’est un asset critique, métier ou multilingue.

---

## 🧩 Exemples d’assets métiers

- `template-legal.json` – Template juridique
- `plugin-analytics.svg` – Icône plugin analytics
- `lang-tzr.ttf` – Police amazigh
- `demo-ar.mp4` – Vidéo démo arabe

---

## 🛡️ Souveraineté & Sécurité

- Aucun asset externe, tout est open source ou libre de droits.
- Les SVG/images sont vérifiés pour éviter toute faille (XSS, JS embarqué).
- Les assets critiques sont versionnés et audités.

---

## 📚 Ressources

- [SVG Accessibility – MDN](https://developer.mozilla.org/fr/docs/Web/SVG/Accessibility)
- [Google Fonts Open Source](https://fonts.google.com/)
- [Contribution Dihya](../docs/contribution/README.md)

---

# Dihya – Assets Documentation

- Liste et description des assets (images, logos, icônes, polices, templates, branding, i18n)
- Conventions de nommage, formats, accessibilité, multilingue
- Procédures d’ajout, de modification, de suppression
- Scripts d’import/export, versioning, audit

Voir [README.md](README.md)

*Ce dossier assets est la colonne vertébrale visuelle, sonore et UX du projet Dihya. Toute contribution d’asset métier, multilingue ou inclusif est la bienvenue !*
