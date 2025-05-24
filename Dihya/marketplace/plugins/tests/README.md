# Tests – Dihya Marketplace Plugins

Ce dossier contient les tests unitaires, d’intégration et E2E pour les plugins de la marketplace Dihya.

## Objectifs
- Vérifier la conformité, la sécurité, la multilingue, la souveraineté
- Couvrir tous les plugins (ex : stripe, plugin.js, plugin.py, etc.)
- Générer des rapports de couverture

## Structure recommandée
- test_stripe_plugin.js
- test_plugin.js
- test_plugin_py.py

## Lancement des tests

```bash
npm test
# ou
pytest
```

## Bonnes pratiques
- Couvrir tous les cas critiques (fail, edge, fallback)
- Tester l’internationalisation (fr, en, ar, tzm)
- Générer des rapports de couverture
