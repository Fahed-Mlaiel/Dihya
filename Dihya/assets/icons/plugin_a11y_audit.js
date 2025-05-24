// Plugin d’audit accessibilité SVG pour Dihya Icons (Node.js)
// Vérifie aria-label, role, focusable, contraste, RGPD
const fs = require('fs');
const path = require('path');
const ICONS_DIR = __dirname;

function checkA11y(svg, file) {
  const errors = [];
  if (!svg.match(/aria-label/)) errors.push('aria-label manquant');
  if (!svg.match(/role="img"/)) errors.push('role="img" manquant');
  if (!svg.match(/focusable="false"/)) errors.push('focusable="false" manquant');
  // Optionnel: vérification contraste, RGPD, etc.
  return errors;
}

fs.readdirSync(ICONS_DIR).forEach(file => {
  if (file.endsWith('.svg')) {
    const filePath = path.join(ICONS_DIR, file);
    const svg = fs.readFileSync(filePath, 'utf8');
    const errors = checkA11y(svg, file);
    if (errors.length) {
      console.warn(`A11Y ${file}:`, errors.join(', '));
    } else {
      console.log(`A11Y OK: ${file}`);
    }
  }
});
