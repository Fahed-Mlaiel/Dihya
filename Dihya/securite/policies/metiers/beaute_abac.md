# Politique ABAC Beauté

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications beauté (salons, e-commerce, réservation, etc.).

## Attributs principaux
- Rôle utilisateur (admin, pro, client, invité)
- Type de service
- Statut de réservation
- Pays, langue

## Règles d'accès
- Admin : accès total, audit, export.
- Pro : gestion de ses salons, réservations.
- Client : accès à ses réservations, historique.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: salon
  condition: {}
- subject: pro
  action: [read, write]
  resource: salon
  condition: {owner: self}
```

## Sécurité
- JWT, CORS, WAF, logs, RGPD.

## Internationalisation
- Règles traduites dynamiquement (fr, en, ar, de, etc.)

## Extensibilité
- Ajout de rôles, ressources, conditions via API/CLI.

## Documentation intégrée
- YAML, Markdown, exemples, tests automatisés.
