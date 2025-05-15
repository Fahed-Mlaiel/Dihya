# Smart Contracts – Dihya Coding

Ce dossier contient les smart contracts de la plateforme Dihya Coding.  
Il respecte le cahier des charges : sécurité, modularité, bonnes pratiques, extensibilité, multichain.

---

## Fonctionnalités principales

- Smart contracts pour la gestion de projets, rôles, plugins, paiements, etc.
- Compatibilité Ethereum (Solidity), EVM, et autres blockchains (extensible)
- Sécurité renforcée (tests, audit, bonnes pratiques OpenZeppelin)
- Documentation et commentaires pour chaque contrat
- Scripts de déploiement fournis dans `../scripts/`
- Prise en charge des mises à jour (upgradeability, proxy pattern si besoin)
- Extensible pour plugins, tokens, NFT, etc.

---

## Structure recommandée

```
contracts/
├── README.md
├── Project.sol
├── Roles.sol
├── PluginManager.sol
├── Payment.sol
└── (autres contrats selon besoins)
```

---

## Bonnes pratiques & sécurité

- Utilisation des librairies OpenZeppelin pour la sécurité
- Tests unitaires obligatoires (voir dossier `../tests/` si présent)
- Commentaires et docstring dans chaque contrat
- Vérification des permissions (modificateurs `onlyOwner`, `onlyAdmin`, etc.)
- Gestion des événements (`event`) pour la transparence
- Limitation du gas et optimisation des fonctions critiques

---

## Déploiement

- Utiliser les scripts fournis dans `../scripts/` (ex: `deploy.js`)
- Adapter les paramètres réseau dans les scripts selon la blockchain cible
- Pour Ethereum : compatible avec Hardhat, Truffle, Remix

---

## Exemple de contrat minimal

```solidity
// SPDX-License-Identifier: AGPL-3.0
pragma solidity ^0.8.20;

/// @title ProjectManager - Gestion des projets Dihya Coding
contract ProjectManager {
    address public owner;

    event ProjectCreated(address indexed creator, string name);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function createProject(string memory name) public {
        emit ProjectCreated(msg.sender, name);
    }
}
```

---

## Licence

Projet open-source sous licence AGPL.  
Voir le fichier `LICENSE` à la racine du projet.

---