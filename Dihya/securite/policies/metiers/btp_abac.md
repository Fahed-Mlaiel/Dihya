# Politique ABAC BTP

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications BTP (chantier, gestion projet, sécurité, etc.).

## Attributs principaux
- Rôle utilisateur (admin, chef de projet, ouvrier, invité)
- Type de chantier
- Statut de sécurité
- Pays, langue

## Règles d'accès
- Admin : accès total, audit, export.
- Chef de projet : gestion chantiers, sécurité.
- Ouvrier : accès à ses chantiers, documents.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: chantier
  condition: {}
- subject: worker
  action: [read]
  resource: chantier
  condition: {assigned: self}
```

## Sécurité
- JWT, CORS, WAF, logs, RGPD.

## Internationalisation
- Règles traduites dynamiquement (fr, en, ar, de, etc.)

## Extensibilité
- Ajout de rôles, ressources, conditions via API/CLI.

## Documentation intégrée
- YAML, Markdown, exemples, tests automatisés.
