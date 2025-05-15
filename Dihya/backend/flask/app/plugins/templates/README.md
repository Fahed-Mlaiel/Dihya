# templates/ — Templates intelligents par domaine (Dihya Coding)

Ce dossier contient les templates dynamiques utilisés pour la génération automatique de projets selon le domaine métier (e-commerce, éducation, social, etc.).

## Objectif

- Offrir des bases de code et de structure adaptées à chaque secteur d’activité.
- Permettre la personnalisation et l’extension sans modifier le cœur du backend.
- Garantir la sécurité, la modularité et la souveraineté logicielle.

## Bonnes pratiques

- Chaque template doit être documenté (fonction, structure, dépendances, domaine visé).
- Versionner chaque template pour assurer la traçabilité des évolutions.
- Valider la conformité métier, sécurité et accessibilité de chaque template.
- Prévoir un mécanisme de sélection automatique du template selon le domaine détecté (`get_template_for_domain`).
- Permettre l’ajout de nouveaux templates par simple ajout de fichier/module dans ce dossier.
- Ne jamais inclure de secrets, d’identifiants ou de données sensibles dans les templates.
- Prévoir des tests unitaires pour chaque template critique.

## Exemple de structure de template

```python
"""
Template e-commerce pour Dihya Coding.
Inclut la structure de base, les routes, les modèles et les bonnes pratiques du secteur.
"""
def get_template():
    """
    Retourne la structure du template e-commerce.
    :return: dict ou str représentant le squelette du projet e-commerce
    """
    # Exemple fictif
    return {
        "routes": ["/products", "/cart", "/checkout"],
        "models": ["Product", "Order", "User"],
        "dependencies": ["stripe", "sqlalchemy"],
        "description": "Template e-commerce prêt à l’emploi"
    }
```

## Sécurité

- Vérifier chaque dépendance et composant inclus dans les templates.
- Ne jamais exposer de données sensibles ou de configuration critique.
- Documenter les points de personnalisation et d’extension.

---

**Équipe Dihya Coding**