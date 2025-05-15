# Dihya Coding — Projet Fullstack

Bienvenue sur le projet **Dihya Coding**.  
Ce dépôt contient l'ensemble des sources pour la plateforme Dihya : backend, frontend, IA, mobile, blockchain, devops, documentation et internationalisation.

---

## Structure du projet

- **ai/** : Modèles, notebooks et scripts d'IA/ML.
- **assets/** : Ressources graphiques (icônes, images).
- **backend/**
  - **flask/** : Backend principal en Flask (API REST, sécurité, gestion utilisateurs, etc.).
  - **node/** : Backend Node.js (si besoin de microservices JS).
- **blockchain/** : Smart contracts et scripts de déploiement.
- **devops/** : Docker, Kubernetes, Terraform, CI/CD.
- **docs/** : Documentation technique et utilisateur.
- **frontend/** : Application web (React, etc.).
- **i18n/** : Fichiers de traduction et internationalisation.
- **mobile/** : Apps Flutter et React Native.

---

## Fonctionnalités principales

- **API REST sécurisée** (Flask, JWT, CORS, validation, tests)
- **Gestion utilisateurs** (inscription, login, rôles, profil)
- **No-Code/Low-Code** (génération multistack)
- **Internationalisation** (i18n, multilingue)
- **SEO** (robots.txt, sitemap.xml)
- **Tests unitaires et d'intégration** (pytest)
- **DevOps** (Docker, K8s, CI/CD)
- **Mobile** (Flutter, React Native)
- **Blockchain** (contrats, scripts)

---

## Lancer le backend Flask

```bash
cd Dihya/backend/flask
export PYTHONPATH=$PYTHONPATH:$(pwd)/app
flask run