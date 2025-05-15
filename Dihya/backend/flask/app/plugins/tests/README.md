# plugins/tests — Tests unitaires API Plugins Dihya Coding

Ce dossier contient les tests unitaires pour l’API de gestion des plugins du backend Dihya Coding.

## Objectif

- Vérifier la sécurité (authentification, rôle admin) de chaque endpoint plugin.
- Tester la validation des payloads (nom, version, unicité…).
- Garantir la robustesse des opérations : ajout, suppression, activation/désactivation.
- Assurer la conformité métier et la non-régression lors des évolutions.

## Bonnes pratiques

- Isoler chaque test pour éviter les effets de bord (vider la liste des plugins avant chaque test).
- Utiliser des fixtures pour simuler différents utilisateurs (admin, user).
- Ne jamais inclure de secrets ou de données sensibles dans les tests.
- Couvrir tous les cas critiques : erreurs, duplicatas, accès non autorisé, etc.
- Documenter chaque test avec une docstring claire.

## Exemple d’exécution

```bash
pytest app/plugins/tests/