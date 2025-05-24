// index.js – Dihya Marketplace Plugins

// Point d’entrée pour l’import/export des plugins marketplace
// Exemples d’utilisation, conventions, scripts d’automatisation

/**
 * Dihya Marketplace Plugins Index
 * Exporte tous les plugins métiers, modules, helpers, multilingue, sécurisé, documenté, prêt à l'emploi.
 */

const plugin = require('./plugin');
const stripePlugin = require('./stripe_plugin');

module.exports = {
  plugin,
  stripePlugin,
  // ...autres plugins à ajouter ici...
};
