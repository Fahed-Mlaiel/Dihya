# schemas/ — Schémas de validation Backend Flask Dihya Coding

Ce dossier contient les schémas Marshmallow utilisés pour la sérialisation, la validation et la désérialisation des données dans l’API Flask Dihya Coding.

## Contenu

- **user.py** : Schéma de validation pour les utilisateurs (inscription, login, update, etc.).
- **__init__.py** : Initialisation du package schemas.

## Bonnes pratiques

- Utiliser Marshmallow pour tous les schémas de validation et de sérialisation.
- Documenter chaque schéma et chaque champ avec une docstring.
- Séparer les schémas de création, de mise à jour et de réponse (UserSchema, UserRegisterSchema, UserUpdateSchema, etc.).
- Ajouter des validations personnalisées pour les règles métier spécifiques.
- Ne jamais exposer de champs sensibles (ex : mot de passe) dans les schémas de sortie.

## Exemple d’utilisation

```python
from app.schemas.user import UserSchema

user_schema = UserSchema()
result = user_schema.load(request.json)  # Validation et désérialisation
## Exemple d'utilisation

```python
# Voir la documentation du module pour un exemple précis
```

