/**
 * Dihya Blockchain Contracts Index
 * Exporte les smart contracts principaux, helpers de déploiement, multichain, sécurisé, documenté.
 */

const Project = require('./Project.sol');
const Roles = require('./Roles.sol');
const PluginManager = require('./PluginManager.sol');
const Payment = require('./Payment.sol');
// ...ajouter d'autres contrats selon besoins...

module.exports = {
  Project,
  Roles,
  PluginManager,
  Payment,
  // ...autres contrats...
};
