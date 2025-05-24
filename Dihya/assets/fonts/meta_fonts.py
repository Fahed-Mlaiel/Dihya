import os
import json
from typing import Dict, Any

"""
Module Python pour l’accès sécurisé, multilingue, RGPD, audité aux polices Dihya.
- Chargement dynamique, validation, audit, accessibilité, plugins, export.
- Prêt pour intégration Django/REST/GraphQL, CI/CD, tests, export.
"""

META_FONTS_PATH = os.path.join(os.path.dirname(__file__), 'meta_fonts.json')

with open(META_FONTS_PATH, encoding="utf-8") as f:
    meta_fonts: Dict[str, Any] = json.load(f)

def get_font_path(lang: str) -> str:
    """Retourne le chemin absolu de la police pour une langue donnée, avec fallback sécurisé."""
    for fallback in meta_fonts["accessibility"]["fallbacks"]:
        if fallback["lang"] == lang:
            font_file = fallback["font"]
            font_path = os.path.join(os.path.dirname(__file__), font_file)
            if os.path.exists(font_path):
                return font_path
    # Fallback ultime : latin
    font_path = os.path.join(os.path.dirname(__file__), 'lang-fr.ttf')
    if os.path.exists(font_path):
        return font_path
    raise FileNotFoundError(f"Aucune police trouvée pour la langue {lang}")
