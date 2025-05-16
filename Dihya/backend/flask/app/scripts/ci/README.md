# Scripts CI/CD custom

Ce dossier regroupe les scripts d’automatisation pour l’intégration continue (CI) et le déploiement continu (CD) du backend Dihya Coding.

## Objectif

- Centraliser les helpers pour les workflows GitHub Actions, la vérification de la qualité, les tests automatisés, le linting, la sécurité, etc.
- Faciliter la maintenance et l’extension des pipelines CI/CD.

## Bonnes pratiques Dihya Coding

- **Sécurité** : ne jamais stocker de secrets ou credentials dans les scripts, utiliser les variables d’environnement GitHub Actions.
- **Documentation** : chaque script doit être documenté (usage, paramètres, sécurité).
- **Extensibilité** : prévoir l’ajout facile de nouveaux jobs ou outils d’automatisation.
- **Validation** : valider les entrées/sorties des scripts pour éviter les erreurs en pipeline.
- **Portabilité** : scripts compatibles Linux, usage de chemins relatifs, pas de dépendances propriétaires.

## Exemples de scripts à inclure

- `run_tests.sh` : lance les tests unitaires et d’intégration
- `lint.sh` : vérifie la qualité du code (flake8, black, etc.)
- `check_security.sh` : scan des dépendances et vulnérabilités
- `build_and_deploy.sh` : build et déploiement automatisé (Docker, K8s, etc.)
- `generate_coverage.sh` : génère le rapport de couverture de tests

## Exemple d’utilisation dans un workflow GitHub Actions

```yaml
- name: Lint code
  run: bash scripts/ci/lint.sh

- name: Run tests
  run: bash scripts/ci/run_tests.sh
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*
