"""
Initialisation du module de gestion de la configuration dynamique pour Dihya Coding.

Ce package centralise la gestion, la validation et le chargement des paramètres dynamiques de l’application
(feature flags, paramètres runtime, configuration multi-environnement, etc.).

Bonnes pratiques :
- Déclarer chaque type de configuration dans un fichier dédié (ex : feature_flags.py, runtime_config.py).
- Valider systématiquement les valeurs chargées (types, plages, sécurité).
- Ne jamais stocker de secrets en clair dans la configuration.
- Prévoir des tests unitaires pour chaque helper de configuration.
- Documenter chaque paramètre configurable (usage, valeurs possibles, sécurité).
- Permettre la surcharge par variables d’environnement pour la portabilité.

Exemple d’import :
    from app.configuration.feature_flags import is_feature_enabled
    from app.configuration.runtime_config import get_config_value
"""
# Exemple d’import automatique (à compléter selon les fichiers créés)
# from .feature_flags import is_feature_enabled
# from .runtime_config import get_config_value