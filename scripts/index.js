// Fichier d'entrée pour scripts
/**
 * index.js – Orchestrateur avancé des scripts Dihya
 * Multilingue, sécurisé, modulaire, extensible, CI/CD ready
 */
const { execSync } = require('child_process');

function runScript(script, lang = 'fr') {
  try {
    console.log(`[${lang}] Exécution de ${script}...`);
    execSync(`bash ${script}`, { stdio: 'inherit', env: { ...process.env, LANG: lang } });
  } catch (e) {
    console.error(`[${lang}] Erreur lors de l’exécution de ${script}:`, e.message);
    process.exit(1);
  }
}

// Exemples d’utilisation
// runScript('backup.sh', 'fr');
// runScript('clean.sh', 'en');
// runScript('deploy.sh', 'ar');

module.exports = { runScript };
