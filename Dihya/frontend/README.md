# 🚀 Dihya Coding – Frontend

Plateforme de génération de code, templates métiers et services robustes, modernes, extensibles et conformes RGPD.

---

## 🎯 Objectifs

- **Design moderne** : UI/UX accessible, responsive, compatible SEO et mobile
- **Sécurité** : validation stricte, anonymisation, anti-DDoS, rate limiting, logs sécurisés
- **Conformité RGPD** : consentement utilisateur, droit à l’oubli, logs anonymisés, portabilité
- **Auditabilité** : chaque action/log est traçable, effaçable, documentée
- **Extensibilité** : architecture modulaire, ajout facile de modules, routes, templates
- **Robustesse** : gestion des erreurs, fallback, tests automatisés, monitoring
- **Documentation claire** : docstring, commentaires, guides, exemples

---

## 🏗️ Structure du frontend

- `src/` : Code source principal
  - `App.js` : Composant principal, navigation, RGPD, auditabilité
  - `index.js` : Point d’entrée, initialisation, logs
  - `templates/` : Modules métiers (e-commerce, éducation, social…)
  - `utils/` : Utilitaires sécurité, RGPD, logs, API, export, fallback, SEO
  - `voice/` : Reconnaissance et synthèse vocale, accessibilité, logs
  - `tests/` : Tests unitaires, intégration, E2E, auditabilité
- `public/` : Fichiers statiques, index.html, favicon, manifest
- `.env` : Variables d’environnement (jamais de secrets en prod)
- `postcss.config.js` : Design moderne, accessibilité, SEO, auditabilité

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Jamais de données sensibles dans le code ou les logs, validation stricte, anonymisation, tokens sécurisés
- **RGPD** : Consentement explicite, logs anonymisés, droit à l’oubli, portabilité des données
- **Auditabilité** : Chaque module/fonction/log est commenté, traçable, effaçable
- **Extensibilité** : Ajout de modules, routes, templates ou utilitaires sans dette technique
- **Robustesse** : Tests automatisés, gestion des erreurs, fallback, monitoring
- **SEO** : Balises, headers, accessibilité, performance
- **Documentation** : Docstring JSDoc, guides, exemples, fichiers README par dossier

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

> **Dihya Coding : frontend moderne, robuste, extensible et conforme RGPD pour chaque génération.**