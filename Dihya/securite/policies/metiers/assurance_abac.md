# Politique ABAC pour le secteur Assurance

## Objectif
Définir les règles d'accès basées sur les attributs (ABAC) pour les applications d'assurance, en conformité avec la RGPD, la sécurité maximale, et la gestion multitenant.

## Attributs principaux
- Rôle utilisateur (admin, user, invité)
- Statut de la police d'assurance
- Type de contrat (auto, habitation, santé, etc.)
- Pays et langue de l'utilisateur
- Niveau de sensibilité des données
- Contexte d'accès (API, mobile, web)

## Règles d'accès
- Les admins peuvent accéder à tous les contrats et données, sauf données anonymisées RGPD.
- Les utilisateurs peuvent accéder uniquement à leurs propres contrats et documents.
- Les invités n'ont accès qu'aux offres publiques et simulateurs.
- Les accès sont journalisés, audités, et exportables.
- Toute action sensible requiert une validation JWT et un audit trail.

## Exemples YAML (exploitable via API/CLI)
```yaml
- subject: admin
  action: [read, write, delete, export]
  resource: contract
  condition: {}
- subject: user
  action: [read, export]
  resource: contract
  condition: {owner: self}
- subject: guest
  action: [read]
  resource: offer
  condition: {public: true}
```

## Internationalisation
- Toutes les règles sont traduites dynamiquement (fr, en, ar, de, etc.)

## Sécurité
- CORS strict, JWT, WAF, anti-DDOS, logs structurés, anonymisation RGPD.

## Extensibilité
- Ajout de nouveaux rôles, ressources, ou conditions via API/CLI.

## Documentation intégrée
Chaque règle est documentée en YAML et Markdown, avec exemples et tests automatisés.
