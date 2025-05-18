# 🧩 Tests unitaires – Dihya Coding

Ce dossier regroupe tous les tests unitaires pour Dihya Coding : vérification des fonctions, services, templates, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Valider chaque fonction, service ou composant de façon isolée
- Garantir la sécurité, la conformité RGPD, l’auditabilité et la robustesse du code métier
- Permettre l’extension facile à de nouveaux tests unitaires

---

## 📁 Structure recommandée

- `*.unit.js` : Un fichier par module ou service testé (ex : `generation.unit.js`, `auth.unit.js`, etc.)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Pas de données sensibles dans les tests ou les logs, anonymisation des logs si besoin, droit à l’oubli (purge)
- **Auditabilité** : Chaque test est commenté, logs vérifiés et effaçables, historique des tests
- **Extensibilité** : Ajout facile de nouveaux tests unitaires ou modules
- **Robustesse** : Gestion des erreurs, tests de fallback, vérification des comportements inattendus
- **SEO** : Vérification des fonctions liées au SEO (balises, meta, accessibilité)
- **Documentation** : Docstring JSDoc pour chaque test, exemples d’utilisation

---

## 📝 Exemple d’utilisation

```js
import { sanitize } from '../../services/generationService';

describe('sanitize', () => {
  it('supprime les caractères dangereux', () => {
    expect(sanitize('<script>alert(1)</script>')).not.toContain('<');
    expect(sanitize('texte normal')).toBe('texte normal');
  });
});
```

---

## 📚 Documentation associée

- [generation.unit.js](./generation.unit.js)
- [auth.unit.js](./auth.unit.js)
- [seo.unit.js](./seo.unit.js)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : tests unitaires modernes, robustes, extensibles et conformes RGPD pour chaque génération.**