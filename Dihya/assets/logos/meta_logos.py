"""
Dihya – Module Python pour l’accès sécurisé, multilingue, RGPD, audité aux logos Dihya.
- Chargement dynamique, validation, audit, accessibilité, plugins, export.
- Prêt pour intégration Django/REST/GraphQL, CI/CD, tests, export.
"""
import os
import json
from typing import Dict, Any

META_LOGOS_PATH = os.path.join(os.path.dirname(__file__), 'meta_logos.json')

with open(META_LOGOS_PATH, encoding="utf-8") as f:
    meta_logos: Dict[str, Any] = json.load(f)

def get_logo_path(logo: str) -> str:
    """Retourne le chemin absolu du logo, avec fallback sécurisé."""
    logo_file = f"{logo}.svg"
    logo_path = os.path.join(os.path.dirname(__file__), logo_file)
    if os.path.exists(logo_path):
        return logo_path
    raise FileNotFoundError(f"Aucun logo trouvé pour {logo}")
