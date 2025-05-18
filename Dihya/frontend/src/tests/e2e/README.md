# 🧪 Tests End-to-End (e2e) – Dihya Coding

Ce dossier regroupe tous les tests end-to-end (E2E) pour Dihya Coding : vérification de la génération, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Valider le fonctionnement global des services et templates métiers en conditions réelles
- Garantir la sécurité, la conformité RGPD, l’auditabilité et la robustesse de chaque fonctionnalité
- Permettre l’extension facile à de nouveaux tests ou scénarios métiers

---

## 📁 Structure recommandée

- `generation.e2e.js` : Tests E2E du service de génération (code, markdown, image, logs, RGPD)
- `auth.e2e.js` : Tests E2E du service d’authentification (inscription, login, logout, logs, RGPD)
- `seo.e2e.js` : Tests E2E du service SEO (balises, accessibilité, logs, RGPD)
- `ecommerce.e2e.js` : Tests E2E du template e-commerce (produit, panier, paiement, logs, RGPD)
- `education.e2e.js` : Tests E2E du template éducation (cours, modules, quiz, logs, RGPD)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Consentement utilisateur simulé, anonymisation des logs, droit à l’oubli (purge), pas de données sensibles dans les tests ou les logs
- **Auditabilité** : Chaque test est commenté, logs vérifiés et effaçables, historique des tests
- **Extensibilité** : Ajout facile de nouveaux tests ou scénarios
- **Robustesse** : Gestion des erreurs, tests de fallback, vérification des comportements inattendus
- **SEO** : Vérification des balises, accessibilité, indexabilité
- **Documentation** : Docstring JSDoc pour chaque test, exemples d’utilisation

---

## 📝 Exemple d’utilisation

```js
import { generate } from '../../services/generationService';

describe('Génération – E2E', () => {
  it('génère du code source sécurisé', () => {
    const result = generate({ type: 'code', options: { language: 'js', content: 'let x = 1;' } });
    expect(result.success).toBe(true);
  });
});
```

---

## 📚 Documentation associée

- [generation.e2e.js](./generation.e2e.js)
- [auth.e2e.js](./auth.e2e.js)
- [seo.e2e.js](./seo.e2e.js)
- [ecommerce.e2e.js](./ecommerce.e2e.js)
- [education.e2e.js](./education.e2e.js)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : tests E2E modernes, robustes, extensibles et conformes RGPD pour chaque génération.**