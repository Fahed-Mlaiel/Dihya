/**
 * Dihya Design Assets Index
 * Exporte images, polices, thèmes, helpers d'accessibilité, multilingue, souverain, documenté.
 */

const images = {
  logo: '/assets/images/dihya.svg',
  favicon: '/assets/images/favicon.ico',
  // ...autres images...
};

const fonts = {
  montserrat: '/assets/fonts/Montserrat.woff2',
  inter: '/assets/fonts/Inter.woff2',
  roboto: '/assets/fonts/Roboto.woff2',
  // ...autres polices...
};

const themes = require('../system');

function getImage(name = 'logo') {
  return images[name] || images.logo;
}

function getFont(name = 'montserrat') {
  return fonts[name] || fonts.montserrat;
}

module.exports = {
  images,
  fonts,
  themes,
  getImage,
  getFont,
};
