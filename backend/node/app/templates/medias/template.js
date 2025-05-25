/**
 * Template médias avancé pour la génération de politiques médias dans Dihya.
 * @module medias/template
 * @version 1.0.0
 * @author Dihya Team
 */

'use strict';

const i18n = require('../../utils/i18n');
const { validateUserRole, auditLog } = require('../../utils/security');

/**
 * Génère une politique médias personnalisée.
 * @param {Object} options
 * @param {string} options.lang
 * @param {string} options.role
 * @param {Object} options.data
 * @returns {string}
 */
function generateMediasPolicy({ lang = 'fr', role = 'user', data = {} }) {
  validateUserRole(role, ['admin', 'user', 'invité']);
  auditLog('generateMediasPolicy', { lang, role, data });
  return i18n.t('medias.policy', lang, { ...data, role });
}

module.exports = { generateMediasPolicy };
