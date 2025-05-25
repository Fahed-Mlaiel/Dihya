# Politique ABAC Blockchain

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications blockchain (wallet, smart contract, NFT, etc.).

## Attributs principaux
- Rôle utilisateur (admin, développeur, utilisateur, invité)
- Type de wallet
- Statut de transaction
- Pays, langue

## Règles d'accès
- Admin : accès total, audit, export.
- Développeur : gestion smart contracts, audits.
- Utilisateur : accès à ses wallets, transactions.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: wallet
  condition: {}
- subject: developer
  action: [read, write]
  resource: contract
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
