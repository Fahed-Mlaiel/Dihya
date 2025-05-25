/**
 * Template logistique avancé pour la génération de politiques logistiques dans Dihya.
 * @module logistique/template
 * @version 1.0.0
 * @author Dihya Team
 */

'use strict';

const i18n = require('../../utils/i18n');
const { validateUserRole, auditLog } = require('../../utils/security');

/**
 * Génère une politique logistique personnalisée.
 * @param {Object} options
 * @param {string} options.lang
 * @param {string} options.role
 * @param {Object} options.data
 * @returns {string}
 */
function generateLogistiquePolicy({ lang = 'fr', role = 'user', data = {} }) {
  validateUserRole(role, ['admin', 'user', 'invité']);
  auditLog('generateLogistiquePolicy', { lang, role, data });
  return i18n.t('logistique.policy', lang, { ...data, role });
}

module.exports = { generateLogistiquePolicy };
