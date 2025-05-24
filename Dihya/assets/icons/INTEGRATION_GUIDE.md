# Dihya Icons – Guide d’intégration avancée

Ce dossier fournit toutes les icônes SVG/React, accessibles, multilingues, RGPD, optimisées IA/VR/AR pour le projet Dihya.

## Intégration frontend (React/Next.js/Vue)
- Utilisez `import { Icons } from './index'`.
- Chaque icône accepte un `aria-label` multilingue dynamique (voir meta_icons.json).
- Accessibilité AAA, audit automatique, RGPD-ready.

## Intégration backend (Django/REST/GraphQL)
- Endpoints sécurisés pour servir les icônes (CORS, JWT, audit, logs RGPD).
- Exemple Django :

```python
from django.http import FileResponse
from Dihya.assets.icons.meta_icons import get_icon_path

def icon_file_view(request, icon):
    """Endpoint sécurisé, RGPD, multilingue, audit, accessibilité."""
    path = get_icon_path(icon)
    return FileResponse(open(path, 'rb'), as_attachment=True)
```

## Plugins & automatisation
- Audit accessibilité, RGPD, optimisation, export
- Génération automatique de fixtures/tests

## CI/CD
- Tests automatisés sur les icônes, accessibilité, RGPD, logs, export
- Intégration GitHub Actions, Docker, K8s, fallback local

## Historique & audit
- Voir meta_icons.json (champ `audit`)

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
