# Politique ABAC Banque & Finance

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications bancaires et financières (comptes, transactions, scoring, etc.).

## Attributs principaux
- Rôle utilisateur (admin, conseiller, client, invité)
- Type de compte
- Statut de la transaction
- Pays, langue
- Sensibilité des données

## Règles d'accès
- Admin : accès total, audit, export.
- Conseiller : accès clients, gestion comptes.
- Client : accès à ses comptes, transactions.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: account
  condition: {}
- subject: client
  action: [read, export]
  resource: account
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
