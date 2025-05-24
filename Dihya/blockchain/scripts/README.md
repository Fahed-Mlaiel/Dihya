# Dihya Coding – Blockchain / Scripts

Scripts pour la génération, le déploiement et la gestion de smart contracts blockchain dans la plateforme Dihya Coding.

---

## 🚀 Objectif

Permettre la génération automatique, l’audit, le test et le déploiement de contrats intelligents (Solidity, EVM) à partir d’un cahier des charges métier, en toute souveraineté et conformité RGPD.

---

## 📦 Contenu du dossier

- `deploy.js` : Script Node.js pour déployer un smart contract sur une blockchain compatible EVM (Ethereum, Polygon, etc.)
- (À compléter) Scripts pour :
  - Génération automatique de contrats à partir de templates métiers
  - Audit de sécurité automatisé (lint, static analysis)
  - Tests unitaires et d’intégration (Truffle, Hardhat, Foundry)
  - Export/import de contrats (JSON, ABI, source)
  - Backup décentralisé (IPFS, DWeb)

---

## 🔒 Sécurité & RGPD

- **Auditabilité** : chaque déploiement est loggé et horodaté
- **Sécurité** : analyse statique, vérification des permissions, gestion des clés hors dépôt
- **Conformité RGPD** : possibilité d’anonymiser ou de supprimer les données liées à un smart contract sur demande

---

## 🛠️ Utilisation rapide

```bash
cd Dihya/blockchain/scripts
node deploy.jsAdapter le script selon votre provider (Infura, Alchemy, etc.) et renseigner les variables d’environnement dans .env.

🧩 Extensibilité
Ajoutez vos propres scripts de génération ou d’audit dans ce dossier
Compatible avec les templates métiers générés par la plateforme (voir /backend/flask/app/templates/blockchain/)
Prêt pour intégration avec la marketplace de plugins Dihya
📚 Documentation
Guide blockchain général
Templates métiers blockchain
Sécurité & RGPD
🏷️ Bonnes pratiques
Ne jamais committer de clés privées dans le dépôt
Vérifiez chaque contrat généré avant déploiement en production
Utilisez les outils d’audit fournis pour garantir la sécurité et la conformité
© Dihya Coding – 2025 ```