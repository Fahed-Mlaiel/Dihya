# services/ — Services Backend Flask Dihya Coding

Ce dossier regroupe les services métiers et techniques utilisés par le backend Flask de Dihya Coding.

## Contenu

- **auth_service.py** : Service d'authentification (gestion JWT, login, refresh, logout, sécurité).
- **mail.py** : Service d'envoi d'e-mails (abstraction Flask-Mail, notifications, confirmation, reset password).
- **user_service.py** : Service de gestion des utilisateurs (CRUD, rôles, profil, sécurité).
- **notifications.py** : Service centralisé d’envoi de notifications (email, webhook, interne).
- **social_auth.py** : Service d’authentification sociale (OAuth2, Google, GitHub…).

## Bonnes pratiques

- Chaque service doit être documenté avec une docstring en tête de fichier et pour chaque fonction.
- Les services doivent encapsuler la logique métier réutilisable (pas de logique métier dans les routes).
- Séparer clairement la logique métier, la validation et l'accès aux données.
- Prévoir des exceptions personnalisées pour la gestion des erreurs métier.
- Ajouter des tests unitaires pour chaque service critique.
- Ne jamais exposer de secrets ou de données sensibles dans les logs ou les erreurs.
- Logger chaque opération critique avec horodatage pour audit et souveraineté.

## Exemple d'utilisation

```python
from app.services.auth_service import authenticate_user, generate_token

user = authenticate_user(email, password)
token = generate_token(user)

from app.services.notifications import send_notification
send_notification("alice@dihya.dev", "Bienvenue sur Dihya !", channel="email")
```

## Sécurité

- Toujours valider les entrées et sécuriser les accès dans chaque service.
- Utiliser les variables d’environnement pour les secrets et credentials.
- Documenter chaque ajout ou modification de service pour faciliter la maintenance.

---

**Équipe Dihya Coding**