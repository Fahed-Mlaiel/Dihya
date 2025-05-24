# Dihya Coding – Migrations & Évolution de la Base de Données

## Présentation

Ce dossier contient tous les **scripts de migration** et la gestion de l’évolution du schéma de base de données pour le backend Flask de Dihya Coding. Les migrations assurent la cohérence, la sécurité, la conformité RGPD, la traçabilité et la robustesse des données lors de l’ajout de nouvelles fonctionnalités, de la correction de bugs ou de l’extension de la plateforme à de nouveaux métiers.

---

## Objectifs & rôle des migrations

- **Gérer l’évolution du schéma de base de données** (ajout, modification, suppression de tables/champs)
- **Assurer la compatibilité ascendante et descendante**
- **Garantir la sécurité et la conformité RGPD lors des changements**
- **Permettre le rollback en cas d’erreur**
- **Automatiser l’application des migrations en CI/CD**
- **Documenter chaque évolution pour auditabilité et support**

---

## Structure du dossier

```
/migrations/
├── versions/               # Scripts de migration auto-générés (Alembic/Flask-Migrate)
├── env.py                  # Script d’environnement de migration
├── script.py.mako          # Template de génération de migration
├── README.md               # (ce fichier)
```

---

## Bonnes pratiques de migration

- **Décrire chaque migration** (but, impact, rollback) dans le script et la PR associée
- **Versionner chaque modification** pour auditabilité
- **Tester chaque migration sur un environnement de staging avant production**
- **Respecter la conformité RGPD lors de la suppression/export de données**
- **Automatiser l’application des migrations via GitHub Actions**
- **Ne jamais stocker de données sensibles en clair dans les scripts**
- **Prévoir des scripts de rollback pour chaque migration critique**
- **Documenter les dépendances entre migrations**

---

## Exemples de cas d’usage

- Ajout d’un champ `is_rgpd_deleted` pour la suppression logique RGPD
- Migration pour prise en charge de nouveaux métiers (ex : ajout de tables santé, juridique…)
- Modification de schémas pour support multilingue ou nouveaux rôles utilisateurs
- Suppression ou anonymisation de données sensibles sur demande utilisateur
- Migration de données lors de l’évolution des templates métiers

---

## Sécurité & conformité RGPD

- **Logs horodatés de chaque migration appliquée**
- **Suppression/export des données sur demande utilisateur**
- **Auditabilité complète des changements**
- **Aucune donnée confidentielle dans les scripts ou logs**
- **Tests automatisés pour chaque migration critique**

---

## Contribution

- Documenter chaque nouvelle migration (but, impact, rollback)
- Respecter la conformité RGPD et la sécurité à chaque évolution
- Proposer vos améliorations via PR ou sur la marketplace communautaire

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute suggestion ou amélioration, ouvrez une issue ou une PR sur GitHub.*