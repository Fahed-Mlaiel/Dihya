# Politique ABAC IT/DevOps

## Description
Gestion des accès basée sur les attributs pour les applications IT/DevOps.

## Rôles
- admin
- devops
- développeur
- invité

## Attributs
- Statut du projet
- Type d'environnement
- Statut de l'utilisateur

## Exemples de règles
- Admin : accès total
- DevOps : gestion de ses environnements
- Développeur : accès à ses projets
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('it_devops')
def can_access_env(user, env):
    if user.role == 'admin':
        return True
    if user.role == 'devops' and env.owner_id == user.id:
        return True
    if user.role == 'développeur' and user.id in env.developer_ids:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
