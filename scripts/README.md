# Dihya Scripts

## Présentation (français)
Ce dossier regroupe tous les scripts d’automatisation, de déploiement, de migration, de backup, de test, et de maintenance pour la plateforme Dihya. Chaque script est documenté, robuste, compatible Linux/GitHub Codespaces, et sécurisé.

## Overview (English)
This folder contains all automation, deployment, migration, backup, test, and maintenance scripts for the Dihya platform. Each script is documented, robust, Linux/GitHub Codespaces compatible, and secure.

## دليل السكريبتات (العربية)
يحتوي هذا المجلد على جميع سكريبتات الأتمتة والنشر والصيانة لمنصة ديهيا، موثقة ومتوافقة مع لينكس وGitHub Codespaces.

## ⵜⴰ⎠ⵣⵉⵖⵜ (amazigh)
Aganfu agi yegber akk iskripten n Dihya, s uselkim, tazwart, tazwart n tutlayin.

### Structure
- main.py, main.js : Entrées principales (Python, Node.js)
- Scripts shell : backup.sh, deploy.sh, test.sh, etc.
- Guides : EMERGENCY_GUIDE.md, etc.

### Sécurité & Portabilité
- Pas de secrets en dur, logs sécurisés, gestion des erreurs avancée.
- Compatible Linux, Codespaces, CI/CD.

### Contribution
Merci de documenter chaque script et de tester la portabilité avant tout commit.

---

## 🔒 Sécurité avancée
- Aucun secret en dur, variables d’environnement obligatoires.
- Logs sécurisés, auditables, rotation automatique.
- Scripts testés contre les injections et élévations de privilèges.

## ♿ Accessibilité & Multilinguisme
- Tous les scripts et guides sont documentés en français, anglais, arabe, amazigh.
- Sorties console compatibles lecteurs d’écran (UTF-8, pas de couleurs bloquantes).

## 🧩 Modularité & Extension
- Chaque script peut être appelé en CLI ou importé comme module (Python/Node).
- Ajout de hooks/plugins possible (voir `index.js`).

## 🧪 Tests & CI/CD
- Tests unitaires et e2e pour chaque script (voir `test.sh`).
- Intégration continue : lint, test, audit sécurité à chaque push.

## 🚀 Exemples d’utilisation
- `./backup.sh` : sauvegarde complète, logs détaillés.
- `python3 main.py --help` : documentation CLI dynamique.
- `node main.js --env production` : exécution Node.js multi-environnement.

## 📄 Documentation & Contribution
- Toute contribution doit inclure : documentation, test, exemple d’appel, vérification multi-OS.
- Voir `/CONTRIBUTING.md` et `/ACCESSIBILITY_GUIDE_ADVANCED.md`.

---

# 🧪 Exemple de test automatisé
```bash
./test.sh --script backup.sh
```

## 🔄 Backup automatisé en temps réel
- `make backup-realtime` ou `./backup_realtime.sh` : surveille toutes les modifications du projet et déclenche un backup sécurisé à chaque changement (inotify, logs, hooks, multilingue, CI/CD-ready).
- Conforme RGPD, audit, accessibilité, production/démo.
- Arrêt : Ctrl+C
