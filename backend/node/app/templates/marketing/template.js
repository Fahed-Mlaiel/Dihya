/**
 * Template marketing avancé pour la génération de politiques marketing dans Dihya.
 * @module marketing/template
 * @version 1.0.0
 * @author Dihya Team
 */

'use strict';

const i18n = require('../../utils/i18n');
const { validateUserRole, auditLog } = require('../../utils/security');

/**
 * Génère une politique marketing personnalisée.
 * @param {Object} options
 * @param {string} options.lang
 * @param {string} options.role
 * @param {Object} options.data
 * @returns {string}
 */
function generateMarketingPolicy({ lang = 'fr', role = 'user', data = {} }) {
  validateUserRole(role, ['admin', 'user', 'invité']);
  auditLog('generateMarketingPolicy', { lang, role, data });
  return i18n.t('marketing.policy', lang, { ...data, role });
}

module.exports = { generateMarketingPolicy };
