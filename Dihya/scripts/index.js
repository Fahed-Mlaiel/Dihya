// index.js – Dihya Scripts Entrypoint (Node)
/**
 * Exporte tous les scripts, hooks, helpers, multilingue, sécurisé, documenté, prêt à l'emploi.
 */

const auditSecrets = require('./audit_secrets.sh');
const checkLicense = require('./check_license.sh');
const importExportTemplates = require('./import_export_templates.js');
const main = require('./main.js');

module.exports = {
  auditSecrets,
  checkLicense,
  importExportTemplates,
  main,
  // ...autres scripts à ajouter ici...
};
