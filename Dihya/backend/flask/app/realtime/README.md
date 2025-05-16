# realtime/ — WebSockets & Temps réel Backend Dihya Coding

Ce dossier contient les modules et scripts pour la gestion des fonctionnalités temps réel (WebSockets, notifications push, live updates) dans le backend Flask de Dihya Coding.

---

## Objectif

- Permettre la communication bidirectionnelle en temps réel (chat, notifications, collaboration, etc.).
- Offrir une expérience utilisateur moderne et interactive sur la plateforme.
- Garantir la sécurité, la conformité RGPD et la traçabilité des échanges temps réel.

---

## Bonnes pratiques

- Utiliser des bibliothèques éprouvées (ex : Flask-SocketIO) pour la gestion des WebSockets.
- Sécuriser chaque connexion : authentification JWT/session, contrôle d’accès, validation stricte des messages.
- Logger chaque événement critique (connexion, déconnexion, message) avec horodatage, sans jamais inclure de données sensibles.
- Ne jamais transmettre de secrets, tokens ou données confidentielles via les canaux temps réel.
- Prévoir des tests unitaires et d’intégration pour chaque handler temps réel.
- Documenter chaque événement, message et payload supporté dans ce dossier.
- Prévoir la purge et l’export des logs temps réel pour conformité RGPD.

---

## Structure recommandée

- `server.py` : serveur Flask-SocketIO (initialisation, configuration, sécurité, CORS)
- `events.py` : gestion des événements WebSocket (handlers, validation, logging, documentation)
- `README.md` : documentation, bonnes pratiques et exemples d’utilisation

---

## Exemple d’utilisation (Flask-SocketIO)

```python
from flask_socketio import SocketIO, emit
from app.realtime.events import register_socketio_events

socketio = SocketIO(app, cors_allowed_origins="*")
register_socketio_events(socketio)

@socketio.on('message')
def handle_message(data):
    # Validation et sanitation du message avant diffusion
    emit('response', {'data': data}, broadcast=True)