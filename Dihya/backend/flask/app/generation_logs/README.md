# Traçabilité des générations – Dihya Coding

Ce dossier centralise la gestion des logs de génération automatique de projets.  
Il garantit la transparence, la conformité RGPD, la souveraineté numérique et la sécurité des traces.

---

## Objectifs

- **Tracer chaque génération** (succès ou erreur) de façon horodatée et structurée (JSON)
- **Permettre l’audit** et l’export des logs pour analyse ou conformité
- **Assurer la sécurité** : aucune donnée sensible (mot de passe, token, spec brute) n’est loggée
- **Permettre la purge** des logs à la demande (conformité RGPD)
- **Prévoir l’extensibilité** : export possible vers Notion, IPFS, stockage décentralisé, etc.

---

## Fonctionnalités

- **Log structuré** : chaque événement contient :
  - Horodatage UTC
  - ID utilisateur (si fourni)
  - Nom du projet généré
  - Stack technique
  - Liste des fichiers générés (noms uniquement)
  - Plugins et template utilisés
  - Statut (succès/erreur)
  - Message d’erreur (si échec)
  - Métadonnées additionnelles (extensible)

- **Export** : possibilité d’exporter tous les logs dans un fichier externe pour audit, sauvegarde ou migration

- **Purge** : suppression totale des logs sur demande (conformité RGPD, suppression de compte, anonymisation)

- **Lecture/Audit** : récupération des logs pour affichage ou analyse automatisée

---

## Bonnes pratiques

- **Ne jamais logger** : mot de passe, token, spec brute, contenu de fichier sensible
- **Logger uniquement** : métadonnées utiles à l’audit et à la traçabilité
- **Utiliser le format JSON** pour faciliter l’analyse automatisée et l’export
- **Purger les logs** sur demande utilisateur ou en cas de suppression de compte
- **Logger chaque action sensible** (génération, export, purge) pour auditabilité
- **Extensibilité** : prévoir des hooks pour exporter vers d’autres systèmes (Notion, IPFS, etc.)

---

## Utilisation

Voir le module [`__init__.py`](./__init__.py) pour :
- `log_generation_event(user_id, needs, code, status, error, extra)`
- `export_generation_logs(destination_path)`
- `purge_generation_logs()`
- `get_generation_logs(limit)`

---

## Exemple de log

```json
{
  "timestamp": "2025-05-16T12:34:56Z",
  "user_id": "user_123",
  "project_name": "Blog Amazigh",
  "stack": "fullstack",
  "files": ["README.md", "backend/app.py", "frontend/App.js"],
  "status": "success",
  "error": null,
  "plugins": ["analytics"],
  "template": "e-commerce"
}