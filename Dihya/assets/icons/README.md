# README – Dihya Icons

Ce dossier contient les icônes du projet Dihya.

- Conventions de nommage, formats (SVG, PNG, etc.), accessibilité
- Exemples d’utilisation, scripts d’import/export
- Contribution, extension, personnalisation

Voir [../assets.md](../assets.md)

---

## 📦 Contenu

- **index.js**
  Registre centralisé exportant tous les icônes pour usage React, Node, mobile, plugins.
- **/*.svg**
  Icônes SVG optimisés, accessibles, multilingues, personnalisables.
- **/*.png / *.ico**
  Fallbacks ou favicons pour legacy ou mobile.
- **README.md**
  Ce guide d’utilisation, bonnes pratiques, accessibilité, contribution.

---

## 🌍 Multilingue & Accessibilité

- Chaque icône doit avoir un `aria-label` dynamique selon la langue de l’utilisateur (fr, en, ar, tzr).
- Les icônes critiques (sécurité, accessibilité, langue) sont fournis dans toutes les langues supportées.
- Les icônes sont testés pour la navigation clavier et les lecteurs d’écran.

---

## 🛠️ Utilisation (React)

```jsx
import { Icons } from './index';
// Exemple : <Icons.dihya aria-label="Logo Dihya" role="img" />
```

- Pour chaque icône, utilisez un `aria-label` pertinent et localisé.
- Pour usage Node.js ou mobile, exportez le chemin ou le composant selon la stack.

---

## ➕ Ajouter un nouvel icône

1. Placez votre SVG optimisé dans ce dossier.
2. Ajoutez-le dans `index.js` avec un nom explicite, multilingue si besoin.
3. Vérifiez l’accessibilité (`aria-label`, focusable, contraste).
4. Documentez-le ici si c’est un icône métier ou critique.

---

## 🧩 Exemples d’icônes métiers

- `template-legal.svg` – Template juridique
- `plugin-analytics.svg` – Plugin analytics
- `lang-tzr.svg` – Langue amazigh
- `accessibility.svg` – Accessibilité universelle

---

## 🛡️ Souveraineté & Sécurité

- Aucun tracking, aucune dépendance externe, tous les assets sont open source.
- Les icônes critiques sont vérifiés pour éviter toute faille SVG (XSS, JS embarqué).

---

## 📚 Ressources

- [SVG Accessibility – MDN](https://developer.mozilla.org/fr/docs/Web/SVG/Accessibility)
- [React Accessible SVG Icons](https://www.smashingmagazine.com/2021/01/accessible-svg-patterns-react/)
- [Contribution Dihya](../../docs/contribution/README.md)

---

*Ce dossier garantit la cohérence, l’accessibilité et la souveraineté visuelle du projet Dihya. Toute contribution d’icône métier, multilingue ou inclusif est la bienvenue !*
