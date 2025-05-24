# Guide de Contribution – Templates Marketplace Dihya

## Objectif
Permettre à tous (débutants, experts, écoles, ONG, makers) de créer, publier et maintenir des templates métiers souverains, sécurisés, multilingues, accessibles, documentés, testés, et prêts à l’emploi.

## Structure d’un template
- `README.md` : description, usage, sécurité, RGPD, accessibilité
- `template.js` : code source modulaire, hooks, i18n, sécurité, extension
- `tests/` : tests unitaires, intégration, e2e, accessibilité, sécurité
- `assets/` : images, icônes, captures, libres de droits
- `plugin.js` (optionnel) : extension, intégration, audit

## Bonnes pratiques
- Multilingue (fr, en, ar, tzr)
- Sécurité (XSS, RBAC, logs, anonymisation)
- Accessibilité (WCAG, ARIA, responsive, SEO)
- Souveraineté (open source, fallback, auditabilité)
- Documentation claire, exemples, tests, contribution

## Processus
1. Forkez le dépôt, créez une branche dédiée
2. Développez votre template selon la structure recommandée
3. Ajoutez des tests, documentez chaque ajout
4. Vérifiez la sécurité, la conformité RGPD, l’accessibilité
5. Soumettez une Pull Request détaillée
6. Répondez aux retours de la communauté

## Contact
[marketplace@dihya.io](mailto:marketplace@dihya.io)
