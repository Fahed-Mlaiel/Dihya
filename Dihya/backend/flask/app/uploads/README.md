# Dossier `uploads/` — Backend Dihya Coding

Ce dossier est dédié au stockage temporaire des fichiers uploadés par les utilisateurs via l’API backend Dihya Coding.

## Bonnes pratiques Dihya Coding

- **Aucun secret ou donnée sensible** ne doit être stocké ici sans chiffrement ou contrôle strict.
- **Validation stricte** de chaque fichier uploadé : type, taille, extension, contenu.
- **Sécuriser l’accès** : seules les routes API authentifiées (JWT requis) peuvent écrire ou lire ici.
- **Nettoyage automatique** : prévoir des tâches planifiées pour supprimer les fichiers anciens ou non validés.
- **Organisation** : utiliser des sous-dossiers par utilisateur ou usage si besoin (`user_<id>/`, `import/`, etc.).
- **Ne jamais exécuter** un fichier stocké dans ce dossier.

## Exemples d’utilisation

- Upload de documents utilisateur (CV, images, etc.)
- Import de données pour traitement batch
- Fichiers temporaires pour conversion ou analyse

## Sécurité

- Logger chaque opération d’upload, de lecture ou de suppression pour audit.
- Interdire l’accès public direct à ce dossier.
- Prévoir une politique de rétention stricte : suppression automatique des fichiers non utilisés ou obsolètes.

---

*Ce fichier fait partie de la documentation interne Dihya Coding.*