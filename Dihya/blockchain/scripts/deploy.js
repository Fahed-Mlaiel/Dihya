/**
 * Script de déploiement des smart contracts Dihya Coding.
 * Utilise ethers.js pour déployer sur Ethereum/EVM-compatible.
 * Respecte sécurité, modularité, bonnes pratiques.
 */

const { ethers } = require("ethers");
const fs = require("fs");
require("dotenv").config();

async function main() {
  // Charger la configuration réseau depuis .env
  const provider = new ethers.JsonRpcProvider(process.env.RPC_URL);
  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

  // Charger le bytecode et ABI du contrat (exemple : ProjectManager)
  const abi = JSON.parse(fs.readFileSync("./contracts/ProjectManager.abi.json", "utf8"));
  const bytecode = fs.readFileSync("./contracts/ProjectManager.bin", "utf8");

  // Déployer le contrat
  const factory = new ethers.ContractFactory(abi, bytecode, wallet);
  console.log("Déploiement du contrat ProjectManager...");
  const contract = await factory.deploy();
  await contract.waitForDeployment();

  console.log("Contrat déployé à l'adresse :", contract.target);

  // (Optionnel) Vérifier le contrat, enregistrer l'adresse, etc.
  fs.writeFileSync("./deployed_address.txt", contract.target);

  // Sécurité : ne jamais exposer la clé privée dans les logs ou le code source
}

main().catch((error) => {
  console.error("Erreur de déploiement :", error);
  process.exit(1);
});