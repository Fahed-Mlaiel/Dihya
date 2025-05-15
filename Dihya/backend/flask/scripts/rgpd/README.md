# rgpd/ — Scripts de conformité RGPD (Dihya Coding)

Ce dossier regroupe les scripts dédiés à la conformité RGPD (Règlement Général sur la Protection des Données) pour le backend Flask Dihya Coding.

## Objectif

- Automatiser les opérations liées à la protection des données personnelles : purge, anonymisation, export, audit, etc.
- Garantir la conformité légale et la traçabilité des traitements de données sensibles.
- Faciliter la gestion des droits des utilisateurs (accès, rectification, suppression, portabilité).

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Logger toutes les opérations RGPD pour audit et conformité.
- Ne jamais inclure de secrets ou de données sensibles en clair dans les scripts ou les logs.
- Prévoir des tests ou des dry-run pour les scripts à effet destructeur.
- Respecter les délais légaux et les politiques internes de conservation des données.

## Exemple de structure

- `purge_user_data.py` : suppression définitive des données d’un utilisateur.
- `anonymize_db.py` : anonymisation des données personnelles en base.
- `export_user_data.py` : export des données personnelles à la demande d’un utilisateur.
- `audit_rgpd.py` : audit des traitements et accès aux données personnelles.

## Exemple d’utilisation

```bash
python purge_user_data.py --user-id 123
python export_user_data.py --user-id 456 --output user_456.zip