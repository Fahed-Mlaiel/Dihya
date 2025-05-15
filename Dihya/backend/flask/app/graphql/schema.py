"""
Schéma principal GraphQL pour Dihya Coding.

Ce module définit les types, requêtes et mutations exposés par l’API GraphQL du backend.
Il centralise la sécurité (authentification, rôles), la validation et la documentation des opérations.

Bonnes pratiques :
- Documenter chaque type, champ, requête et mutation.
- Protéger les mutations sensibles par authentification et contrôle de rôle.
- Valider toutes les entrées côté serveur.
- Ne jamais exposer de données sensibles dans les erreurs ou réponses.
- Séparer la logique métier dans les resolvers/services.

Exemple d’utilisation :
    from app.graphql.schema import schema
    app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))
"""

import graphene
from graphene import ObjectType, String, Field, Int, Boolean, List
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

# Exemple de type User
class UserType(graphene.ObjectType):
    id = Int()
    email = String()
    role = String()

# Décorateur pour sécuriser les mutations/queries (JWT)
def jwt_required_graphql(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper

# Query principale
class Query(ObjectType):
    hello = String(description="Test de disponibilité GraphQL")
    me = Field(UserType, description="Retourne l'utilisateur courant (JWT requis)")

    def resolve_hello(parent, info):
        return "Bienvenue sur l’API GraphQL Dihya Coding !"

    @jwt_required_graphql
    def resolve_me(parent, info):
        user_id = get_jwt_identity()
        # TODO: Récupérer l'utilisateur depuis la base (exemple fictif)
        return UserType(id=user_id, email="user@dihya.dev", role="user")

# Mutation d’exemple (création de projet)
class CreateProject(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        type = String(required=True)

    ok = Boolean()
    project_id = Int()
    message = String()

    @jwt_required_graphql
    def mutate(self, info, name, type):
        # TODO: Ajouter la logique de création réelle (validation, audit, etc.)
        # Exemple fictif :
        project_id = 123
        return CreateProject(ok=True, project_id=project_id, message="Projet créé avec succès.")

class Mutation(ObjectType):
    create_project = CreateProject.Field(description="Créer un nouveau projet (JWT requis)")

# Schéma principal
schema = graphene.Schema(query=Query, mutation=Mutation)