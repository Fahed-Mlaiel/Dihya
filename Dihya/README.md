# Dihya Coding — Projet Fullstack
**No-Code souverain, multilingue, extensible, production-ready**

---

## 🌍 Présentation | Overview | العرض | ⴰⵙⵉⵏⴰⵡ

**Dihya Coding** est une plateforme No-Code / Low-Code souveraine, open source, capable de générer, déployer et documenter tout projet numérique (web, mobile, backend, IA, blockchain, DevOps) à partir d’un cahier des charges écrit ou dicté, en toute souveraineté.

- **Génération multistack** : React, Flask, Node.js, Django, Flutter, Solidity, DevOps, IA, plugins, templates métiers.
- **Design UI/UX** : responsive, accessible, multilingue (fr, en, ar, amazigh), thèmes amazigh ou personnalisés.
- **Déploiement automatique** : preview/demo, CI/CD, sécurité, SEO, mailing, authentification, marketplace de plugins/templates.

---

## 🏗️ Structure du projet | Project Structure

```text
ai/         # IA/ML : modèles, scripts, notebooks, API, fallback open source
assets/     # Icônes, logos, images, polices, vidéos, templates, branding
backend/
  flask/    # Backend principal Flask (API REST, sécurité, gestion utilisateurs, etc.)
  node/     # Backend Node.js (microservices JS, plugins, fallback)
blockchain/ # Smart contracts Solidity, scripts déploiement, audit
devops/     # Docker, Kubernetes, Terraform, CI/CD, scripts, monitoring
docs/       # Documentation technique, guides, API, contribution, RGPD
frontend/   # Application web (React, UI/UX, marketplace, preview)
i18n/       # Fichiers de traduction, gestion multilingue, import/export
mobile/     # Apps Flutter et React Native (génération, preview, plugins)
```

---

## 🚀 Fonctionnalités principales | Main Features

- **API REST sécurisée** (Flask, JWT, CORS, validation, tests, auditabilité)
- **Gestion utilisateurs** (inscription, login, rôles, profil, OAuth, RGPD)
- **Génération No-Code/Low-Code** (multi-stack, templates métiers, plugins)
- **Internationalisation** (i18n, multilingue, dialectes, import/export)
- **SEO avancé** (robots.txt, sitemap.xml, balises, Lighthouse)
- **Tests unitaires, intégration, e2e** (pytest, jest, coverage 100%)
- **DevOps** (Docker, K8s, CI/CD GitHub Actions, monitoring, alerting)
- **Mobile** (Flutter, React Native, preview, déploiement)
- **Blockchain** (contrats Solidity, scripts, audit, démo)
- **Souveraineté numérique** (fallback IA open source, logs, audit, RGPD, licence AGPL)
- **Extensibilité** (plugins, templates métiers, marketplace, contribution ouverte)

---

## 🛡️ Sécurité & conformité | Security & Compliance

- **RGPD** : données minimisées, anonymisation, logs, auditabilité, opt-in/opt-out.
- **Sécurité** : CORS, anti-DDoS, rate limiting, headers stricts, validation forte, audit de code.
- **Fallback IA** : Mixtral, LLaMA, Mistral intégrés en local.
- **Transparence** : open source AGPL, logs d’origine du code généré, auditabilité complète.

---

## 🗺️ Démarrage rapide | Quickstart

### Backend Flask

```bash
cd Dihya/backend/flask
export PYTHONPATH=$PYTHONPATH:$(pwd)/app
flask run
```

### Frontend React

```bash
cd Dihya/frontend
npm install
npm start
```

### Mobile (Flutter)

```bash
cd Dihya/mobile/flutter
flutter pub get
flutter run
```

---

## 📚 Documentation

- [Guide utilisateur](../docs/user_guide.md)
- [Guide développeur](../docs/dev_guide.md)
- [Architecture](../docs/architecture.md)
- [Contribution](../docs/contribution/README.md)
- [API & OpenAPI](../backend/docs/openapi.yaml)

---

## 📜 Licence | License

Projet sous licence **AGPL v3** pour garantir la souveraineté, la transparence et la contribution ouverte.
Voir [LICENSE](./LICENSE) pour les détails multilingues.

---

# Dihya – README du module principal

Ce module centralise la logique, les interfaces et les scripts partagés du projet Dihya.

- Architecture modulaire, microservices, sécurité, multilingue
- Intégration backend, frontend, mobile, plugins, IA, blockchain
- Scripts d’automatisation, tests, CI/CD, monitoring
- Documentation, guides, templates, assets, branding

Voir [../README.md](../README.md), [../ARCHITECTURE.md](../ARCHITECTURE.md)

---

**Dihya Coding** – Souveraineté, innovation, ouverture, accessibilité pour tous.
