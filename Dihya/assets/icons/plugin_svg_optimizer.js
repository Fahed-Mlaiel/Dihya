// Plugin d’optimisation SVG pour Dihya Icons (Node.js)
// Optimise les SVG du dossier pour accessibilité, poids, sécurité, RGPD
const fs = require('fs');
const path = require('path');
const { optimize } = require('svgo');

const ICONS_DIR = __dirname;

fs.readdirSync(ICONS_DIR).forEach(file => {
  if (file.endsWith('.svg')) {
    const filePath = path.join(ICONS_DIR, file);
    const svg = fs.readFileSync(filePath, 'utf8');
    const result = optimize(svg, {
      multipass: true,
      plugins: [
        'removeDimensions',
        'removeScriptElement',
        'removeStyleElement',
        'removeComments',
        'removeMetadata',
        'removeTitle',
        'removeDesc',
        {
          name: 'addAttributesToSVGElement',
          params: {
            attributes: [{ 'focusable': 'false' }]
          }
        }
      ]
    });
    fs.writeFileSync(filePath, result.data, 'utf8');
    console.log(`Optimisé: ${file}`);
  }
});
