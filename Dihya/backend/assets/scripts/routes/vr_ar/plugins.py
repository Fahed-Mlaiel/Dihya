"""
Dihya Backend – Plugins dynamiques IA/VR/AR
Exemples de plugins extensibles, chargement dynamique, sécurité, RGPD, audit, i18n.
"""
from typing import List, Dict

PLUGINS: List[Dict] = [
    {"name": "audit_logger", "enabled": True, "config": {"level": "INFO"}},
    {"name": "rgpd_export", "enabled": True, "config": {"anonymize": True}},
    {"name": "llama_fallback", "enabled": True, "config": {"model": "LLaMA3"}},
]

def get_active_plugins() -> List[Dict]:
    return [p for p in PLUGINS if p["enabled"]]

# ... possibilité d'ajouter dynamiquement des plugins via API/CLI ...
