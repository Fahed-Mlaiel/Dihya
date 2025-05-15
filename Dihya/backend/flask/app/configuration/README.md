# configuration/ — Gestion dynamique de la configuration (Dihya Coding)

Ce dossier centralise la gestion, la validation et le chargement des paramètres dynamiques pour le backend Flask Dihya Coding.

## Objectif

- Permettre une configuration flexible et sécurisée de l’application (feature flags, runtime, multi-environnement, etc.).
- Faciliter la surcharge par variables d’environnement pour la portabilité et la sécurité.
- Garantir la traçabilité et la documentation de chaque paramètre configurable.

## Bonnes pratiques

- Déclarer chaque type de configuration dans un fichier dédié (`feature_flags.py`, `runtime_config.py`, etc.).
- Valider systématiquement les valeurs chargées (types, plages, sécurité).
- Ne jamais stocker de secrets en clair dans la configuration.
- Documenter chaque paramètre configurable (usage, valeurs possibles, sécurité).
- Prévoir des tests unitaires pour chaque helper de configuration.
- Permettre la surcharge par variables d’environnement et fichiers `.env`.

## Exemple de structure

- `feature_flags.py` : gestion des fonctionnalités activables/désactivables dynamiquement.
- `runtime_config.py` : gestion des paramètres runtime (timeouts, quotas, etc.).
- `env_config.py` : helpers pour charger et valider les variables d’environnement.

## Exemple d’utilisation

```python
from app.configuration.feature_flags import is_feature_enabled
from app.configuration.runtime_config import get_config_value

if is_feature_enabled("NEW_DASHBOARD"):
    # Afficher la nouvelle interface
timeout = get_config_value("REQUEST_TIMEOUT", default=30)