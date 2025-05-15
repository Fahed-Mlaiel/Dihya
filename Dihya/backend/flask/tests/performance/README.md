# tests/performance/ — Tests de charge & performance Backend Dihya Coding

Ce dossier contient les scripts, scénarios et résultats de tests de charge et de performance pour le backend Flask de Dihya Coding.

## Objectif

- Évaluer la robustesse, la scalabilité et la réactivité de l’API et des services critiques.
- Identifier les goulets d’étranglement et anticiper les besoins d’optimisation.
- Garantir une expérience utilisateur fluide, même sous forte charge.

## Bonnes pratiques

- Utiliser des outils open source (Locust, JMeter, k6, etc.) pour simuler la charge.
- Documenter chaque scénario de test (endpoints, volume, durée, utilisateurs virtuels).
- Ne jamais utiliser de données sensibles ou de secrets dans les scénarios.
- Logger les résultats et anomalies détectées pour audit et amélioration continue.
- Automatiser les tests de performance dans la CI/CD si possible.
- Prévoir des seuils d’alerte (latence, taux d’erreur, saturation).

## Exemple de structure

- `locustfile.py` : scénario Locust pour simuler des utilisateurs concurrents.
- `report/` : dossiers pour les rapports de tests (HTML, CSV, etc.).
- `README.md` : documentation et consignes d’utilisation.

## Exemple d’utilisation (Locust)

```bash
locust -f locustfile.py --host=http://localhost:5000