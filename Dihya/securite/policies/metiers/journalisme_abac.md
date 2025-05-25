# Politique ABAC Journalisme

## Description
Gestion des accès basée sur les attributs pour les applications de journalisme.

## Rôles
- admin
- journaliste
- lecteur
- invité

## Attributs
- Statut de l'article
- Type de contenu
- Statut du lecteur

## Exemples de règles
- Admin : accès total
- Journaliste : gestion de ses articles
- Lecteur : accès à ses abonnements
- Invité : accès limité

## Sécurité
- JWT, CORS, validation, audit, RGPD

## I18n
- fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es

## Exemple Python
```python
@policy('journalisme')
def can_access_article(user, article):
    if user.role == 'admin':
        return True
    if user.role == 'journaliste' and article.author_id == user.id:
        return True
    if user.role == 'lecteur' and user.id in article.reader_ids:
        return True
    return False
```

## Extensible, auditable, RGPD, plugins.
