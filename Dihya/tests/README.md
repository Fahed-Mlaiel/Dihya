# 🧪 Dihya – Tests (README)

Ce dossier regroupe tous les tests du projet Dihya : unitaires, intégration, e2e, accessibilité, sécurité, multilingue, CI/CD.

---

## Structure
- **unit/** : tests unitaires (Python, JS, etc.)
- **integration/** : tests d’intégration multi-stack
- **e2e/** : tests end-to-end (web, mobile, API)
- **manual/** : scénarios de tests manuels
- **securite/** : tests de sécurité, audit, conformité

---

## Types de tests
- **Unitaires** : chaque module/fonction
- **Intégration** : API, DB, plugins, IA
- **E2E** : parcours utilisateur, accessibilité, multilingue
- **Sécurité** : XSS, CSRF, RBAC, secrets
- **Accessibilité** : WCAG, ARIA, contrastes, navigation clavier
- **Performance** : temps de réponse, charge

---

## Multilingue
- Tous les tests critiques sont multilingues (fr, en, ar, tzr)
- Les scénarios couvrent les cas d’usage métiers, souveraineté, conformité

---

## CI/CD
- Intégration avec GitHub Actions, scripts CI, badges de couverture
- Lint, build, test, audit automatisés

---

## Exécution
- **Python** : `pytest tests/`
- **Node.js** : `npm test` ou `yarn test`
- **Manuel** : voir `manual/README.md`

---

## Contribution
- Ajouter des tests pour chaque nouvelle fonctionnalité
- Documenter chaque scénario (langue, métier, sécurité)
- Vérifier la couverture et la conformité

---

## Contact
Pour toute question : [qa@dihya.io](mailto:qa@dihya.io)
