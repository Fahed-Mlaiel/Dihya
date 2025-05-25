# Métier : Tourisme

## Présentation
Le module Tourisme de Dihya permet la gestion avancée de projets touristiques (sites, événements, guides, réservations, IA, VR/AR, etc.) avec sécurité, conformité RGPD, internationalisation et extensibilité.

## Routes API REST/GraphQL
- `GET /api/tourisme/sites` : Liste des sites touristiques (filtrage, pagination, i18n)
- `POST /api/tourisme/sites` : Création d’un site (validation, rôles, audit)
- `GET /api/tourisme/sites/{id}` : Détail d’un site (SEO, logs, multilingue)
- `PUT /api/tourisme/sites/{id}` : Modification (admin, audit, RGPD)
- `DELETE /api/tourisme/sites/{id}` : Suppression (anonymisation, export, logs)
- `POST /graphql` : Support GraphQL (requêtes personnalisées, sécurité JWT)

## Sécurité
- CORS strict, JWT, WAF, anti-DDOS, audit logging, RBAC (admin/user/invité)
- Plugins de sécurité activables via API/CLI

## Internationalisation
- Support dynamique : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
- Traductions automatiques IA fallback open source (LLaMA, Mixtral, Mistral)

## Exemples d’intégration IA/VR/AR
- Génération de visites virtuelles (VR/AR)
- Recommandations IA personnalisées (fallback open source)

## RGPD & Auditabilité
- Export/anonymisation des données
- Logs structurés, accès exportable, conformité totale

## Extensibilité
- Système de plugins (ajout de modules via API/CLI)
- Exemples : plugin météo, plugin réservation, plugin analyse IA

## Tests & Déploiement
- Couverture unitaire, intégration, e2e
- Déploiement GitHub Actions, Docker, K8s, fallback local

## Exemple de plugin
```python
"""Plugin météo pour le tourisme (exemple, extensible)"""
def get_weather(site_id: int, lang: str = 'fr') -> dict:
    """Retourne la météo pour un site touristique (i18n, sécurisé, loggé)"""
    # ...implémentation...
    return {"temp": 22, "desc": "Ensoleillé"}
```

## Documentation intégrée
- Chaque route, module, plugin est documenté (docstring, type hints, exemples)

## Accessibilité & SEO
- Respect WCAG, sitemap dynamique, robots.txt, logs SEO

## Structure prête à l’emploi
- Code, tests, assets, configs, docs, plugins, policies, etc.
