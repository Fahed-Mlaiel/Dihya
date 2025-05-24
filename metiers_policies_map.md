# 🛡️ Dihya – Cartographie Métiers ↔ Politiques & Procédures

---

## Table des matières

- [Introduction](#introduction)
- [Principe de la cartographie](#principe-de-la-cartographie)
- [Tableau de correspondance métiers ↔ policies](#tableau-de-correspondance-métiers--policies)
- [Exemples d’intégration](#exemples-dintégration)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document cartographie chaque métier du projet **Dihya** avec les politiques, procédures, guides et contrôles qui lui sont associés.
Il garantit la conformité, la traçabilité, la souveraineté numérique, la sécurité, l’accessibilité, et la compatibilité multi-stack (React, Flask, Node, Django, Flutter…).

---

## Principe de la cartographie

- **Chaque métier** est lié à :
  - Ses politiques (sécurité, RGPD, accessibilité, souveraineté, open source…)
  - Ses procédures opérationnelles (incident, conformité, logging, tests…)
  - Ses guides et templates (README, guides, modèles de déclaration…)
  - Ses contrôles de conformité (voir inventaire_controle_corrige.csv)
- **Multilingue** : chaque ressource est disponible en fr, en, ar, tzm.
- **Traçabilité** : chaque lien est vérifié, versionné, et auditable.

---

## Tableau de correspondance métiers ↔ policies

| Métier                  | Politiques/Procédures associées                   | Guides/Templates associés                | Contrôles liés (ID)         |
|-------------------------|---------------------------------------------------|------------------------------------------|-----------------------------|
| DevOps                  | [INCIDENT_RESPONSE.md](INCIDENT_RESPONSE.md), [LOGGING_GUIDE.md](LOGGING_GUIDE.md), [LEGAL_COMPLIANCE_GUIDE.md](LEGAL_COMPLIANCE_GUIDE.md) | [MANUAL_TESTS.md](MANUAL_TESTS.md), [Makefile](Makefile) | SEC-002, SEC-005, CI-001    |
| Développeur Frontend    | [LEGAL_COMPLIANCE.md](LEGAL_COMPLIANCE.md), [LOGGING_GUIDE.md](LOGGING_GUIDE.md), [INCIDENTS_GUIDE.md](INCIDENTS_GUIDE.md) | [MANUAL_TESTS.md](MANUAL_TESTS.md)       | ACC-001, RGPD-002           |
| Développeur Backend     | [INCIDENT_RESPONSE.md](INCIDENT_RESPONSE.md), [LEGAL_COMPLIANCE_GUIDE.md](LEGAL_COMPLIANCE_GUIDE.md), [LOGGING_GUIDE.md](LOGGING_GUIDE.md) | [MANUAL_TESTS.md](MANUAL_TESTS.md)       | SEC-001, SEC-004, RGPD-001  |
| Data Privacy Officer    | [LEGAL_COMPLIANCE_GUIDE.md](LEGAL_COMPLIANCE_GUIDE.md), [INCIDENTS.md](INCIDENTS.md) | [MANUAL_TESTS.md](MANUAL_TESTS.md), [inventaire_controle_corrige.csv](inventaire_controle_corrige.csv) | RGPD-001, RGPD-002          |
| QA/Accessibility Lead   | [LEGAL_COMPLIANCE_GUIDE.md](LEGAL_COMPLIANCE_GUIDE.md), [LOGGING_GUIDE.md](LOGGING_GUIDE.md) | [MANUAL_TESTS.md](MANUAL_TESTS.md)       | ACC-001, DOC-001            |
| Product Owner           | [LEGAL_COMPLIANCE.md](LEGAL_COMPLIANCE.md), [INCIDENTS_GUIDE.md](INCIDENTS_GUIDE.md) | [MANUAL_TESTS.md](MANUAL_TESTS.md)       | DOC-001                     |
| ...                     | ...                                               | ...                                      | ...                         |

> **Ajoutez chaque nouveau métier et ses liens dans ce tableau pour garantir la couverture documentaire et la traçabilité.**

---

## Exemples d’intégration

### Exemple 1 : DevOps

- **Politiques/Procédures** : [INCIDENT_RESPONSE.md](INCIDENT_RESPONSE.md), [LOGGING_GUIDE.md](LOGGING_GUIDE.md)
- **Guides/Templates** : [MANUAL_TESTS.md](MANUAL_TESTS.md), [Makefile](Makefile)
- **Contrôles** : SEC-002, SEC-005, CI-001

### Exemple 2 : Data Privacy Officer

- **Politiques/Procédures** : [LEGAL_COMPLIANCE_GUIDE.md](LEGAL_COMPLIANCE_GUIDE.md), [INCIDENTS.md](INCIDENTS.md)
- **Guides/Templates** : [MANUAL_TESTS.md](MANUAL_TESTS.md), [inventaire_controle_corrige.csv](inventaire_controle_corrige.csv)
- **Contrôles** : RGPD-001, RGPD-002

---

## Multilingue

- **Français** : Ce mapping est disponible en français.
- **English** : This mapping is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-policies
- **Email** : policies@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce mapping est validé pour la production. Toute modification doit être soumise via PR et validée par le Doc Lead et le RSSI.**

---

# Mapping policies métiers Dihya

- Liste des policies métiers, rôles, permissions
- Mapping entre policies, modules, métiers
- Liens vers les fichiers associés

Voir [METIERS_OVERVIEW.md](METIERS_OVERVIEW.md), [README_METIERS.md](README_METIERS.md)
