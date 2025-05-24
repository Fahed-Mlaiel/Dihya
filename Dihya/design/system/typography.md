# 🔤 Dihya – Typographie (Design System)

Documentation avancée sur la typographie : polices, tailles, hiérarchie, multilingue, souveraineté, accessibilité.

---

## Polices officielles
- Montserrat (titres, UI)
- Inter (texte courant, UI)
- Roboto (fallback, compatibilité Android)
- Noto Sans Arabic (arabe)
- Noto Sans Tifinagh (amazigh)

---

## Hiérarchie typographique
- **h1** : 2.5rem, gras
- **h2** : 2rem, gras
- **h3** : 1.5rem, semi-gras
- **body** : 1rem, normal
- **small** : 0.875rem, normal

---

## Bonnes pratiques
- Utiliser les polices libres, multilingues, souveraines
- Respecter la hiérarchie pour l’accessibilité (screen readers, SEO)
- Tester le rendu sur tous les supports/langues

---

## Exemples d’intégration
- **CSS** :
```css
body {
  font-family: 'Inter', 'Montserrat', 'Roboto', 'Noto Sans Arabic', 'Noto Sans Tifinagh', sans-serif;
}
h1 { font-size: 2.5rem; font-weight: bold; }
```
- **JS** :
```js
export const fonts = {
  montserrat: 'Montserrat, sans-serif',
  inter: 'Inter, sans-serif',
  roboto: 'Roboto, sans-serif',
  arabic: 'Noto Sans Arabic, sans-serif',
  tifinagh: 'Noto Sans Tifinagh, sans-serif',
};
```

---

## Contact
[design@dihya.io](mailto:design@dihya.io)
