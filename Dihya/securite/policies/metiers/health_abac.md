# Politique ABAC Santé

## Description
Gestion des accès basée sur les attributs pour les applications santé.

## Rôles
- admin
- médecin
- patient
- invité

## Attributs
- Statut du dossier
- Spécialité
- Consentement

## Exemples de règles
- Admin : accès total
- Médecin : accès à ses patients
- Patient : accès à ses données
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD, anonymisation

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('health')
def can_access_record(user, record):
    if user.role == 'admin':
        return True
    if user.role == 'médecin' and record.doctor_id == user.id:
        return True
    if user.role == 'patient' and record.patient_id == user.id:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
