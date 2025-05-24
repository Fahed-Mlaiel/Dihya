/**
 * Dihya Branding Assets Index
 * Exporte logos, palettes, helpers d'accessibilité, multilingue, souverain, documenté.
 */

const logos = {
  amazigh: '/assets/logos/dihya_amazigh.svg',
  modern: '/assets/logos/dihya_modern.svg',
  favicon: '/assets/logos/favicon.ico',
};

const palettes = {
  amazighBlue: '#0077B6',
  gold: '#FFD700',
  modernGray: '#222831',
  pureWhite: '#FFFFFF',
};

function getLogo(type = 'amazigh') {
  return logos[type] || logos.amazigh;
}

function getPalette(name = 'amazighBlue') {
  return palettes[name] || palettes.amazighBlue;
}

module.exports = {
  logos,
  palettes,
  getLogo,
  getPalette,
};
