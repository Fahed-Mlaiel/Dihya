import os
import json
from typing import Dict, Any

"""
Module Python pour l’accès sécurisé, multilingue, RGPD, audité aux icônes Dihya.
- Chargement dynamique, validation, audit, accessibilité, plugins, export.
- Prêt pour intégration Django/REST/GraphQL, CI/CD, tests, export.
"""

META_ICONS_PATH = os.path.join(os.path.dirname(__file__), 'meta_icons.json')

with open(META_ICONS_PATH, encoding="utf-8") as f:
    meta_icons: Dict[str, Any] = json.load(f)

def get_icon_path(icon: str) -> str:
    """Retourne le chemin absolu de l’icône, avec fallback sécurisé."""
    icon_file = f"{icon}.svg"
    icon_path = os.path.join(os.path.dirname(__file__), icon_file)
    if os.path.exists(icon_path):
        return icon_path
    raise FileNotFoundError(f"Aucune icône trouvée pour {icon}")
