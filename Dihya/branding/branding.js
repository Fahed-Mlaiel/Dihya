/**
 * Dihya Branding Module
 * Multilingue, souverain, accessible, documenté, prêt à l'emploi.
 * Fournit palette, logos, thèmes, helpers accessibilité pour le frontend.
 */

const palette = {
  amazighBlue: '#0077B6',
  gold: '#FFD700',
  modernGray: '#222831',
  pureWhite: '#FFFFFF',
};

const logos = {
  amazigh: '/assets/logos/dihya_amazigh.svg',
  modern: '/assets/logos/dihya_modern.svg',
  favicon: '/assets/logos/favicon.ico',
};

const themes = {
  amazigh: {
    primary: palette.amazighBlue,
    secondary: palette.gold,
    background: palette.pureWhite,
    text: palette.modernGray,
  },
  modern: {
    primary: palette.modernGray,
    secondary: palette.gold,
    background: palette.pureWhite,
    text: palette.amazighBlue,
  },
};

function getLogo(type = 'amazigh') {
  return logos[type] || logos.amazigh;
}

function getTheme(name = 'amazigh') {
  return themes[name] || themes.amazigh;
}

function getAccessibleColor(hex, fallback = '#000') {
  // Simple contrast checker (à améliorer selon WCAG)
  if (!hex) return fallback;
  return hex.toLowerCase() === '#ffffff' ? '#222831' : '#fff';
}

module.exports = {
  palette,
  logos,
  themes,
  getLogo,
  getTheme,
  getAccessibleColor,
};
