# 🧪 Tests – Dihya Coding

Ce dossier regroupe tous les tests (unitaires, intégration, end-to-end) pour la plateforme **Dihya Coding**. L’ensemble garantit la conformité au cahier des charges : génération multi-stack, sécurité, RGPD, auditabilité, extensibilité, robustesse, UX, i18n, souveraineté numérique et documentation claire.

---

## 🚀 Objectifs des tests

- **Valider** le fonctionnement de chaque module, service, template, API et plugin généré automatiquement (frontend, backend, IA, DevOps, Blockchain…)
- **Garantir** la sécurité, la conformité RGPD, l’auditabilité, la robustesse et la souveraineté numérique du code et des échanges
- **Tester** l’extensibilité (ajout de nouveaux métiers, modules, plugins, stacks, langues…)
- **Assurer** une expérience utilisateur et développeur moderne, multilingue, accessible et personnalisable

---

## 📁 Structure recommandée

- `unit/` : Tests unitaires (fonctions, services, templates métiers, utilitaires)
- `integration/` : Tests d’intégration (API, services, modules métiers, plugins)
- `e2e/` : Tests end-to-end (scénarios utilisateurs, génération, navigation, sécurité, fallback)
- `README.md` : Présentation, bonnes pratiques, exemples, liens

---

## 🛡️ Bonnes pratiques Dihya Coding

- **Sécurité & RGPD** : Consentement utilisateur simulé, anonymisation des logs, droit à l’oubli (purge), pas de données sensibles dans les tests ou les logs
- **Auditabilité** : Chaque test est commenté, logs vérifiés et effaçables, historique des tests, conformité AGPL
- **Extensibilité** : Ajout facile de nouveaux tests, métiers, stacks, plugins, langues, scénarios
- **Robustesse** : Gestion des erreurs, tests de fallback, vérification des comportements inattendus, résilience
- **Souveraineté** : Tests de fallback open source, backup, décentralisation, logs horodatés
- **SEO & Accessibilité** : Vérification des fonctions, API et balises liées au SEO, accessibilité, multilingue/dialectes
- **Documentation** : Docstring JSDoc pour chaque test, exemples d’utilisation, liens vers guides

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

- [unit/README.md](./unit/README.md) – Tests unitaires (fonctions, services, templates métiers)
- [integration/README.md](./integration/README.md) – Tests d’intégration (API, services, plugins)
- [e2e/README.md](./e2e/README.md) – Tests end-to-end (scénarios utilisateurs, navigation, sécurité)
- [Cahier des charges Dihya Coding](../../docs/user_guide/README.md)

---

## 🏷️ Branding & Souveraineté

- **Nom** : Dihya Coding
- **Thème** : héritage amazigh + modernité tech
- **Slogan** : "De l’idée au code, en toute souveraineté."
- **Licence** : AGPL, open-source, logs horodatés, auditabilité

---

> **Dihya Coding : tests modernes, robustes, extensibles, souverains et conformes RGPD pour chaque génération.**