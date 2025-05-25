# Politique ABAC Éducation

## Description
Politique d'accès basée sur les attributs pour les applications éducatives.

## Rôles
- admin
- enseignant
- élève
- invité

## Attributs
- Statut d'inscription
- Niveau scolaire
- Langue
- Groupe

## Exemples de règles
- Un admin a tous les droits.
- Un enseignant accède à ses classes.
- Un élève accède à ses cours.
- Un invité a un accès limité.

## Sécurité
- JWT, CORS, validation stricte, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('education')
def can_access_course(user, course):
    if user.role == 'admin':
        return True
    if user.role == 'enseignant' and course.teacher_id == user.id:
        return True
    if user.role == 'élève' and user.id in course.student_ids:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
