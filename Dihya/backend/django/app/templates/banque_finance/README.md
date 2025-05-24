# 💳 Dihya – Templates Banque & Finance Ultra Avancés (Sécurité, Multilingue, Souveraineté, Extensible)

---

## Table des matières

- [Rôle du dossier `templates/banque_finance`](#rôle-du-dossier-templatesbanque_finance)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemple d’intégration d’un template](#exemple-dintégration-dun-template)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 💳 Rôle du dossier `templates/banque_finance`

Ce dossier centralise tous les templates, assets, scripts et plugins métiers pour la banque et la finance (contrats, relevés, transactions, audits, IA, plugins) utilisés par la plateforme Dihya.

- **Multi-stack** : compatible Django, Node, API REST, outils financiers, YAML, PDF, etc.
- **Souveraineté** : templates open source, traçables, versionnés, audités
- **Sécurité** : aucun code exécutable non contrôlé, audit automatique, conformité RGPD/NIS2
- **Extensible** : ajoutez vos propres modèles, contrats, scripts, plugins, assets IA

---

## 🧠 Fonctions principales

- **Gestion centralisée** des templates banque & finance (contrats, relevés, transactions, audits, scripts de génération)
- **Découverte automatique** des templates/plugins (voir `__init__.py`)
- **Interopérabilité** avec outils métiers, API, pipelines CI/CD, IA
- **Documentation et métadonnées** pour chaque template (origine, licence, usage, hash)
- **Scripts de validation** et d’intégrité pour chaque ajout/modification

---

## 📁 Structure recommandée

```
banque_finance/
├── __init__.py                       # Initialisation, auto-discovery, sécurité
├── policy.md                         # Politique d’utilisation, sécurité, conformité
├── README.md                         # Ce fichier (documentation multilingue)
├── validate_banque_finance_template.py    # Script de validation d’intégrité et de conformité
├── assets/                           # Templates banque & finance (json, yaml, pdf, md…)
│   ├── exemple_contrat_bancaire.json
│   ├── exemple_releve.yaml
│   └── README.assets.md
├── plugins/                          # Plugins/scripts de génération ou traitement métier
│   └── exemple_plugin_audit.py
└── tests/                            # Tests unitaires et d’intégration pour assets/scripts
    └── test_validate_banque_finance_template.py
```

---

## 🔒 Sécurité & conformité

- **Aucun code exécutable** dans les templates (pas de scripts embarqués, pas de macros)
- **Auditabilité** : chaque template est versionné, documenté, hashé (SHA256)
- **Chiffrement** des documents sensibles (au repos et en transit)
- **Anonymisation** des métadonnées (pas de données personnelles)
- **Vérification automatique** via `validate_banque_finance_template.py` (CI/CD, GitHub Actions)
- **Suppression sur demande** et export des métadonnées (conformité RGPD/NIS2)
- **Fallback IA open source** pour la vérification automatique des templates

---

## 🛠️ Exemple d’intégration d’un template

### Ajout d’un template

1. Placez le fichier dans `assets/` (ex : `contrat_bancaire_2025.json`)
2. Ajoutez une entrée dans `README.assets.md` :

```markdown
### contrat_bancaire_2025.json
- Origine : Création interne
- Licence : CC-BY-SA 4.0
- Auteur : A. Dihya
- Usage : Contrat bancaire 2025
- Date : 2025-05-21
- Version : 1.0
- SHA256 : `a1b2c3...`
- Description : Contrat structuré pour la gestion bancaire, compatible outils financiers et IA.
```

3. Lancez le script de validation :

```bash
python3 validate_banque_finance_template.py assets/contrat_bancaire_2025.json
```

---

## 📝 Bonnes pratiques

- **Limiter la taille** des documents (max 10 Mo)
- **Optimiser** pour l’usage numérique (accessibilité, champs structurés, interopérabilité)
- **Séparer** contrats, relevés, transactions, audits, scripts
- **Versionner** chaque modification (Git, changelog, hash)
- **Traduire** les métadonnées et descriptions (fr, en, ar, tzm)
- **Respecter la propriété intellectuelle** et les licences open source

---

## 🌍 Multilingue

- **Français** : Ce dossier est documenté en français.
- **English** : This folder is documented in English.
- **العربية** : هذا المجلد موثق باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Afaylu agi yettwarnan s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📚 Documentation associée

- [Politique d’utilisation & sécurité](./policy.md)
- [Script de validation](./validate_banque_finance_template.py)
- [Architecture backend](../../../../docs/architecture.md)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)

---

**Dihya Coding** – Banque & finance souveraines, extensibles, multilingues, prêtes pour la production, la démo et la contribution.

---
