# README – Dihya Logos

Ce dossier contient les logos du projet Dihya.

- Conventions de nommage, formats (SVG, PNG, etc.), branding
- Exemples d’utilisation, scripts d’import/export
- Contribution, extension, personnalisation

Voir [../assets.md](../assets.md)

---

## 📦 Contenu

- **index.js**
  Registre centralisé exportant tous les logos pour usage React, Node, mobile, plugins, docs.
- **/*.svg**
  Logos SVG optimisés, accessibles, multilingues, thématiques (clair, sombre, amazigh, métiers…).
- **/*.png / *.ico**
  Fallbacks ou favicons pour legacy ou mobile.
- **README.md**
  Ce guide d’utilisation, bonnes pratiques, accessibilité, contribution.

---

## 🌍 Multilingue & Accessibilité

- Chaque logo doit avoir un `aria-label` dynamique selon la langue de l’utilisateur (fr, en, ar, tzr).
- Les logos principaux sont fournis en plusieurs variantes : clair, sombre, amazigh, métiers, multilingue.
- Tous les logos sont testés pour la navigation clavier et les lecteurs d’écran.

---

## 🛠️ Utilisation (React)

```jsx
import { Logos } from './index';
// Exemple : <Logos.main aria-label="Logo Dihya" role="img" />
```

- Pour chaque logo, utilisez un `aria-label` pertinent et localisé.
- Pour usage Node.js ou mobile, exportez le chemin ou le composant selon la stack.

---

## ➕ Ajouter un nouveau logo

1. Placez votre SVG optimisé dans ce dossier.
2. Ajoutez-le dans `index.js` avec un nom explicite, multilingue ou thématique si besoin.
3. Vérifiez l’accessibilité (`aria-label`, focusable, contraste).
4. Documentez-le ici si c’est un logo métier, plugin ou critique.

---

## 🧩 Exemples de logos métiers ou thématiques

- `dihya-amazigh.svg` – Logo Dihya version amazigh
- `dihya-dark.svg` – Logo Dihya version sombre
- `dihya-fr.svg` – Logo Dihya version française
- `legal.svg` – Logo métier juridique
- `health.svg` – Logo métier santé
- `education.svg` – Logo métier éducation

---

## 🛡️ Souveraineté & Sécurité

- Aucun tracking, aucune dépendance externe, tous les assets sont open source.
- Les logos sont vérifiés pour éviter toute faille SVG (XSS, JS embarqué).

---

## 📚 Ressources

- [SVG Accessibility – MDN](https://developer.mozilla.org/fr/docs/Web/SVG/Accessibility)
- [React Accessible SVG Logos](https://www.smashingmagazine.com/2021/01/accessible-svg-patterns-react/)
- [Contribution Dihya](../../docs/contribution/README.md)

---

*Ce dossier garantit la cohérence, l’accessibilité et la souveraineté visuelle du projet Dihya. Toute contribution de logo métier, multilingue ou inclusif est la bienvenue !*
