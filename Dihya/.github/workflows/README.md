# CI/CD workflow pour Dihya Coding

Ce dossier contient les fichiers de configuration pour l’intégration continue (CI) et le déploiement continu (CD) du projet Dihya Coding, basés sur GitHub Actions.

## Objectifs

- Automatiser les tests, la vérification du code, la génération de documentation et le déploiement.
- Garantir la qualité, la sécurité et la conformité du code à chaque contribution.
- Faciliter la collaboration et la livraison continue.

## Contenu

- **ci.yml** : Pipeline principal pour le backend Flask (tests, lint, génération de doc, artefacts).
- (Ajouter ici d’autres workflows pour le frontend, le déploiement, la sécurité, etc.)

## Bonnes pratiques

- Chaque push ou pull request sur `main` ou `develop` déclenche la CI.
- Les tests doivent passer avant tout merge.
- Les erreurs de linting ou de sécurité doivent bloquer le pipeline.
- Les secrets (tokens, clés) doivent être stockés dans les variables GitHub Actions, jamais dans le code.
- Documenter chaque étape du workflow pour faciliter la maintenance.

## Exemple d’ajout d’un nouveau workflow

Créer un fichier `.yml` dans ce dossier, puis adapter les jobs selon la stack (frontend, blockchain, etc.).

## Sécurité

- Ne jamais exposer de secrets dans les logs.
- Utiliser des permissions minimales pour chaque job.
- Ajouter des jobs de scan de vulnérabilités si besoin.

---

**Équipe Dihya Coding**