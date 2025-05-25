# Politique ABAC Immobilier

## Description
Gestion des accès basée sur les attributs pour les applications immobilières.

## Rôles
- admin
- agent
- client
- invité

## Attributs
- Statut du bien
- Type de bien
- Statut du client

## Exemples de règles
- Admin : accès total
- Agent : gestion de ses biens
- Client : accès à ses dossiers
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('immobilier')
def can_access_property(user, property):
    if user.role == 'admin':
        return True
    if user.role == 'agent' and property.agent_id == user.id:
        return True
    if user.role == 'client' and property.client_id == user.id:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
