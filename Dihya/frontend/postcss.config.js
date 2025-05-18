/**
 * @file postcss.config.js
 * @description Configuration PostCSS pour Dihya Coding : garantit un design moderne, la robustesse, la conformité RGPD, l’auditabilité, l’extensibilité, la sécurité et la documentation claire.
 * Toutes les options sont commentées pour auditabilité et bonnes pratiques.
 */

module.exports = {
  // Plugins PostCSS utilisés pour la génération moderne, l’accessibilité et la robustesse
  plugins: {
    // Ajoute les préfixes pour la compatibilité navigateurs (SEO/accessibilité)
    'autoprefixer': {
      overrideBrowserslist: [
        '>0.2%',
        'not dead',
        'not op_mini all'
      ]
    },
    // Permet l’utilisation de variables CSS modernes et fallback
    'postcss-preset-env': {
      stage: 2,
      features: {
        'nesting-rules': true,
        'custom-properties': true
      },
      autoprefixer: { grid: true }
    },
    // Optimise la minification CSS pour la performance et le SEO
    'cssnano': process.env.NODE_ENV === 'production' ? {
      preset: 'default'
    } : false
  }
};

/*
  Sécurité & RGPD : 
    - Aucun traitement de données personnelles dans le CSS.
    - Les logs et traces sont gérés côté JS, pas dans cette config.
  Auditabilité : 
    - Ce fichier est commenté pour la traçabilité et la conformité.
  Extensibilité : 
    - Ajoutez vos plugins PostCSS selon vos besoins métiers.
  Robustesse : 
    - Compatible avec tous les navigateurs modernes.
  Documentation claire : 
    - Chaque option est expliquée pour faciliter la maintenance.
*/