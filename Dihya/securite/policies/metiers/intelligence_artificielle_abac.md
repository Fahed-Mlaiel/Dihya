# Politique ABAC Intelligence Artificielle

## Description
Gestion des accès basée sur les attributs pour les applications IA.

## Rôles
- admin
- data scientist
- utilisateur
- invité

## Attributs
- Statut du projet
- Type de modèle
- Statut de l'utilisateur

## Exemples de règles
- Admin : accès total
- Data scientist : gestion de ses projets
- Utilisateur : accès à ses projets
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('intelligence_artificielle')
def can_access_ai_project(user, project):
    if user.role == 'admin':
        return True
    if user.role == 'data scientist' and project.owner_id == user.id:
        return True
    if user.role == 'utilisateur' and user.id in project.user_ids:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
