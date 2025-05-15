# souverainete/ — Souveraineté numérique, export/import/anonymisation (Dihya Coding)

Ce dossier regroupe les scripts et outils pour garantir la souveraineté numérique des utilisateurs et du projet : export, import, anonymisation des données, conformité RGPD.

## Objectif

- Permettre l’export des données dans des formats ouverts (CSV, JSON) pour la portabilité et la transparence.
- Faciliter l’import de données pour migration, restauration ou synchronisation.
- Offrir des outils d’anonymisation pour la confidentialité et la conformité légale (RGPD).
- Logger chaque opération pour audit et traçabilité.

## Bonnes pratiques

- Toujours logger chaque opération (export, import, anonymisation) avec horodatage et périmètre.
- Ne jamais inclure de secrets ou de données confidentielles dans les exports sans contrôle d’accès.
- Valider la structure et la cohérence des fichiers avant import.
- Documenter précisément les champs et tables concernés dans chaque script.
- Tester l’intégrité de la base après chaque opération.
- Restreindre l’accès à ce dossier aux administrateurs ou responsables conformité.

## Contenu

- **export.py** : Export des tables principales en CSV/JSON.
- **import.py** : Import de données depuis CSV/JSON.
- **anonymize.py** : Anonymisation des données personnelles (ex : utilisateurs).
- **exports/** : Dossier cible pour les fichiers exportés.

## Exemple d’utilisation

```bash
python export.py
python import.py
python anonymize.py