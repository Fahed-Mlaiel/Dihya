# README – Tests d’intégration avancés Dihya Coding

Ce dossier contient les tests d’intégration automatisés pour garantir :
- Sécurité maximale (CORS, JWT, validation, audit, logs, mocks, RBAC, plugins)
- RGPD (anonymisation, consentement, auditabilité)
- Accessibilité (tests ARIA, navigation clavier, multilingue)
- CI/CD-ready, extensible, documentation intégrée
- Exemples, guides, contribution

## Exécution

```bash
pytest --cov --disable-warnings
npm test -- --ci --coverage
```

## Multilingue
- Tests i18n (fr, en, ar, de, es, it, zh, ru, pt, nl, tr, pl, ja)

## Contribution
Voir [CONTRIBUTING.md](../../../../CONTRIBUTING.md)
