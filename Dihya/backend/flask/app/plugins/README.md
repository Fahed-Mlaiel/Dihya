# plugins/ — Extensibilité & Plugins Backend Dihya Coding

Ce dossier permet d’ajouter des plugins Python pour étendre dynamiquement les fonctionnalités du backend Flask Dihya Coding.

---

## Objectif

- Permettre l’ajout de fonctionnalités sans modifier le cœur du backend.
- Favoriser l’extensibilité, la modularité et la souveraineté logicielle.
- Garantir la sécurité, la conformité RGPD et la stabilité du projet lors de l’intégration de plugins tiers.

---

## Bonnes pratiques

- Chaque plugin doit être un module Python documenté, avec une docstring en tête de fichier.
- Les plugins doivent hériter de `GenerationPluginBase` et être validés/testés avant activation.
- Prévoir un mécanisme d’activation/désactivation (via config, variable d’environnement ou ACL).
- Ne jamais compromettre la sécurité, la confidentialité ou la stabilité du backend.
- Documenter les dépendances, hooks, options et points d’extension de chaque plugin.
- Respecter la licence AGPL et la charte Dihya Coding.
- Protéger toutes les routes exposées par les plugins via ACL, authentification et validation stricte.
- Logger les opérations critiques pour audit, traçabilité et conformité RGPD (jamais de données sensibles).
- Prévoir des tests unitaires et d’intégration pour chaque plugin.
- Prévoir la purge et l’export des logs liés aux plugins (conformité RGPD).
- Documenter les hooks disponibles (`before_generation`, `after_generation`, etc.).
- Versionner chaque plugin et documenter ses évolutions.

---

## Sécurité & conformité

- **Sandboxing** : tout code plugin doit être exécuté dans un environnement contrôlé.
- **Validation stricte** des entrées/sorties et des dépendances.
- **Auditabilité** : chaque action critique d’un plugin doit être loggée (sans fuite de données sensibles).
- **Extensibilité** : ajout de nouveaux plugins sans redémarrage du backend (hot reload possible).
- **Conformité RGPD** : logs anonymisés, purge/export sur demande, documentation claire.
- **Désactivation rapide** : tout plugin peut être désactivé en cas de faille ou de non-conformité.

---

## Exemple de structure de plugin

```python
"""
Plugin d’exemple pour Dihya Coding.
Décrit la fonctionnalité, les points d’extension et les dépendances.
"""
from app.plugins.generation_plugin import GenerationPluginBase

class ExamplePlugin(GenerationPluginBase):
    name = "Example"
    description = "Plugin d’exemple pour Dihya Coding."
    version = "1.0.0"
    author = "Dihya Team"
    safe = True

    def before_generation(self, needs):
        # Modifier les besoins avant génération
        return needs

    def after_generation(self, code, needs):
        # Enrichir le code généré
        return code