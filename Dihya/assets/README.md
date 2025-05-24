# README – Dihya Assets

Ce dossier contient tous les assets du projet Dihya : images, logos, icônes, polices, templates, branding, i18n, etc.

- Structure claire, multilingue, accessible, versionnée
- Exemples d’utilisation, conventions de nommage, scripts d’import/export
- Contribution, extension, personnalisation

Voir [../../README.md](../../README.md), [../README.md](../README.md)

# 🗂️ Dihya Coding – Assets Registry & Guide
**Multilingue | Accessible | Souverain | Prêt pour la production**

---

## 🎨 Rôle du dossier `assets` | Assets Role | دور مجلد الأصول | ⴰⵙⵉⵏⴰⵡ

Ce dossier centralise toutes les ressources statiques et médias nécessaires à la plateforme **Dihya Coding** :

- **Logos et branding** (SVG, PNG, React, multilingue, variantes métiers)
- **Icônes UI/UX** (SVG, React, accessibles, multilingues, métiers, plugins)
- **Images métiers** (pour les templates sectoriels, illustrations, backgrounds)
- **Fichiers multimédias** (audio, vidéo, démos, voix IA, jingles)
- **Polices** (open source, multilingues, RGPD, accessibilité)
- **Templates métiers** (JSON, YAML, snippets UI, wireframes)
- **Exports design** (Figma, palettes, tokens, assets UI)
- **Assets pour la génération automatique** (avatars IA, assets de preview, assets plugins)
- **Assets pour la documentation** (screenshots, diagrammes, branding docs)

---

## 📁 Structure recommandée | Recommended Structure | الهيكلية المقترحة | ⴰⵎⵙⵙⴰⵡ

```text
assets/
├── icons/      # Icônes SVG/React accessibles, multilingues, métiers, plugins
├── logos/      # Logos Dihya (clair, sombre, amazigh, métiers, multilingue), favicons
├── images/     # Illustrations, photos, backgrounds, assets UI/UX
├── fonts/      # Polices open source, multilingues (fr, en, ar, tzr)
├── videos/     # Démos, tutoriels, branding, assets motion
├── audio/      # Sons UI, notifications, voix IA, jingles branding
├── templates/  # Templates métiers, modèles d’UI, wireframes, snippets
├── figma/      # Exports Figma, palettes, design tokens
├── metiers/    # Images spécifiques aux templates métiers
├── demo/       # Captures d’écran, vidéos de démonstration
└── README.md   # Ce fichier / This file / هذا الملف / ⴰⵙⴳⴳⴰⵙ
```

---

## 🌍 Multilingue & Accessibilité | Multilingual & Accessibility | التعدد اللغوي وإمكانية الوصول | ⵜⴰⵎⴰⵣⵉⵖⵜ ⴷ ⵜⴰⵏⴰⵡⴰⵙⵜ

- Tous les assets critiques sont fournis en versions multilingues (fr, en, ar, tzr) et testés pour l’accessibilité (contraste, aria-label, alt, focusable).
- Les polices couvrent tous les alphabets nécessaires (latin, arabe, tifinagh…).
- Les images et vidéos sont optimisées pour le web et le mobile (WebP, SVG, compression lossless).
- Les assets sont utilisables sur toutes les stacks (React, Node, Flask, Django, Flutter, mobile, plugins, docs).

---

## 🛠️ Utilisation | Usage | الاستخدام | ⴰⵙⵉⵏⴰⵡ

- **Web/React** : import direct via `index.js` ou chemin relatif.
- **Mobile** : export des chemins ou composants adaptés (SVG, PNG, etc.).
- **Backend** : accès via scripts Python (`main.py`), Node.js, ou API.
- **Docs** : utilisez les assets pour illustrer guides, API, branding.
- **Plugins** : assets métiers ou spécifiques à chaque plugin.

---

## ➕ Ajouter un nouvel asset | Add a new asset | إضافة أصل جديد | ⴰⵙⵉⵏⴰⵡ ⴰⵎⵎⴰⵙⴰⵏ

1. Placez votre asset dans le dossier approprié.
2. Ajoutez-le dans le registre (`index.js`, `main.py` ou équivalent) si besoin.
3. Vérifiez : accessibilité (alt, aria-label), performance (taille, format), souveraineté (open source, pas de tracking).
4. Documentez-le ici si c’est un asset critique, métier ou multilingue.

---

## 🔒 Bonnes pratiques | Best Practices | أفضل الممارسات | ⵜⴰⵏⴰⵡⴰⵙⵜ

- **Nommez clairement** chaque fichier (ex : `logo-amazigh.svg`, `template-sante.png`).
- **Optimisez** les images (taille, format web, compression).
- **Respectez la RGPD** : pas de données personnelles dans les assets.
- **Versionnez** les assets critiques (logo, branding) pour la traçabilité.
- **Centralisez** les assets partagés pour éviter les doublons.
- **Aucun asset externe** : tout doit être open source ou libre de droits.
- **Auditabilité** : chaque ajout/modification d’asset doit être documenté dans les PR.
- **Extensibilité** : ajoutez de nouveaux assets métiers au fil de l’évolution des templates.

---

## 🛡️ Sécurité & conformité | Security & Compliance | الأمان والامتثال | ⵜⴰⵏⴰⵡⴰⵙⵜ ⴷ ⵜⴰⵎⴰⵣⵉⵖⵜ

- **Aucune donnée sensible** ne doit transiter ou être stockée ici.
- Les SVG/images sont vérifiés pour éviter toute faille (XSS, JS embarqué).
- Les assets critiques sont versionnés et audités.

---

## 📝 Contribution | Contribution | المساهمة | ⵜⴰⵏⴰⵡⴰⵙⵜ

- Toute contribution d’asset doit respecter la charte graphique Dihya Coding.
- Pour proposer un nouveau logo, icône ou illustration, ouvrez une PR avec une description claire.
- Voir [CONTRIBUTING.md](../../CONTRIBUTING.md) pour les guidelines.

---

## 📢 À propos | About | حول | ⴰⵙⵉⵏⴰⵡ

- **Thème visuel** : héritage amazigh + modernité tech.
- **Palette** : voir `/design/figma` pour les couleurs officielles.
- **Logo officiel** : `/assets/logos/dihya-amazigh.svg`

---

**Dihya Coding** – Plateforme No-Code souveraine, ouverte et inclusive.
**Dihya Coding** – Sovereign, open and inclusive No-Code platform.
**ديهيا كودينغ – منصة بدون كود، سيادية، مفتوحة وشاملة.**
**ⴷⵉⵀⵢⴰ ⴽⵓⴷⵉⵏⴳ – ⵜⴰⵏⴰⵡⴰⵙⵜ ⴷ ⵜⴰⵎⴰⵣⵉⵖⵜ، ⴰⵏⴼⴰⵜⴻⵏ، ⴰⵏⵙⴻⵏⴻⵏ.**
