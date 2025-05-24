/**
 * Dihya Blockchain – Main Script
 * Gestion, audit, test, extension des smart contracts (Node.js)
 * Multilingue, sécurisé, souverain, documenté, prêt à l'emploi.
 */

const { execSync } = require('child_process');
const fs = require('fs');

function auditContract(contractPath) {
  // Audit statique (exemple avec slither ou mythril)
  try {
    console.log('Audit du contrat', contractPath);
    execSync(`slither ${contractPath}`);
    console.log('Audit terminé.');
  } catch (e) {
    console.error('Erreur audit:', e.message);
  }
}

function testContracts() {
  // Lancer les tests unitaires (ex: truffle test)
  try {
    execSync('truffle test', { stdio: 'inherit' });
  } catch (e) {
    console.error('Erreur tests:', e.message);
  }
}

function main() {
  // Exemple d'utilisation
  auditContract('./contracts/ProjectManager.sol');
  testContracts();
}

if (require.main === module) {
  main();
}
