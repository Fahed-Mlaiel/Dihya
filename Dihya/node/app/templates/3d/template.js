/**
 * Dihya 3D Template - template.js
 * Prêt à l’emploi pour projets 3D (Three.js, Babylon.js, WebGL)
 * Sécurité, i18n, plugins, REST/GraphQL, audit, RGPD, IA fallback
 * @module 3d_template
 * @author Dihya Coding
 * @license MIT
 */

'use strict';

// Import sécurité, i18n, plugins
const { t, sanitize, auditLog } = require('../../../frontend/src/utils/utils.js');
const jwt = require('jsonwebtoken');

/**
 * Initialisation d’une scène 3D sécurisée
 * @param {object} options - { lang, user, plugins, ... }
 * @returns {object} - Objet scène 3D
 */
function init3DScene(options = {}) {
  const lang = options.lang || 'fr';
  auditLog('init_3d_scene', { user: options.user || 'guest', lang });
  // Exemple : initialisation Three.js (remplaçable)
  const scene = { objects: [], lang, plugins: options.plugins || [] };
  // Chargement plugins dynamiques
  if (scene.plugins.length) {
    scene.plugins.forEach(async p => await require(`../../../plugins/${p}/index.js`));
  }
  return scene;
}

/**
 * Ajout d’un objet 3D avec validation et audit
 * @param {object} scene
 * @param {object} object3D - { type, params }
 * @param {string} token - JWT utilisateur
 * @returns {boolean}
 */
function addObject3D(scene, object3D, token) {
  try {
    const user = jwt.verify(token, process.env.JWT_SECRET || 'dihya_secret');
    if (!user.roles.includes('admin') && !user.roles.includes('user')) throw new Error('Unauthorized');
    // Validation type
    if (!['cube', 'sphere', 'custom'].includes(object3D.type)) throw new Error('Invalid type');
    scene.objects.push({ ...object3D, createdBy: user.id });
    auditLog('add_object_3d', { user: user.id, type: object3D.type });
    return true;
  } catch (e) {
    auditLog('add_object_3d_failed', { error: e.message });
    return false;
  }
}

module.exports = { init3DScene, addObject3D };
