/**
 * @file routes.js
 * @description Constantes des routes de navigation et API pour Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité et documentation claire.
 * Aucun secret, donnée personnelle ou sensible n’est stocké ici.
 */

/**
 * Routes de navigation principales (UI).
 * @readonly
 * @type {Object.<string, string>}
 */
export const NAV_ROUTES = Object.freeze({
  HOME: '/',
  GENERATE: '/generate',
  PREVIEW: '/preview',
  PROJECTS: '/projects',
  DASHBOARD: '/dashboard',
  BACKUPS: '/backups',
  SETTINGS: '/settings',
  ABOUT: '/about',
  CONTACT: '/contact',
  DOCS: '/docs/user_guide/README.md',
  LOGIN: '/login',
  LEGAL: '/legal',
  PRIVACY: '/privacy',
  ACCESSIBILITY: '/accessibility',
});

/**
 * Routes API principales (backend).
 * @readonly
 * @type {Object.<string, string>}
 */
export const API_ROUTES = Object.freeze({
  LOGIN: '/api/auth/login',
  LOGOUT: '/api/auth/logout',
  REGISTER: '/api/auth/register',
  USER: '/api/user/me',
  PROJECTS: '/api/projects',
  PROJECT: '/api/projects/:id',
  GENERATE: '/api/generate',
  BACKUP: '/api/backup',
  BACKUP_LIST: '/api/backup/list',
  BACKUP_DELETE: '/api/backup/delete/:id',
  BACKUP_GITHUB: '/api/backup/github',
  BACKUP_NOTION: '/api/backup/notion',
  CHAT_ASSISTANT: '/api/assistant/chat',
  VOICE_TRANSCRIBE: '/api/voice/transcribe',
});

/**
 * Valide une route de navigation.
 * @param {string} route
 * @returns {boolean}
 */
export function isValidNavRoute(route) {
  return Object.values(NAV_ROUTES).includes(route);
}

/**
 * Valide une route API.
 * @param {string} route
 * @returns {boolean}
 */
export function isValidApiRoute(route) {
  return Object.values(API_ROUTES).some(apiRoute =>
    apiRoute === route || (apiRoute.includes(':') && matchDynamicRoute(apiRoute, route))
  );
}

/**
 * Vérifie la correspondance d’une route dynamique (ex: /api/projects/:id).
 * @param {string} pattern
 * @param {string} route
 * @returns {boolean}
 */
function matchDynamicRoute(pattern, route) {
  const regex = new RegExp('^' + pattern.replace(/:[^/]+/g, '[^/]+') + '$');
  return regex.test(route);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} route
 */
export function logRouteEvent(action, route) {
  try {
    const logs = JSON.parse(localStorage.getItem('route_logs') || '[]');
    logs.push({
      action,
      route,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('route_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de routes locaux (droit à l’oubli RGPD).
 */
export function clearLocalRouteLogs() {
  localStorage.removeItem('route_logs');
}