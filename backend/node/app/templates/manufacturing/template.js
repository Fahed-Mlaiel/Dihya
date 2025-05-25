/**
 * Template manufacturing avancé pour la génération de politiques manufacturing dans Dihya.
 * @module manufacturing/template
 * @version 1.0.0
 * @author Dihya Team
 */

'use strict';

const i18n = require('../../utils/i18n');
const { validateUserRole, auditLog } = require('../../utils/security');

/**
 * Génère une politique manufacturing personnalisée.
 * @param {Object} options
 * @param {string} options.lang
 * @param {string} options.role
 * @param {Object} options.data
 * @returns {string}
 */
function generateManufacturingPolicy({ lang = 'fr', role = 'user', data = {} }) {
  validateUserRole(role, ['admin', 'user', 'invité']);
  auditLog('generateManufacturingPolicy', { lang, role, data });
  return i18n.t('manufacturing.policy', lang, { ...data, role });
}

module.exports = { generateManufacturingPolicy };
