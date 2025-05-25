# Politique ABAC Juridique

## Description
Gestion des accès basée sur les attributs pour les applications juridiques.

## Rôles
- admin
- avocat
- client
- invité

## Attributs
- Statut du dossier
- Type de dossier
- Statut du client

## Exemples de règles
- Admin : accès total
- Avocat : gestion de ses dossiers
- Client : accès à ses dossiers
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('juridique')
def can_access_case(user, case):
    if user.role == 'admin':
        return True
    if user.role == 'avocat' and case.lawyer_id == user.id:
        return True
    if user.role == 'client' and case.client_id == user.id:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
