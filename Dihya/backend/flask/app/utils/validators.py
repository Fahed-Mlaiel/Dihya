"""
Utilitaires de validation pour l'application Dihya Coding.
Inclut : validation d'inscription, de connexion, de mise à jour utilisateur, etc.
"""

import re

def validate_email(email):
    """
    Valide le format d'un email.
    Args:
        email (str)
    Returns:
        bool
    """
    if not email:
        return False
    regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(regex, email) is not None

def validate_registration(data):
    """
    Valide les données d'inscription utilisateur.
    Args:
        data (dict)
    Returns:
        list: Liste d'erreurs, vide si aucune erreur
    """
    errors = []
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not email or not validate_email(email):
        errors.append("Email invalide ou manquant.")
    if not username or len(username) < 3:
        errors.append("Nom d'utilisateur trop court (min 3 caractères).")
    if not password or len(password) < 6:
        errors.append("Mot de passe trop court (min 6 caractères).")
    return errors

def validate_login(data):
    """
    Valide les données de connexion utilisateur.
    Args:
        data (dict)
    Returns:
        list: Liste d'erreurs, vide si aucune erreur
    """
    errors = []
    email = data.get("email")
    password = data.get("password")
    if not email or not validate_email(email):
        errors.append("Email invalide ou manquant.")
    if not password:
        errors.append("Mot de passe manquant.")
    return errors

def validate_user_update(data):
    """
    Valide les données de mise à jour utilisateur.
    Args:
        data (dict)
    Returns:
        list: Liste d'erreurs, vide si aucune erreur
    """
    errors = []
    if "email" in data and not validate_email(data["email"]):
        errors.append("Email invalide.")
    if "username" in data and len(data["username"]) < 3:
        errors.append("Nom d'utilisateur trop court (min 3 caractères).")
    return errors