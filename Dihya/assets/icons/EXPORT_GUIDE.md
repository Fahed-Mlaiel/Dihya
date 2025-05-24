# Dihya Icons – Export RGPD

Ce fichier permet l’export des métadonnées des icônes Dihya, conforme RGPD, multilingue, accessibilité, audit, plugins.

- Format : JSON, CSV, YAML
- Export automatique via API ou CLI
- Exemple d’export :

```json
{
  "name": "Dihya Icons",
  "description": {"fr": "Icônes SVG/React ultra avancées..."},
  "version": "1.0.0",
  "created": "2025-05-22T00:00:00Z",
  ...
}
```

- Export CLI :
```bash
python meta_icons_export.py --export json
```

- Export API :
```http
GET /api/meta/icons?format=json
```

- RGPD : anonymisation, logs, audit, exportabilité, multilingue, accessibilité, plugins.

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
