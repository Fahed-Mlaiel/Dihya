/**
 * @fileoverview Routes juridiques pour la gestion avancée des projets IA, VR, AR, etc.
 * Sécurité maximale, multilingue, multitenant, extensible, RGPD, SEO, audit, plugins, IA fallback.
 * @module routes/juridique
 * @author Dihya Coding
 * @version 1.0.0
 * @license AGPL-3.0
 */

const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLogger, wafMiddleware, ddosProtection } = require('../../middlewares/security');
const { validateJuridiqueInput } = require('../../validators/juridique');
const { getJuridiqueData, createJuridiqueEntry, updateJuridiqueEntry, deleteJuridiqueEntry } = require('../../controllers/juridique');
const { pluginManager } = require('../../plugins');
const router = express.Router();

/**
 * @swagger
 * tags:
 *   name: Juridique
 *   description: Gestion juridique avancée (multitenant, multilingue, RGPD, audit, plugins)
 */

// Middlewares globaux
router.use(i18nMiddleware);
router.use(auditLogger);
router.use(wafMiddleware);
router.use(ddosProtection);

/**
 * @route GET /juridique
 * @desc Liste des données juridiques (admin, user, invité)
 * @access Roles: admin, user, invite
 */
router.get('/', checkJwt, checkRole(['admin', 'user', 'invite']), async (req, res) => {
  try {
    const data = await getJuridiqueData(req);
    res.status(200).json({ success: true, data });
  } catch (err) {
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

/**
 * @route POST /juridique
 * @desc Création d'une entrée juridique (admin, user)
 * @access Roles: admin, user
 */
router.post('/', checkJwt, checkRole(['admin', 'user']), validateJuridiqueInput, async (req, res) => {
  try {
    const entry = await createJuridiqueEntry(req);
    res.status(201).json({ success: true, entry });
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

/**
 * @route PUT /juridique/:id
 * @desc Mise à jour d'une entrée juridique (admin)
 * @access Roles: admin
 */
router.put('/:id', checkJwt, checkRole(['admin']), validateJuridiqueInput, async (req, res) => {
  try {
    const updated = await updateJuridiqueEntry(req);
    res.status(200).json({ success: true, updated });
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

/**
 * @route DELETE /juridique/:id
 * @desc Suppression d'une entrée juridique (admin)
 * @access Roles: admin
 */
router.delete('/:id', checkJwt, checkRole(['admin']), async (req, res) => {
  try {
    await deleteJuridiqueEntry(req);
    res.status(204).send();
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

// Plugins dynamiques (exemple)
router.use('/plugin', pluginManager('juridique'));

module.exports = router;
