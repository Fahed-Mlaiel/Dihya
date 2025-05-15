# i18n/ — Internationalisation (i18n) Dihya Coding

Ce dossier contient tous les fichiers et ressources nécessaires à l’internationalisation (i18n) et à la gestion multilingue du projet Dihya Coding.

## Contenu

- **en/** : Traductions et ressources pour l’anglais.
- **fr/** : Traductions et ressources pour le français.
- **other/** : Autres langues ou variantes.
- **README.md** : Documentation et bonnes pratiques i18n.

## Bonnes pratiques

- Organiser les fichiers de traduction par langue et par module si besoin.
- Utiliser des clés de traduction explicites et cohérentes.
- Prévoir un fallback (langue par défaut) en cas de clé manquante.
- Documenter la structure des fichiers de traduction.
- Mettre à jour les traductions à chaque ajout de fonctionnalité ou modification d’interface.
- Tester l’application dans chaque langue supportée.

## Exemple d’utilisation

```python
# Exemple d’utilisation d’une fonction utilitaire i18n côté backend
from app.utils.i18n import translate

message = translate("user.welcome", lang="fr")