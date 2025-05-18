# 🧪 Tests – Dihya Coding

Ce dossier regroupe tous les tests (unitaires, intégration, end-to-end) pour Dihya Coding : vérification des services, templates, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Valider le fonctionnement de chaque module, service, template et API
- Garantir la sécurité, la conformité RGPD, l’auditabilité et la robustesse du code
- Permettre l’extension facile à de nouveaux tests, scénarios ou modules

---

## 📁 Structure recommandée

- `unit/` : Tests unitaires (fonctions, services, utils)
- `integration/` : Tests d’intégration (API, services, modules)
- `e2e/` : Tests end-to-end (scénarios utilisateurs, génération, navigation)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Consentement utilisateur simulé, anonymisation des logs, droit à l’oubli (purge), pas de données sensibles dans les tests ou les logs
- **Auditabilité** : Chaque test est commenté, logs vérifiés et effaçables, historique des tests
- **Extensibilité** : Ajout facile de nouveaux tests, modules ou scénarios
- **Robustesse** : Gestion des erreurs, tests de fallback, vérification des comportements inattendus
- **SEO** : Vérification des fonctions et API liées au SEO (balises, meta, accessibilité)
- **Documentation** : Docstring JSDoc pour chaque test, exemples d’utilisation

---

## 📝 Exemple d’utilisation

```js
import { generate } from '../services/generationService';

describe('Génération – Test unitaire', () => {
  it('génère du code source sécurisé', () => {
    const result = generate({ type: 'code', options: { language: 'js', content: 'let x = 1;' } });
    expect(result.success).toBe(true);
  });
});
```

---

## 📚 Documentation associée

- [unit/README.md](./unit/README.md)
- [integration/README.md](./integration/README.md)
- [e2e/README.md](./e2e/README.md)
- [Cahier des charges Dihya Coding](../../docs/user_guide/README.md)

---

> **Dihya Coding : tests modernes, robustes, extensibles et conformes RGPD pour chaque génération.**