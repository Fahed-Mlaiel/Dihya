# Politique ABAC pour la gestion VR/AR

## Objectif
Définir les règles d'accès basées sur les attributs pour les modules VR/AR (création, visualisation, interaction, IA).

## Attributs principaux
- `role` : admin, user, invité
- `lang` : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
- `tenant_id` : identifiant du locataire
- `verified` : true/false
- `project_type` : vr, ar, ia

## Règles d'accès
- **Admin** : accès total à toutes les fonctions, logs, audit, configuration.
- **User** : accès aux fonctions standards, logs anonymisés, configuration limitée.
- **Invité** : accès lecture seule, aucune configuration, logs anonymisés.
- **Tenant** : isolation stricte des données et logs par tenant.
- **Sécurité** : authentification JWT, audit, validation, anti-abus.

## Exemples de règles YAML
```yaml
- effect: allow
  action: [vr_ar:read, vr_ar:create, vr_ar:interact]
  condition:
    role: [admin, user]
    verified: true
- effect: deny
  action: [vr_ar:configure]
  condition:
    role: invité
```

## Auditabilité
- Tous les accès sont logués, exportables, anonymisables.
- Conformité RGPD.
