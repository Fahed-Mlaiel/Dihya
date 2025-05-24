# Tests – Dihya Marketplace Templates

Ce dossier contient les tests unitaires, d’intégration et E2E pour les templates métiers de la marketplace Dihya.

## Objectifs
- Vérifier la conformité, la sécurité, la multilingue, la souveraineté
- Couvrir tous les templates (3D, e-commerce, VR/AR, générique, etc.)
- Générer des rapports de couverture

## Structure recommandée
- test_3d_template.js
- test_ecommerce_template.js
- test_vr_ar_template.js
- test_example_template.js

## Lancement des tests

```bash
npm test
# ou
jest
```

## Bonnes pratiques
- Couvrir tous les cas critiques (fail, edge, fallback)
- Tester l’internationalisation (fr, en, ar, tzm)
- Générer des rapports de couverture
