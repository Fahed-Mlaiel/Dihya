# Politique ABAC Culture

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications culturelles (musées, événements, billetterie, etc.).

## Attributs principaux
- Rôle utilisateur (admin, organisateur, visiteur, invité)
- Type d'événement
- Statut de réservation
- Pays, langue

## Règles d'accès
- Admin : accès total, audit, export.
- Organisateur : gestion événements, réservations.
- Visiteur : accès à ses réservations, billets.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: event
  condition: {}
- subject: organizer
  action: [read, write]
  resource: event
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
