# Dihya Logos – Export RGPD

Ce fichier permet l’export des métadonnées des logos Dihya, conforme RGPD, multilingue, accessibilité, audit, plugins.

- Format : JSON, CSV, YAML
- Export automatique via API ou CLI
- Exemple d’export :

```json
{
  "name": "Dihya Logos",
  "description": {"fr": "Logos SVG/React ultra avancés..."},
  "version": "1.0.0",
  "created": "2025-05-22T00:00:00Z",
  ...
}
```

- Export CLI :
```bash
node plugin_rgpd_export.js json
```

- Export API :
```http
GET /api/meta/logos?format=json
```

- RGPD : anonymisation, logs, audit, exportabilité, multilingue, accessibilité, plugins.

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
