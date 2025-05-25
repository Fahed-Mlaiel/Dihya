# Politique ABAC Énergie

## Description
Gestion des accès basée sur les attributs pour les applications du secteur énergie.

## Rôles
- admin
- opérateur
- client
- invité

## Attributs
- Type d'énergie
- Localisation
- Statut de contrat

## Exemples de règles
- Admin : accès total
- Opérateur : gestion de ses sites
- Client : accès à ses données
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('energie')
def can_access_site(user, site):
    if user.role == 'admin':
        return True
    if user.role == 'opérateur' and site.operator_id == user.id:
        return True
    if user.role == 'client' and site.client_id == user.id:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
