"""
Dihya – Assets Registry & Loader (Python)
Ultra avancé, accessible, multilingue, souverain, modulaire.
Centralise et expose tous les assets du projet pour usage multi-stack (Flask, Django, FastAPI, scripts, tests, plugins, docs).
Prêt pour la production, la démo, la contribution.

@author: Dihya Team
"""

import os
from typing import Dict, Optional

# Définir les chemins de base des assets
ASSETS_BASE = os.path.dirname(os.path.abspath(__file__))

def asset_path(*parts) -> str:
    """Construit un chemin absolu vers un asset."""
    return os.path.join(ASSETS_BASE, *parts)

# Icônes (exemple)
ICONS = {
    "dihya": asset_path("icons", "dihya-logo.svg"),
    "user": asset_path("icons", "user.svg"),
    "admin": asset_path("icons", "admin.svg"),
    "lang_fr": asset_path("icons", "lang-fr.svg"),
    "lang_en": asset_path("icons", "lang-en.svg"),
    "lang_ar": asset_path("icons", "lang-ar.svg"),
    "lang_tzr": asset_path("icons", "lang-tzr.svg"),
    "accessibility": asset_path("icons", "accessibility.svg"),
    "security": asset_path("icons", "security.svg"),
    "plugin": asset_path("icons", "plugin.svg"),
    "template": asset_path("icons", "template.svg"),
    # Ajoutez ici vos nouveaux icônes métiers ou personnalisés
}

# Logos (exemple)
LOGOS = {
    "main": asset_path("logos", "dihya-main.svg"),
    "amazigh": asset_path("logos", "dihya-amazigh.svg"),
    "dark": asset_path("logos", "dihya-dark.svg"),
    "light": asset_path("logos", "dihya-light.svg"),
    "minimal": asset_path("logos", "dihya-minimal.svg"),
    "favicon": asset_path("logos", "favicon.svg"),
    "brandmark": asset_path("logos", "brandmark.svg"),
    "fr": asset_path("logos", "dihya-fr.svg"),
    "en": asset_path("logos", "dihya-en.svg"),
    "ar": asset_path("logos", "dihya-ar.svg"),
    "tzr": asset_path("logos", "dihya-tzr.svg"),
    "legal": asset_path("logos", "legal.svg"),
    "health": asset_path("logos", "health.svg"),
    "education": asset_path("logos", "education.svg"),
    # Ajoutez ici vos nouveaux logos métiers, plugins, ou personnalisés
}

# Images (exemple)
IMAGES = {
    "hero": asset_path("images", "hero.webp"),
    "demo": asset_path("images", "demo.png"),
    # Ajoutez ici vos images métiers ou UI
}

# Fonts (exemple)
FONTS = {
    "amazigh": asset_path("fonts", "lang-tzr.ttf"),
    "arabic": asset_path("fonts", "lang-ar.ttf"),
    "english": asset_path("fonts", "lang-en.ttf"),
    "french": asset_path("fonts", "lang-fr.ttf"),
    # Ajoutez ici vos polices métiers ou personnalisées
}

# Vidéos (exemple)
VIDEOS = {
    "demo_fr": asset_path("videos", "demo-fr.mp4"),
    "demo_en": asset_path("videos", "demo-en.mp4"),
    "demo_ar": asset_path("videos", "demo-ar.mp4"),
    "demo_tzr": asset_path("videos", "demo-tzr.mp4"),
    # Ajoutez ici vos vidéos métiers ou démos
}

# Templates métiers (exemple)
TEMPLATES = {
    "legal": asset_path("templates", "template-legal.json"),
    "health": asset_path("templates", "template-health.json"),
    "education": asset_path("templates", "template-education.json"),
    # Ajoutez ici vos templates métiers ou personnalisés
}

def get_asset(category: str, name: str) -> Optional[str]:
    """
    Récupère le chemin absolu d'un asset par catégorie et nom.
    :param category: icons, logos, images, fonts, videos, templates
    :param name: nom de l'asset
    :return: chemin absolu ou None
    """
    registry: Dict[str, Dict[str, str]] = {
        "icons": ICONS,
        "logos": LOGOS,
        "images": IMAGES,
        "fonts": FONTS,
        "videos": VIDEOS,
        "templates": TEMPLATES,
    }
    return registry.get(category, {}).get(name)

# Exemple d'utilisation CLI
if __name__ == "__main__":
    print("Dihya Assets Registry (Python)")
    for cat, reg in [("icons", ICONS), ("logos", LOGOS), ("images", IMAGES), ("fonts", FONTS), ("videos", VIDEOS), ("templates", TEMPLATES)]:
        print(f"\n{cat.upper()}:")
        for k, v in reg.items():
            print(f"  {k}: {v}")
    # Exemple d'accès
    print("\nExemple d'accès à un logo principal :", get_asset("logos", "main"))

# main.py – Dihya Assets Entrypoint

if __name__ == "__main__":
    print("Dihya Assets module – gestion des images, logos, icônes, polices, templates, branding, i18n.")
    # ...lancer les scripts d’import/export, de vérification, d’audit, etc.
