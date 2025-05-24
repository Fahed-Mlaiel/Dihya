# Dihya Logos – Guide des tests

## Tests Node.js/Jest
- `test_logos_node.js` : vérifie la présence, l’accessibilité, la conformité de chaque logo SVG
- Lancer avec : `npx jest Dihya/assets/logos/test_logos_node.js`

## Tests Python
- `test_meta_logos.py` : vérifie la structure, l’accès, la conformité RGPD/multilingue des métadonnées
- Lancer avec : `pytest Dihya/assets/logos/test_meta_logos.py`

## CI/CD
- Workflows GitHub Actions `.github/workflows/integration_logos.yml` : tests Node.js, Python, audit SVG, export RGPD

## Bonnes pratiques
- Ajouter un test pour chaque nouveau logo ou plugin
- Vérifier l’accessibilité (aria-label, role, focusable)
- Couvrir tous les cas d’usage (React, Node, Django, plugins)

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
