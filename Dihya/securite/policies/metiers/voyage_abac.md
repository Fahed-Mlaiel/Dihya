# Politique ABAC pour la gestion des voyages (Voyage)

## Objectif
Définir les règles d'accès basées sur les attributs pour les modules de gestion de voyages (réservation, planification, IA, VR, AR).

## Attributs principaux
- `role` : admin, user, invité
- `lang` : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
- `tenant_id` : identifiant du locataire
- `verified` : true/false
- `project_type` : voyage, ia, vr, ar

## Règles d'accès
- **Admin** : accès total à toutes les fonctions, logs, audit, configuration.
- **User** : accès aux fonctions standards, logs anonymisés, configuration limitée.
- **Invité** : accès lecture seule, aucune configuration, logs anonymisés.
- **Tenant** : isolation stricte des données et logs par tenant.
- **Sécurité** : authentification JWT, audit, validation, anti-abus.

## Exemples de règles YAML
```yaml
- effect: allow
  action: [voyage:read, voyage:book, voyage:plan]
  condition:
    role: [admin, user]
    verified: true
- effect: deny
  action: [voyage:configure]
  condition:
    role: invité
```

## Auditabilité
- Tous les accès sont logués, exportables, anonymisables.
- Conformité RGPD.
