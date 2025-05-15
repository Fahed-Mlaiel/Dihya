# realtime/ — WebSockets & Temps réel Backend Dihya Coding

Ce dossier contient les modules et scripts pour la gestion des fonctionnalités temps réel (WebSockets, notifications push, live updates) dans le backend Flask de Dihya Coding.

## Objectif

- Permettre la communication bidirectionnelle en temps réel (chat, notifications, collaboration, etc.).
- Offrir une expérience utilisateur moderne et interactive sur la plateforme.

## Bonnes pratiques

- Utiliser des bibliothèques éprouvées (ex : Flask-SocketIO) pour la gestion des WebSockets.
- Sécuriser chaque connexion (authentification JWT/session, contrôle d’accès, validation des messages).
- Logger chaque événement critique (connexion, déconnexion, message) avec horodatage.
- Ne jamais transmettre de données sensibles ou de secrets via les canaux temps réel.
- Prévoir des tests unitaires et d’intégration pour les handlers temps réel.
- Documenter chaque événement et message supporté dans ce dossier.

## Structure recommandée

- `server.py` : serveur Flask-SocketIO (initialisation, configuration, sécurité)
- `events.py` : gestion des événements WebSocket (handlers, validation, logging)
- `README.md` : documentation et exemples d’utilisation

## Exemple d’utilisation (Flask-SocketIO)

```python
from flask_socketio import SocketIO, emit
from app.realtime.events import register_socketio_events

socketio = SocketIO(app, cors_allowed_origins="*")
register_socketio_events(socketio)

@socketio.on('message')
def handle_message(data):
    emit('response', {'data': data}, broadcast=True)
```

## Sécurité

- Authentifier chaque client WebSocket (JWT, session…).
- Limiter les permissions selon le rôle utilisateur.
- Valider et filtrer tous les messages entrants.
- Logger chaque connexion, déconnexion et événement critique pour audit.

## Tests

- Prévoir des tests unitaires pour chaque handler d’événement.
- Simuler des scénarios d’accès non autorisé et de validation de message.

## Documentation

- Documenter chaque événement supporté dans `events.py` via docstrings.
- Ajouter des exemples de payloads et de flux temps réel dans ce README si besoin.

---

**Équipe Dihya Coding**