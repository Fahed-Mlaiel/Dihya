# quotas/ — Gestion des quotas API & fallback IA (Dihya Coding)

Ce dossier contient les outils et scripts pour surveiller l’utilisation des APIs propriétaires (ex : GPT), détecter les dépassements de quotas et rediriger automatiquement les requêtes vers des modèles IA open source (Mixtral, LLaMA, etc.) en fallback.

## Objectif

- Garantir la continuité de service même en cas de dépassement de quotas ou d’indisponibilité des APIs externes.
- Assurer la souveraineté numérique et la résilience du backend Dihya Coding.

## Bonnes pratiques

- Journaliser chaque dépassement de quota et chaque bascule en fallback pour audit.
- Ne jamais exposer de données sensibles dans les logs ou lors de la gestion des quotas.
- Prévoir une configuration souple des seuils de quotas et des priorités de fallback (variables d’environnement).
- Tester la robustesse et la rapidité du mécanisme de redirection.
- Respecter les licences open source des modèles utilisés en fallback.

## Exemple d’utilisation

```python
from app.ai_fallback.quotas import check_and_route

response = check_and_route("Explique la souveraineté numérique.", lang="fr")