// Plugin d’export RGPD des métadonnées des logos Dihya (Node.js)
const fs = require('fs');
const path = require('path');
const meta = require('./meta_logos.json');

function exportRGPD(format = 'json') {
  const out = path.join(__dirname, `meta_logos_export.${format}`);
  if (format === 'json') {
    fs.writeFileSync(out, JSON.stringify(meta, null, 2), 'utf8');
  } else if (format === 'csv') {
    const keys = Object.keys(meta);
    const values = keys.map(k => JSON.stringify(meta[k]));
    fs.writeFileSync(out, keys.join(',') + '\n' + values.join(','), 'utf8');
  } else if (format === 'yaml') {
    let yaml = '';
    for (const k in meta) {
      yaml += `${k}: ${JSON.stringify(meta[k])}\n`;
    }
    fs.writeFileSync(out, yaml, 'utf8');
  }
  console.log(`Export RGPD: ${out}`);
}

if (require.main === module) {
  exportRGPD(process.argv[2] || 'json');
}

module.exports = exportRGPD;
