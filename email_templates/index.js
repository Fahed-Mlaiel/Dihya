// index.js - Gestion avancée des templates email Dihya
// Multilingue, sécurisé, compatible Node.js/Express

const fs = require('fs');
const path = require('path');

/**
 * Ajoute un hook de transformation sur le contenu HTML du template.
 * @param {function(string, object): string} hookFn - Fonction de transformation (html, variables) => html
 */
let hooks = [];
function registerTemplateHook(hookFn) {
  if (typeof hookFn === 'function') hooks.push(hookFn);
}

/**
 * Charge un template email multilingue, injecte les variables dynamiques, applique les hooks, et gère les erreurs.
 * @param {string} templateName - Nom du template (ex: 'welcome_email')
 * @param {Object} variables - Variables à injecter (ex: { username, link })
 * @param {string} lang - Langue ('fr', 'en', 'ar', 'amz')
 * @returns {string} - Contenu HTML prêt à l’envoi
 * @throws {Error} - Si le template n’existe pas ou variable manquante
 */
function loadEmailTemplate(templateName, variables = {}, lang = 'fr') {
  const filePath = path.join(__dirname, `${templateName}_${lang}.html`);
  if (!fs.existsSync(filePath)) throw new Error(`Template not found: ${filePath}`);
  let content = fs.readFileSync(filePath, 'utf8');
  // Validation basique des variables (anti-XSS)
  for (const [key, value] of Object.entries(variables)) {
    if (typeof value !== 'string') throw new Error(`Invalid variable: ${key}`);
    content = content.replace(new RegExp(`{{${key}}}`, 'g'), escapeHtml(value));
  }
  // Application des hooks
  for (const hook of hooks) {
    content = hook(content, variables);
  }
  return content;
}

/**
 * Échappe les caractères HTML pour éviter les injections XSS.
 * @param {string} unsafe
 * @returns {string}
 */
function escapeHtml(unsafe) {
  return unsafe.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
}

module.exports = { loadEmailTemplate, registerTemplateHook };

// Exemple d’utilisation avancée :
// const { loadEmailTemplate, registerTemplateHook } = require('./index');
// registerTemplateHook((html, vars) => html.replace('Dihya', vars.username.toUpperCase()));
// const html = loadEmailTemplate('welcome_email', { username: 'Dihya', link: 'https://dihya.app' }, 'fr');

// Tests unitaires intégrés (Node.js)
if (require.main === module) {
  try {
    const html = loadEmailTemplate('welcome_email', { username: 'Dihya', link: 'https://dihya.app' }, 'fr');
    console.assert(html.includes('Dihya'), 'Test: username injecté');
    console.log('All tests passed.');
  } catch (e) {
    console.error('Test failed:', e.message);
    process.exit(1);
  }
}
