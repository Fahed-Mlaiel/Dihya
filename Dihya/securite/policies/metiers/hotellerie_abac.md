# Politique ABAC Hôtellerie

## Description
Gestion des accès basée sur les attributs pour les applications hôtelières.

## Rôles
- admin
- manager
- client
- invité

## Attributs
- Statut de réservation
- Type de chambre
- Statut du client

## Exemples de règles
- Admin : accès total
- Manager : gestion de ses hôtels
- Client : accès à ses réservations
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('hotellerie')
def can_access_booking(user, booking):
    if user.role == 'admin':
        return True
    if user.role == 'manager' and booking.manager_id == user.id:
        return True
    if user.role == 'client' and booking.client_id == user.id:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
