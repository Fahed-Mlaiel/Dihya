"""
Module pour la traçabilité et l’horodatage des générations de code dans Dihya Coding.

Ce package permet de journaliser chaque génération de projet (frontend, backend, assets, etc.)
avec un log horodaté, le type de génération, l’utilisateur (si applicable) et les métadonnées associées.

Bonnes pratiques :
- Chaque log doit inclure la date, l’heure, le type de génération, l’auteur (si connu) et un identifiant unique.
- Ne jamais stocker de secrets ou de données sensibles dans les logs.
- Prévoir une rotation et une purge régulière des logs.
- Les logs doivent être accessibles uniquement aux administrateurs ou à des fins d’audit.

Exemple d’utilisation :
    from generation_logs import log_generation_event
    log_generation_event("backend", user="alice", meta={"stack": "Flask"})

"""

import os
from datetime import datetime
import json
import uuid

LOG_FILE = os.getenv("GENERATION_LOG_FILE", "logs/generation.log")

def log_generation_event(event_type, user=None, meta=None):
    """
    Journalise un événement de génération de code.
    :param event_type: Type de génération (ex: backend, frontend, ia, etc.)
    :param user: Utilisateur à l’origine de la génération (optionnel)
    :param meta: Dictionnaire de métadonnées complémentaires (optionnel)
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "user": user,
        "meta": meta or {}
    }
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")