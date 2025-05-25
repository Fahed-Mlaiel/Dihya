/**
 * Template loisirs avancé pour la génération de politiques loisirs dans Dihya.
 * @module loisirs/template
 * @version 1.0.0
 * @author Dihya Team
 */

'use strict';

const i18n = require('../../utils/i18n');
const { validateUserRole, auditLog } = require('../../utils/security');

/**
 * Génère une politique loisirs personnalisée.
 * @param {Object} options
 * @param {string} options.lang
 * @param {string} options.role
 * @param {Object} options.data
 * @returns {string}
 */
function generateLoisirsPolicy({ lang = 'fr', role = 'user', data = {} }) {
  validateUserRole(role, ['admin', 'user', 'invité']);
  auditLog('generateLoisirsPolicy', { lang, role, data });
  return i18n.t('loisirs.policy', lang, { ...data, role });
}

module.exports = { generateLoisirsPolicy };
