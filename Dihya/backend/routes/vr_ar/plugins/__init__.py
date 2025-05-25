"""
Initialisation du système de plugins VR/AR (Dihya)
Chargement dynamique, extension via API/CLI, sécurité, audit, multilingue.
"""

PLUGINS = {}

def register_plugin(name, plugin):
    PLUGINS[name] = plugin

def get_plugin(name):
    return PLUGINS.get(name)
