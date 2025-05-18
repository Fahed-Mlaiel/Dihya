/**
 * @file tailwind.config.js
 * @description Configuration Tailwind CSS pour Dihya Coding : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Respecte les bonnes pratiques CSS, responsive, dark/light, contrastes, focus, animations accessibles.
 */

module.exports = {
  content: [
    '../../**/*.html',
    '../../**/*.js',
    '../../**/*.jsx',
    '../../**/*.ts',
    '../../**/*.tsx',
    '../../**/*.md',
    '../../**/*.svelte',
    '../../**/*.vue'
  ],
  darkMode: 'media', // ou 'class' pour gestion manuelle
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2563eb',
          dark: '#1e40af',
          light: '#60a5fa'
        },
        secondary: {
          DEFAULT: '#facc15',
          dark: '#b45309',
          light: '#fde68a'
        },
        background: {
          light: '#f9fafb',
          dark: '#181a1b'
        },
        surface: {
          light: '#fff',
          dark: '#23272f'
        }
      },
      fontFamily: {
        sans: ['Inter', 'Segoe UI', 'Arial', 'sans-serif']
      },
      borderRadius: {
        DEFAULT: '0.375em'
      },
      transitionProperty: {
        width: 'width',
        spacing: 'margin, padding'
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/line-clamp')
  ],
  safelist: [
    'sr-only', 'focus-visible', 'hidden'
  ],
  // RGPD & sécurité : pas de classes dynamiques générées à partir de données utilisateur
  // Auditabilité : documentez toute extension ou modification dans ce fichier
};