# services/tests — Tests unitaires des services métiers Dihya Coding

Ce dossier regroupe les tests unitaires pour tous les services métiers du backend Dihya Coding (authentification, utilisateurs, mailing, notifications, templates, OAuth2…).

## Objectif

- Garantir la robustesse, la sécurité et la conformité métier de chaque service.
- Prévenir les régressions lors des évolutions du code.
- Couvrir tous les cas critiques : succès, erreurs, sécurité, validation, edge cases.

## Bonnes pratiques

- Isoler chaque test pour éviter les effets de bord (utiliser des fixtures).
- Simuler les entrées utilisateur et les états critiques (erreurs, duplicatas…).
- Ne jamais inclure de secrets ou de données sensibles dans les tests.
- Documenter chaque test avec une docstring claire.
- Couvrir les cas d’usage métier, la sécurité (hash, tokens, validation), et la conformité RGPD.

## Exemple d’exécution

```bash
pytest app/services/tests/