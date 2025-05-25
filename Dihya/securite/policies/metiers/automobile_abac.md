# Politique ABAC pour le secteur Automobile

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications automobiles (gestion flotte, location, maintenance, etc.).

## Attributs principaux
- Rôle utilisateur (admin, gestionnaire, conducteur, invité)
- Type de véhicule
- Statut de maintenance
- Localisation
- Niveau de sensibilité des données

## Règles d'accès
- Admin : accès total, audit, export.
- Gestionnaire : accès flotte, maintenance, logs.
- Conducteur : accès à ses véhicules, historiques.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: vehicle
  condition: {}
- subject: driver
  action: [read]
  resource: vehicle
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
