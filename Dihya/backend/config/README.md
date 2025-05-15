# config/ — Configuration Backend Dihya Coding

Ce dossier contient les fichiers de configuration Python pour le backend Flask.

## Contenu

- **\_\_init\_\_.py** : Initialisation du package de configuration.
- (Ajouter ici d'autres fichiers de configuration si besoin, ex : `production.py`, `development.py`, etc.)
- **secrets_example.md** : Exemple et bonnes pratiques pour la gestion des secrets.

## Bonnes pratiques

- Centraliser toutes les variables de configuration (base de données, sécurité, mail, etc.) dans ce dossier.
- Ne jamais stocker de secrets ou mots de passe en clair dans le code : utiliser les variables d’environnement.
- Prévoir plusieurs fichiers de config si besoin (développement, production, test).
- Documenter chaque variable de configuration importante.
- Utiliser des classes de configuration pour faciliter la surcharge et l’extension.
- Ajouter un exemple de fichier `.env` et l’exclure du versionnement (`.gitignore`).

## Exemple d’utilisation

```python
from backend.config import Config

app.config.from_object(Config)
```

## Sécurité

- Toujours charger les secrets via les variables d’environnement ou un gestionnaire de secrets.
- Ne jamais exposer les valeurs de configuration sensibles dans les logs ou les erreurs.
- Restreindre l’accès aux fichiers de configuration contenant des chemins ou infos critiques.

---

**Équipe Dihya Coding**