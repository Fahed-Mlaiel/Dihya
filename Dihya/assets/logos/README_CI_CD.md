# Dihya Logos – CI/CD & Automatisation

Ce module est entièrement automatisé :
- **Tests Node.js/Jest** : accessibilité, conformité, multilingue, RGPD
- **Tests Python** : structure, accès, RGPD, multilingue
- **Optimisation SVG** : via plugin Node.js (svgo)
- **Audit accessibilité SVG** : plugin Node.js
- **Export RGPD** : JSON, CSV, YAML, artefacts CI
- **Workflows GitHub Actions** : `.github/workflows/integration_logos.yml`
- **Compatibilité Docker/K8s**

## Exécution locale
- `npx jest Dihya/assets/logos/test_logos_node.js`
- `pytest Dihya/assets/logos/test_meta_logos.py`
- `node Dihya/assets/logos/plugin_svg_optimizer.js`
- `node Dihya/assets/logos/plugin_a11y_audit.js`
- `node Dihya/assets/logos/plugin_rgpd_export.js json`

## Production-ready
- 100% automatisé, testé, RGPD, multilingue, souverain, extensible, CI/CD-ready.
