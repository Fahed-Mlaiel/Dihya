# graphql/ — API GraphQL pour Dihya Coding

Ce dossier contient les schémas, résolveurs et scripts liés à l’API GraphQL du backend Dihya Coding.

## Objectif

- Offrir une alternative moderne à l’API REST pour la génération, la consultation et la gestion des projets.
- Permettre des requêtes flexibles et optimisées pour le frontend ou des intégrations tierces.

## Bonnes pratiques

- Définir les schémas GraphQL dans des fichiers dédiés et documentés.
- Sécuriser chaque requête/mutation (authentification, validation des rôles, contrôle d’accès).
- Logger les requêtes critiques pour audit.
- Ne jamais exposer de données sensibles ou de secrets via GraphQL.
- Prévoir des tests unitaires pour chaque résolveur.
- Documenter chaque type, requête et mutation dans ce dossier.

## Structure recommandée

- `schema.py` : schéma principal GraphQL (types, queries, mutations)
- `resolvers.py` : fonctions de résolution des queries/mutations (logique métier)
- `README.md` : documentation et exemples d’utilisation

## Exemple d’utilisation (Flask + Graphene)

```python
from flask import Flask
from flask_graphql import GraphQLView
from app.graphql.schema import schema

app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)
```

## Sécurité

- Protéger l’endpoint `/graphql` par authentification JWT ou OAuth2.
- Limiter la profondeur des requêtes et la taille des réponses pour éviter les abus.
- Valider toutes les entrées côté serveur avant toute mutation.
- Logger chaque mutation ou accès critique pour audit et souveraineté.

## Tests

- Prévoir des tests unitaires pour chaque résolveur et mutation.
- Simuler des scénarios d’accès non autorisé et de validation d’entrée.

## Documentation

- Documenter chaque type, champ, requête et mutation dans `schema.py` et `resolvers.py` via docstrings.
- Ajouter des exemples de requêtes GraphQL dans ce README si besoin.

---

**Équipe Dihya Coding**