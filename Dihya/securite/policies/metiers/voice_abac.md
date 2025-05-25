# Politique ABAC pour la gestion vocale (Voice)

## Objectif
Définir les règles d'accès basées sur les attributs (ABAC) pour les fonctionnalités vocales (reconnaissance, synthèse, commandes) dans Dihya.

## Attributs principaux
- `role` : admin, user, invité
- `lang` : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
- `project_type` : ia, vr, ar, voice, voyage
- `tenant_id` : identifiant du locataire
- `verified` : true/false

## Règles d'accès
- **Admin** : accès total à toutes les fonctions vocales, logs, audit, configuration.
- **User** : accès aux fonctions vocales standards, logs anonymisés, configuration limitée.
- **Invité** : accès lecture seule, aucune configuration, logs anonymisés.
- **Langue** : accès restreint selon la langue supportée par le projet.
- **Tenant** : isolation stricte des données et logs par tenant.
- **Sécurité** : toutes les requêtes doivent être authentifiées (JWT), auditables, et validées (anti-injection, anti-abus).

## Exemples de règles YAML
```yaml
- effect: allow
  action: [voice:read, voice:transcribe, voice:synthesize]
  condition:
    role: [admin, user]
    lang: [fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es]
    verified: true
- effect: deny
  action: [voice:configure]
  condition:
    role: invité
```

## Auditabilité
- Tous les accès sont logués, exportables, et anonymisables.
- Conformité RGPD assurée.
