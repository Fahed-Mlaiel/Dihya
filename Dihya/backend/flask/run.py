"""
Point d'entrée pour lancer l'application Flask Dihya Coding.
Charge la configuration, initialise l'app et lance le serveur.
"""

import os
from app import create_app

if __name__ == "__main__":
    # Charge la configuration depuis la variable d'environnement ou par défaut
    config_path = os.environ.get("DIHYA_CONFIG", "backend.config.Config")
    app = create_app(config_path)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)