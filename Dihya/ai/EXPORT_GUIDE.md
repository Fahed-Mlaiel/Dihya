# Dihya AI – Export RGPD

Ce fichier permet l’export des logs, prompts, réponses et métadonnées IA Dihya, conforme RGPD, multilingue, accessibilité, audit, plugins.

- Format : JSON, CSV, YAML
- Export automatique via API ou CLI
- Exemple d’export :

```json
{
  "prompt": "Génère un template métier RH.",
  "response": "[Mixtral:fr] ...",
  "user_id": "demo-user",
  "lang": "fr",
  "engine": "mixtral",
  "timestamp": "2025-05-22T00:00:00Z"
}
```

- Export CLI :
```bash
python export_ai_rgpd.py --export json
```

- Export API :
```http
GET /api/ai/export?format=json
```

- RGPD : anonymisation, logs, audit, exportabilité, multilingue, accessibilité, plugins.

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
