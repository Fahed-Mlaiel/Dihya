# README – Dihya Templates (assets/templates)

Ce dossier regroupe les templates métiers multilingues (JSON) prêts à l’emploi pour la génération automatique de documents, formulaires, IA, et intégration web/mobile/plugins.

## Structure et conventions
- Chaque template est un fichier JSON structuré : nom, langues supportées, champs, labels multilingues.
- Les templates couvrent les secteurs : éducation, santé, juridique, industrie, finance, RH…
- Tous les labels sont fournis en fr, en, ar, amazigh (tzr) pour la souveraineté et l’accessibilité.
- Les templates sont RGPD-ready, extensibles, versionnés, testés.

## Exemples de templates disponibles
- `template-education.json` : bulletin scolaire multilingue
- `template-health.json` : dossier patient multilingue
- `template-legal.json` : dossier juridique multilingue
- `template-industry.json` : fiche production industrielle
- `template-finance.json` : fiche transaction financière
- `template-hr.json` : fiche employé RH

## Ajouter un template métier
1. Créez un fichier `template-<secteur>.json` structuré comme les exemples.
2. Fournissez tous les labels en fr, en, ar, tzr.
3. Documentez chaque champ dans ce README si besoin.
4. Vérifiez la conformité RGPD, l’accessibilité, la cohérence multilingue.

## Utilisation
- Import direct dans les modules backend/frontend/plugins pour la génération automatique.
- Compatible Python, Node.js, scripts, tests, CI/CD.
- Voir `/assets/main.py` et `/assets/index.js` pour l’import dynamique et la documentation technique.
