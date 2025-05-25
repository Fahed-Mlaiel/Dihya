# Politique métier Voice

## Objectif
Définir les droits, responsabilités et bonnes pratiques pour l'utilisation des fonctionnalités vocales dans Dihya.

## Rôles
- **Admin** : gestion complète, accès à la configuration, audit, logs détaillés.
- **User** : usage standard, accès aux fonctions vocales, logs anonymisés.
- **Invité** : accès limité, lecture seule, aucune configuration.

## Sécurité
- Authentification JWT obligatoire.
- Validation stricte des entrées (anti-injection, anti-abus).
- CORS restrictif, WAF, anti-DDOS.

## Internationalisation
- Support dynamique des langues : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Auditabilité
- Tous les accès et actions sont logués, exportables, anonymisables.
- Conformité RGPD.

## Exemples d’usage
- Création de projet vocal multilingue.
- Génération de scripts vocaux IA.
- Intégration avec fallback LLaMA/Mixtral/Mistral.
