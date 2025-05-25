/**
 * Dihya VR/AR Template - template.js
 * Prêt à l’emploi pour projets VR/AR (WebXR, A-Frame, Babylon.js)
 * Sécurité, i18n, plugins, REST/GraphQL, audit, RGPD, IA fallback
 * @module vr_ar_template
 * @author Dihya Coding
 * @license MIT
 */

'use strict';

const { t, sanitize, auditLog } = require('../../../frontend/src/utils/utils.js');
const jwt = require('jsonwebtoken');

/**
 * Initialisation d’une expérience VR/AR sécurisée
 * @param {object} options - { lang, user, plugins, ... }
 * @returns {object} - Objet expérience VR/AR
 */
function initVRARExperience(options = {}) {
  const lang = options.lang || 'fr';
  auditLog('init_vr_ar_experience', { user: options.user || 'guest', lang });
  const experience = { entities: [], lang, plugins: options.plugins || [] };
  if (experience.plugins.length) {
    experience.plugins.forEach(async p => await require(`../../../plugins/${p}/index.js`));
  }
  return experience;
}

/**
 * Ajout d’une entité VR/AR avec validation et audit
 * @param {object} experience
 * @param {object} entity - { type, params }
 * @param {string} token - JWT utilisateur
 * @returns {boolean}
 */
function addEntityVRAR(experience, entity, token) {
  try {
    const user = jwt.verify(token, process.env.JWT_SECRET || 'dihya_secret');
    if (!user.roles.includes('admin') && !user.roles.includes('user')) throw new Error('Unauthorized');
    if (!['avatar', 'object', 'marker', 'custom'].includes(entity.type)) throw new Error('Invalid type');
    experience.entities.push({ ...entity, createdBy: user.id });
    auditLog('add_entity_vr_ar', { user: user.id, type: entity.type });
    return true;
  } catch (e) {
    auditLog('add_entity_vr_ar_failed', { error: e.message });
    return false;
  }
}

module.exports = { initVRARExperience, addEntityVRAR };
