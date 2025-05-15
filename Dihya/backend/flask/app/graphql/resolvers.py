"""
Resolvers GraphQL pour Dihya Coding.

Ce module centralise la logique métier des queries et mutations GraphQL.
Il sépare la logique d’accès aux données, la validation et la sécurité des schémas.

Bonnes pratiques :
- Valider toutes les entrées côté serveur.
- Protéger les mutations sensibles par authentification et contrôle de rôle.
- Logger chaque action critique pour audit.
- Ne jamais exposer de données sensibles dans les erreurs ou réponses.
- Utiliser les services métiers pour la logique métier (pas d’accès direct à la base ici).

Exemple d’utilisation :
    from app.graphql.resolvers import resolve_me, resolve_create_project
"""

from app.services.user_service import get_user_by_id
from app.services.auth_service import register_user
from app.services import register_user as service_register_user

def resolve_me(user_id):
    """
    Résout la query 'me' pour retourner les infos de l'utilisateur courant.
    :param user_id: ID de l'utilisateur courant (int)
    :return: dict ou None
    """
    user = get_user_by_id(user_id)
    if not user:
        return None
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role
    }

def resolve_create_project(user_id, name, type):
    """
    Résout la mutation 'create_project' pour créer un projet.
    :param user_id: ID de l'utilisateur courant (int)
    :param name: nom du projet (str)
    :param type: type de projet (str)
    :return: dict (ok, project_id, message)
    """
    # TODO: Ajouter validation, audit, appel au service métier réel
    # Exemple fictif :
    project_id = 123  # À remplacer par l’ID réel du projet créé
    # Logger l’action ici si besoin
    return {
        "ok": True,
        "project_id": project_id,
        "message": "Projet créé avec succès."
    }