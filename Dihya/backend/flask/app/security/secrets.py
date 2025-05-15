"""
Gestion sécurisée des secrets pour Dihya Coding.

Ce module centralise la gestion, le chargement et la validation des secrets applicatifs (clés API, tokens, credentials, etc.)
pour garantir la sécurité, la traçabilité et la conformité RGPD.

Bonnes pratiques :
- Ne jamais stocker de secrets en dur dans le code source.
- Charger les secrets depuis des variables d’environnement ou des fichiers sécurisés.
- Valider la présence et le format des secrets au démarrage de l’application.
- Protéger l’accès aux secrets (permissions, audit).
- Ne jamais logguer ou exposer de secrets en clair.
- Prévoir des tests unitaires pour la gestion des secrets.

Exemple d’utilisation :
    from app.security.secrets import get_secret

    api_key = get_secret("SENDGRID_API_KEY")
"""

import os
from typing import Optional


class SecretNotFound(Exception):
    """Exception levée lorsqu'un secret requis est manquant ou invalide."""
    pass


def get_secret(name: str, default: Optional[str] = None, required: bool = True) -> str:
    """
    Récupère un secret depuis les variables d'environnement.

    Args:
        name (str): Nom de la variable d'environnement.
        default (Optional[str]): Valeur par défaut si le secret n'est pas trouvé.
        required (bool): Si True, lève une exception si le secret est absent.

    Returns:
        str: Valeur du secret.

    Raises:
        SecretNotFound: Si le secret est requis et absent.
    """
    value = os.environ.get(name, default)
    if required and (value is None or value == ""):
        raise SecretNotFound(f"Le secret '{name}' est requis mais n'est pas défini.")
    return value


def validate_secrets(required_secrets: list):
    """
    Valide la présence de tous les secrets requis au démarrage de l'application.

    Args:
        required_secrets (list): Liste des noms de secrets à valider.

    Raises:
        SecretNotFound: Si un secret requis est absent.
    """
    for secret in required_secrets:
        get_secret(secret, required=True)


# Exemple d'utilisation au démarrage de l'app :
# validate_secrets(["JWT_SECRET_KEY", "SENDGRID_API_KEY", "DATABASE_URL"])