/**
 * @fileoverview Routes VR/AR pour la gestion avancée des projets IA, VR, AR, etc.
 * Sécurité maximale, multilingue, multitenant, extensible, RGPD, SEO, audit, plugins, IA fallback.
 * @module routes/vr_ar
 * @author Dihya Coding
 * @version 1.0.0
 * @license AGPL-3.0
 */

const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLogger, wafMiddleware, ddosProtection } = require('../../middlewares/security');
const { validateVRARInput } = require('../../validators/vr_ar');
const { getVRARData, createVRAREntry, updateVRAREntry, deleteVRAREntry } = require('../../controllers/vr_ar');
const { pluginManager } = require('../../plugins');
const router = express.Router();

/**
 * @swagger
 * tags:
 *   name: VRAR
 *   description: Gestion VR/AR avancée (multitenant, multilingue, RGPD, audit, plugins)
 */

router.use(i18nMiddleware);
router.use(auditLogger);
router.use(wafMiddleware);
router.use(ddosProtection);

router.get('/', checkJwt, checkRole(['admin', 'user', 'invite']), async (req, res) => {
  try {
    const data = await getVRARData(req);
    res.status(200).json({ success: true, data });
  } catch (err) {
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

router.post('/', checkJwt, checkRole(['admin', 'user']), validateVRARInput, async (req, res) => {
  try {
    const entry = await createVRAREntry(req);
    res.status(201).json({ success: true, entry });
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

router.put('/:id', checkJwt, checkRole(['admin']), validateVRARInput, async (req, res) => {
  try {
    const updated = await updateVRAREntry(req);
    res.status(200).json({ success: true, updated });
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

router.delete('/:id', checkJwt, checkRole(['admin']), async (req, res) => {
  try {
    await deleteVRAREntry(req);
    res.status(204).send();
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

router.use('/plugin', pluginManager('vr_ar'));

module.exports = router;
