# 📄 Pages – Dihya Coding

Ce dossier regroupe toutes les pages principales de l’application Dihya Coding : accueil, génération, aperçu, profil, connexion, erreurs, etc.  
Chaque page vise : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Offrir une expérience utilisateur moderne, accessible et conforme RGPD pour chaque page
- Garantir la sécurité, la robustesse, l’auditabilité et la documentation de chaque route/page
- Faciliter l’extension, la maintenance et la personnalisation des pages

---

## 📁 Structure recommandée

- `Home.jsx` : Page d’accueil (présentation, navigation, logs RGPD)
- `Generate.jsx` : Génération de projet/module (formulaire, validation, logs)
- `Preview.jsx` : Aperçu de projet/module généré (sécurité, logs, RGPD)
- `Profile.jsx` : Profil utilisateur (gestion, droit à l’oubli, logs)
- `Login.jsx` : Connexion utilisateur (validation, logs, sécurité)
- `NotFound.jsx` : Page 404 (SEO, logs, accessibilité)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Validation stricte des entrées, anonymisation des logs, consentement utilisateur requis, droit à l’oubli (purge).
- **Auditabilité** : Historique local des accès et actions, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouvelles pages ou routes.
- **Robustesse** : Gestion des erreurs, feedback utilisateur, accessibilité.
- **SEO** : Titres, descriptions et balises meta dynamiques pour chaque page.
- **Documentation** : Docstring JSDoc pour chaque page, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```jsx
import Home from './Home';
import Generate from './Generate';
import Preview from './Preview';
import Profile from './Profile';
import Login from './Login';
import NotFound from './NotFound';

// Utilisation dans un routeur React
<Route path="/" element={<Home />} />
<Route path="/generate" element={<Generate />} />
<Route path="/preview" element={<Preview />} />
<Route path="/profile" element={<Profile />} />
<Route path="/login" element={<Login />} />
<Route path="*" element={<NotFound />} />
```

---

## 📚 Documentation associée

- [Layout](../layout/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : pages modernes, accessibles, sécurisées, robustes, extensibles et conformes RGPD pour chaque génération.**