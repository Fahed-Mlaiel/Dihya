# 🌐 i18n – Dihya Coding

Ce dossier centralise toute l’internationalisation (i18n) de Dihya Coding : gestion multilingue, dialectes, conformité RGPD, auditabilité, accessibilité et SEO.  
Chaque composant vise : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.

---

## 🚀 Objectifs

- Offrir une expérience multilingue, inclusive et accessible à tous les utilisateurs (arabe, berbère, français, anglais, dialectes…)
- Garantir la conformité RGPD, la sécurité et l’auditabilité de la gestion des langues
- Faciliter l’extension, la maintenance et la personnalisation des langues et dialectes

---

## 📁 Structure recommandée

- `index.js` : Initialisation et configuration d’i18n (React, RGPD, auditabilité)
- `locales/` : Dossiers et fichiers de traduction pour chaque langue et dialecte
  - `ar/translation.json` : Arabe standard
  - `ber/translation.json` : Berbère (amazigh)
  - `fr/translation.json` : Français
  - `en/translation.json` : Anglais
  - `dialectes.json` : Métadonnées et descriptions des dialectes supportés
  - `README.md` : Documentation des conventions et bonnes pratiques

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Pas de données personnelles dans les fichiers de traduction, consentement utilisateur requis, logs locaux anonymisés, droit à l’oubli (purge).
- **Auditabilité** : Historique local des changements de langue, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouvelles langues ou dialectes.
- **SEO** : Mots-clés et descriptions optimisés pour chaque langue/dialecte.
- **Accessibilité** : Traductions adaptées pour tous les publics, prise en charge des langues régionales.
- **Documentation** : Structure claire, conventions de nommage, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import i18n from './index';

// Utilisation dans un composant React
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t } = useTranslation();
  return <h1>{t('app.title')}</h1>;
}
```

---

## 📚 Documentation associée

- [locales/README.md](./locales/README.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : internationalisation moderne, inclusive, sécurisée, robuste, extensible et conforme RGPD pour chaque génération.**