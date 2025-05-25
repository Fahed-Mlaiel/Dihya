# Services à la personne / Personal Services / خدمات شخصية / Dienstleistungen / 个人服务 / パーソナルサービス / 개인 서비스 / Persoonlijke diensten / שירותים אישיים / خدمات شخصی / व्यक्तिगत सेवाएं / Servicios personales / ⴰⵙⵉⵏⴳⴰⵔ ⴰⵎⴰⵣⵉⵖ

## Présentation
Les services à la personne exploitent l’IA, la VR/AR pour la gestion des interventions, la personnalisation, et l’accompagnement multilingue.

### Exemples d’usages IA/VR/AR
- Planification intelligente (IA)
- Assistance vocale multilingue (IA)
- Formation immersive (VR)

## Exemples de routes API
- `GET /api/services_personne/interventions` : Liste des interventions
- `POST /api/services_personne/planifier` : Planification IA
- `GET /api/services_personne/formation-vr` : Formation VR

### Extrait GraphQL
```graphql
query {
  interventions {
    id
    type
    date
  }
}
```

## Exemple de plugin
- Plugin d’assistance vocale

## Sécurité & RGPD
- JWT, CORS, logs, anonymisation, export RGPD, auditabilité.

## Tests
- Unitaire : planification
- Intégration : workflow intervention
- E2E : parcours bénéficiaire multilingue

## Multilingue
- 13 langues supportées.

## Personnalisation
- Plugins, modules, API extensibles.

---
*Template services à la personne avancé, sécurisé, RGPD, multilingue.*
