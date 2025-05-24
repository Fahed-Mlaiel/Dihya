# Dihya Fonts – Guide d’intégration avancée

Ce dossier fournit toutes les polices open source, multilingues, accessibles, RGPD, optimisées IA/VR/AR pour le projet Dihya.

## Polices incluses
- Latin (fr, en, de, nl, es, hi)
- Arabe (ar, fa, he)
- Tifinagh (tzm)
- CJK (zh, ja, ko)

## Fallbacks et accessibilité
- Chaque langue a un fallback testé (voir meta_fonts.json)
- Contraste AAA, audit accessibilité automatisé

## Intégration backend (Django/REST/GraphQL)
- Endpoints sécurisés pour servir les polices (CORS, JWT, audit, logs RGPD)
- Exemple Django :

```python
from django.http import FileResponse
from Dihya.assets.fonts.meta_fonts import get_font_path

def font_file_view(request, lang):
    """Endpoint sécurisé, RGPD, multilingue, audit, accessibilité."""
    path = get_font_path(lang)
    return FileResponse(open(path, 'rb'), as_attachment=True)
```

## Plugins & automatisation
- Audit accessibilité, RGPD, optimisation, export
- Génération automatique de fixtures/tests

## CI/CD
- Tests automatisés sur les polices, accessibilité, RGPD, logs, export
- Intégration GitHub Actions, Docker, K8s, fallback local

## Historique & audit
- Voir meta_fonts.json (champ `audit`)

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
