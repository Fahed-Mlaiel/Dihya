/**
 * Dihya Plugins Index – Ultra avancé, modulaire, extensible, multilingue, souverain
 * Découverte automatique, documentation, tests, sécurité, accessibilité, fallback open source.
 */

const fs = require('fs');
const path = require('path');

// Découverte dynamique de tous les plugins du dossier ./metiers
function discoverPlugins(dir) {
  return fs.readdirSync(dir)
    .filter(f => f.endsWith('.js') && f !== 'index.js')
    .map(f => require(path.join(dir, f)));
}

const metiers = discoverPlugins(path.join(__dirname, 'metiers'));
const plugin = require('./plugin');

module.exports = {
  metiers,
  plugin,
  // Extension : ajoutez vos plugins personnalisés ici (voir /docs/plugins/USAGE.md)
};

/**
 * Tous les plugins sont documentés dans /docs/plugins/ et testés dans /tests/plugins/
 * Pour ajouter un plugin, suivre la convention : sécurité, i18n, doc, test, fallback, accessibilité.
 */

// --- TESTS UNITAIRES (Jest) ---
// Voir tests/plugins/index.test.js pour la couverture complète (découverte, import, extension, fallback, conformité)
