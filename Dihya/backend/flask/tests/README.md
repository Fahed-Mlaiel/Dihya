# Dihya Coding – Tests Backend Flask

## Présentation

Ce dossier contient tous les **tests automatisés** pour le backend Flask de Dihya Coding. Les tests garantissent la robustesse, la sécurité, la conformité RGPD, l’extensibilité et la qualité de la plateforme. Ils couvrent l’ensemble des modules : API, génération de projet, authentification, gestion des utilisateurs, plugins, templates métiers, scripts, sécurité, logs, migrations, etc.

---

## Objectifs & rôle des tests

- **Vérifier la conformité fonctionnelle et métier de chaque module**
- **Assurer la sécurité (authentification, permissions, injection, CORS, etc.)**
- **Garantir la conformité RGPD (suppression/export, anonymisation, logs)**
- **Tester la robustesse face aux erreurs, cas limites et attaques**
- **Valider la génération multi-stack (web, mobile, IA, DevOps, Blockchain)**
- **Couvrir l’extensibilité via plugins, scripts, templates métiers**
- **Automatiser les tests en CI/CD (GitHub Actions)**
- **Documenter chaque cas de test pour auditabilité**

---

## Structure du dossier

```
/tests/
├── test_api.py                # Tests API REST/GraphQL (routes, payloads, sécurité)
├── test_auth.py               # Tests authentification, rôles, permissions
├── test_user.py               # Tests gestion utilisateurs, RGPD, profils
├── test_project.py            # Tests génération de projet multi-stack
├── test_templates.py          # Tests templates métiers (import/export, sécurité)
├── test_plugins.py            # Tests plugins métiers, extensions, sécurité
├── test_scripts.py            # Tests scripts d’automatisation (backup, migration…)
├── test_security.py           # Tests sécurité (CORS, rate limiting, headers, anti-DDoS)
├── test_logs.py               # Tests logs, auditabilité, suppression/export RGPD
├── test_migrations.py         # Tests migrations, rollback, cohérence DB
├── fixtures/                  # Données de test, mocks, configs simulées
├── conftest.py                # Configuration Pytest (fixtures globales)
└── README.md                  # (ce fichier)
```

---

## Bonnes pratiques de test

- **Docstring** pour chaque test (objectif, scénario, sécurité)
- **Typage** et validation stricte des entrées/sorties
- **Mocks** pour simuler les dépendances externes (API, DB, plugins)
- **Logs horodatés pour chaque test critique**
- **Tests de non-régression à chaque évolution**
- **Respect de la conformité RGPD (anonymisation, suppression/export)**
- **Automatisation des tests dans la CI/CD**
- **Couverture maximale des cas d’usage métier et sécurité**

---

## Exemples de cas testés

- Authentification JWT/OAuth, gestion des rôles et permissions
- Génération automatique d’un projet à partir d’un cahier des charges
- Import/export de templates métiers (JSON, YAML, JS)
- Sécurité des routes API (CORS, rate limiting, headers)
- Suppression/export des données utilisateur (RGPD)
- Auditabilité des logs et traçabilité des actions
- Rollback et cohérence lors des migrations de schéma
- Extensibilité via plugins et scripts métiers

---

## Lancer les tests

Depuis la racine du backend Flask :

```bash
pytest tests/
```

---

## Contribution

- Ajouter des tests pour chaque nouvelle fonctionnalité ou correction
- Documenter chaque test (objectif, scénario, sécurité)
- Respecter la structure, la sécurité et la conformité RGPD
- Proposer vos améliorations via PR ou sur la marketplace communautaire

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute suggestion ou amélioration, ouvrez une issue ou une PR sur GitHub.*