# Politique ABAC E-commerce

## Objectif
Définir les règles d'accès basées sur les attributs pour les applications e-commerce (boutique, panier, paiement, etc.).

## Attributs principaux
- Rôle utilisateur (admin, vendeur, client, invité)
- Type de produit
- Statut de commande
- Pays, langue

## Règles d'accès
- Admin : accès total, audit, export.
- Vendeur : gestion produits, commandes.
- Client : accès à ses commandes, historique.
- Invité : accès aux offres publiques.

## Exemples YAML
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: product
  condition: {}
- subject: seller
  action: [read, write]
  resource: product
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
