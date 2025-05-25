# Politique ABAC Construction

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications construction (projets, chantiers, sécurité, etc.).

## Attributs principaux
- Rôle utilisateur (admin, chef de projet, ouvrier, invité)
- Type de projet
- Statut de sécurité
- Pays, langue

## Règles d'accès
- Admin : accès total, audit, export.
- Chef de projet : gestion projets, sécurité.
- Ouvrier : accès à ses projets, documents.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: projet
  condition: {}
- subject: worker
  action: [read]
  resource: projet
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
