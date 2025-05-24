# README – Dihya DevOps

Ce dossier contient les scripts, configurations et guides DevOps pour Dihya : CI/CD, monitoring, backup, sécurité, déploiement multi-cloud, etc.

- Architecture CI/CD, scripts d’automatisation, sécurité, multicloud
- Exemples d’utilisation, pipelines, tests, contribution

Voir [../../README.md](../../README.md), [../README.md](../README.md)

---

## Fonctionnalités principales

- Dockerisation complète (backend Flask, frontend React)
- Déploiement Kubernetes (manifests k8s prêts à l’emploi)
- Infrastructure as Code (Terraform, cloud-agnostique)
- CI/CD automatisé (GitHub Actions recommandé)
- Sécurité : non-root, variables d’environnement, probes, ressources limitées
- Extensible pour d’autres stacks (Node.js, blockchain, etc.)

---

## Structure des dossiers

```
devops/
├── README.md
├── docker/
│   ├── Dockerfile.backend
│   └── Dockerfile.frontend
├── k8s/
│   └── deployment.yaml
└── terraform/
    └── main.tf
```

---

## Docker

- **Backend Flask** : `docker/Dockerfile.backend`
- **Frontend React** : `docker/Dockerfile.frontend`
- Utilisation d’utilisateurs non-root, build multi-étapes, variables d’environnement

### Commandes utiles

```bash
docker build -f docker/Dockerfile.backend -t dihya/backend:latest .
docker build -f docker/Dockerfile.frontend -t dihya/frontend:latest .
docker run --env-file ../backend/flask/.env -p 5000:5000 dihya/backend:latest
docker run -p 8080:80 dihya/frontend:latest
```

---

## Kubernetes

- Déploiement multi-conteneurs (`k8s/deployment.yaml`)
- Probes (readiness/liveness), ressources limitées, labels, services
- Prêt pour Ingress ou LoadBalancer selon le cloud

### Commandes utiles

```bash
kubectl apply -f k8s/deployment.yaml
kubectl get pods,svc
```

---

## Terraform

- Déploiement automatisé Docker local (cloud-agnostique)
- Variables d’environnement sécurisées
- Outputs pour accès rapide aux services

### Commandes utiles

```bash
cd terraform
terraform init
terraform apply
```

---

## CI/CD (recommandé)

- Utiliser GitHub Actions pour build, test, lint, déploiement automatique
- Exemple de workflow : `.github/workflows/ci.yml` (à créer)

---

## Sécurité & bonnes pratiques

- Utilisateurs non-root dans les containers
- Variables d’environnement pour secrets
- Limitation des ressources CPU/mémoire
- Probes de santé pour haute disponibilité
- Images minimales et build multi-étapes

---

## Extensibilité

- Ajouter d’autres stacks (Node.js, blockchain, etc.) dans les Dockerfiles et manifests
- Ajouter des scripts de migration, backup, monitoring, etc.

---

## Licence

Projet open-source sous licence AGPL.
Voir le fichier `LICENSE` à la racine du projet.

---
