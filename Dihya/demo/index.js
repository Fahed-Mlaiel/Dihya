/**
 * Dihya Demo – Entrée principale
 * Génération, preview, audit, multilingue, sécurisé, documenté, prêt à l'emploi.
 */

const { generateProject, previewProject, exportProject, auditGeneration } = require('../generation');
const { logEvent } = require('../utils/audit');

function runDemo(input, lang = 'fr', type = 'web') {
  // Génère un projet à partir d'un cahier des charges
  const project = generateProject(input, lang, type);
  previewProject(project);
  auditGeneration(project);
  logEvent('demo_run', { input, lang, type });
  return project;
}

module.exports = {
  runDemo,
};
