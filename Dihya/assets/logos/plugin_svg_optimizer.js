// Plugin d’optimisation SVG pour Dihya Logos (Node.js)
const fs = require('fs');
const path = require('path');
const { optimize } = require('svgo');

const LOGOS_DIR = __dirname;

fs.readdirSync(LOGOS_DIR).forEach(file => {
  if (file.endsWith('.svg')) {
    const filePath = path.join(LOGOS_DIR, file);
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
