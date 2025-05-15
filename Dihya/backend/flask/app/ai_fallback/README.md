# ai_fallback/ — Fallback IA open source Backend Dihya Coding

Ce dossier permet d’intégrer des modèles d’intelligence artificielle open source (ex : Mixtral, LLaMA, Mistral) pour servir de solution de repli (fallback) locale lorsque les APIs propriétaires (GPT, etc.) sont inaccessibles ou limitées.

## Objectif

- Garantir la souveraineté numérique et la continuité de service même en cas de coupure ou de blocage des APIs externes.
- Permettre l’utilisation de modèles IA open source compatibles avec le cahier des charges Dihya Coding.

## Bonnes pratiques

- Documenter chaque intégration de modèle IA (licence, version, dépendances).
- Sécuriser les échanges avec les modèles (pas de fuite de données sensibles).
- Prévoir un mécanisme de sélection automatique du backend IA selon la disponibilité (fallback transparent).
- Respecter les licences open source des modèles utilisés.
- Tester la robustesse et la performance de chaque fallback.

## Exemple d’utilisation

```python
from app.ai_fallback import get_fallback_response

response = get_fallback_response("Explique le concept de souveraineté numérique.", lang="fr")