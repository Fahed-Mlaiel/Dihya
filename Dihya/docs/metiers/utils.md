# Métier : Utils (Utilitaires)

## Présentation
Le module Utils regroupe les fonctions utilitaires transverses (validation, conversion, logs, sécurité, i18n, plugins, audit, RGPD).

## Fonctions principales
- Validation de données (types, schémas, RGPD)
- Conversion d’unités, formats, monnaies (i18n, logs)
- Génération d’identifiants uniques (sécurisé, audit)
- Outils de logs structurés (SEO, accessibilité)

## Sécurité
- CORS, JWT, WAF, audit logging, RBAC
- Plugins sécurité (ex : anti-injection, anti-fraude)

## Internationalisation
- Support multilingue dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Traductions IA open source fallback

## Exemples d’intégration IA
- Validation intelligente (fallback LLaMA, Mixtral, Mistral)
- Suggestions automatiques

## RGPD & Auditabilité
- Anonymisation, export, logs structurés

## Extensibilité
- Plugins (ex : plugin conversion devise, plugin validation IA)

## Exemple de fonction utilitaire
```python
"""Validation d’email (exemple, extensible, sécurisé)"""
from typing import Optional
import re

def validate_email(email: str) -> Optional[str]:
    """Valide un email (RGPD, log, i18n)"""
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return email
    return None
```

## Documentation intégrée
- Docstring, type hints, exemples

## Structure prête à l’emploi
- Code, tests, assets, configs, docs, plugins, policies, etc.
