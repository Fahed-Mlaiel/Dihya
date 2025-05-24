# 🗺️ Dihya – Cartographie des Métiers & Documentation Associée

---

## Table des matières

- [Introduction](#introduction)
- [Principe de la cartographie](#principe-de-la-cartographie)
- [Tableau de correspondance métiers ↔ docs](#tableau-de-correspondance-métiers--docs)
- [Exemples d’intégration](#exemples-dintégration)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document cartographie chaque métier du projet **Dihya** avec sa documentation, ses templates, ses tests, ses assets, et ses modules associés.
Il garantit la traçabilité, la cohérence, la souveraineté numérique, la conformité RGPD, l’accessibilité, et la compatibilité multi-stack (React, Flask, Node, Django, Flutter…).

---

## Principe de la cartographie

- **Chaque métier** est lié à :
  - Sa fiche métier (template, doc, README)
  - Ses modules/plugins (frontend, backend, mobile…)
  - Ses tests (unitaires, intégration, e2e, manuels)
  - Ses assets (UI, API, scripts, configs)
  - Ses contrôles de conformité (sécurité, RGPD, accessibilité, souveraineté)
- **Multilingue** : chaque ressource est disponible en fr, en, ar, tzm.
- **Traçabilité** : chaque lien est vérifié, versionné, et auditable.

---

## Tableau de correspondance métiers ↔ docs

| Métier                  | Fiche métier                | Modules/Plugins         | Tests associés              | Assets/Configs             | Contrôles/Docs liés                  |
|-------------------------|----------------------------|------------------------|-----------------------------|----------------------------|--------------------------------------|
| DevOps                  | [devops.md](docs/metiers/devops.md) | backend/devops, scripts/ci | tests/devops, MANUAL_TESTS.md | scripts/devops, .github/workflows | [SEC-002](inventaire_controle_corrige.csv), [SEC-005](inventaire_controle_corrige.csv) |
| Développeur Frontend    | [frontend.md](docs/metiers/frontend.md) | frontend/, plugins/ui      | tests/frontend, MANUAL_TESTS.md | assets/ui, configs/i18n    | [ACC-001](inventaire_controle_corrige.csv)           |
| Développeur Backend     | [backend.md](docs/metiers/backend.md) | backend/, plugins/api      | tests/backend, MANUAL_TESTS.md  | assets/api, configs/db     | [SEC-001](inventaire_controle_corrige.csv)           |
| Data Privacy Officer    | [dpo.md](docs/metiers/dpo.md) | backend/dpo, scripts/rgpd   | tests/rgpd, MANUAL_TESTS.md     | docs/rgpd, configs/rgpd    | [RGPD-001](inventaire_controle_corrige.csv), [RGPD-002](inventaire_controle_corrige.csv) |
| QA/Accessibility Lead   | [qa.md](docs/metiers/qa.md) | frontend/qa, scripts/a11y    | tests/accessibility, MANUAL_TESTS.md | assets/a11y, configs/a11y  | [ACC-001](inventaire_controle_corrige.csv)           |
| Product Owner           | [po.md](docs/metiers/po.md) | docs/po, scripts/po          | tests/po, MANUAL_TESTS.md       | docs/roadmap, configs/po   | [DOC-001](inventaire_controle_corrige.csv)           |
| ...                     | ...                        | ...                    | ...                         | ...                        | ...                                  |

> **Ajoutez chaque nouveau métier et ses liens dans ce tableau pour garantir la couverture documentaire et la traçabilité.**

---

## Exemples d’intégration

### Exemple 1 : Développeur Backend

- **Fiche métier** : [backend.md](docs/metiers/backend.md)
- **Modules** : backend/, plugins/api
- **Tests** : tests/backend, MANUAL_TESTS.md
- **Assets** : assets/api, configs/db
- **Contrôles** : [SEC-001](inventaire_controle_corrige.csv)

### Exemple 2 : Data Privacy Officer

- **Fiche métier** : [dpo.md](docs/metiers/dpo.md)
- **Modules** : backend/dpo, scripts/rgpd
- **Tests** : tests/rgpd, MANUAL_TESTS.md
- **Assets** : docs/rgpd, configs/rgpd
- **Contrôles** : [RGPD-001](inventaire_controle_corrige.csv), [RGPD-002](inventaire_controle_corrige.csv)

---

## Multilingue

- **Français** : Ce mapping est disponible en français.
- **English** : This mapping is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-docs
- **Email** : docs@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce mapping est validé pour la production. Toute modification doit être soumise via PR et validée par le Doc Lead et le RSSI.**

# Mapping documentation métiers Dihya

- Liste des documents métiers, templates, guides, policies
- Mapping entre métiers, rôles, permissions, modules
- Liens vers les fichiers associés

Voir [METIERS_OVERVIEW.md](METIERS_OVERVIEW.md), [README_METIERS.md](README_METIERS.md)
