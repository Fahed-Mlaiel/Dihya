/**
 * @file tailwind.config.js
 * @description Configuration Tailwind CSS pour Dihya Coding : garantit un design moderne, l’accessibilité, la robustesse, la conformité RGPD, l’auditabilité, l’extensibilité, la sécurité et la documentation claire.
 * Toutes les options sont commentées pour auditabilité et bonnes pratiques.
 */

module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        // Palette Dihya Coding (accessibilité, design moderne)
        primary: "#2B4C7E",
        secondary: "#F5A623",
        accent: "#E94F37",
        neutral: "#F4F4F4",
        info: "#3ABFF8",
        success: "#36D399",
        warning: "#FBBD23",
        error: "#F87272"
      },
      fontFamily: {
        // Typographie moderne et accessible
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['Fira Mono', 'ui-monospace', 'SFMono-Regular', 'monospace']
      },
      borderRadius: {
        xl: '1.25rem'
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'), // Accessibilité et design des formulaires
    require('@tailwindcss/typography'), // SEO et lisibilité
    require('@tailwindcss/aspect-ratio'), // Responsive images/videos
    require('@tailwindcss/line-clamp') // Gestion du contenu long
  ],
  safelist: [
    // Pour auditabilité et robustesse, garantir certains styles critiques
    'bg-primary', 'text-primary', 'bg-secondary', 'text-secondary'
  ],
  darkMode: 'media', // Accessibilité : support du mode sombre selon les préférences utilisateur
};

/*
  Sécurité & RGPD : 
    - Aucun traitement de données personnelles dans le CSS généré.
    - Les logs et traces sont gérés côté JS, pas dans cette config.
  Auditabilité : 
    - Ce fichier est commenté pour la traçabilité et la conformité.
  Extensibilité : 
    - Ajoutez vos plugins Tailwind selon vos besoins métiers.
  Robustesse : 
    - Compatible avec tous les navigateurs modernes.
  Documentation claire : 
    - Chaque option est expliquée pour faciliter la maintenance.
*/