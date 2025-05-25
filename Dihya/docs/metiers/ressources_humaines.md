# Ressources Humaines / Human Resources / الموارد البشرية / Personalwesen / 人力资源 / 人事 / 인사 / Human Resources / משאבי אנוש / منابع انسانی / मानव संसाधन / Recursos humanos / ⴰⵙⵉⵏⴳⴰⵔ ⴰⵎⴰⵣⵉⵖ

## Présentation
Les RH modernes s’appuient sur l’IA, la VR/AR pour le recrutement, la gestion des talents, la formation et l’engagement collaborateur.

### Exemples d’usages IA/VR/AR
- Recrutement automatisé (IA)
- Formation immersive (VR)
- Analyse de satisfaction (IA)

## Exemples de routes API
- `GET /api/rh/candidats` : Liste des candidats
- `POST /api/rh/recruter` : Recrutement IA
- `GET /api/rh/formation-vr` : Formation VR

### Extrait GraphQL
```graphql
query {
  candidats {
    id
    nom
    competences
  }
}
```

## Exemple de plugin
- Plugin d’analyse de satisfaction

## Sécurité & RGPD
- JWT, CORS, logs, anonymisation, export RGPD, auditabilité.

## Tests
- Unitaire : recrutement
- Intégration : workflow formation
- E2E : parcours collaborateur multilingue

## Multilingue
- 13 langues supportées.

## Personnalisation
- Plugins, modules, API extensibles.

---
*Template RH avancé, sécurisé, RGPD, multilingue.*
