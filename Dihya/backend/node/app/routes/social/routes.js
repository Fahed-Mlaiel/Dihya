/**
 * @fileoverview Routes social pour la gestion avancée des projets IA, VR, AR, etc.
 * Sécurité maximale, multilingue, multitenant, extensible, RGPD, SEO, audit, plugins, IA fallback.
 * @module routes/social
 * @author Dihya Coding
 * @version 1.0.0
 * @license AGPL-3.0
 */

const express = require('express');
const { checkJwt, checkRole, i18nMiddleware, auditLogger, wafMiddleware, ddosProtection } = require('../../middlewares/security');
const { validateSocialInput } = require('../../validators/social');
const { getSocialData, createSocialEntry, updateSocialEntry, deleteSocialEntry } = require('../../controllers/social');
const { pluginManager } = require('../../plugins');
const router = express.Router();

/**
 * @swagger
 * tags:
 *   name: Social
 *   description: Gestion social avancée (multitenant, multilingue, RGPD, audit, plugins)
 */

router.use(i18nMiddleware);
router.use(auditLogger);
router.use(wafMiddleware);
router.use(ddosProtection);

router.get('/', checkJwt, checkRole(['admin', 'user', 'invite']), async (req, res) => {
  try {
    const data = await getSocialData(req);
    res.status(200).json({ success: true, data });
  } catch (err) {
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

router.post('/', checkJwt, checkRole(['admin', 'user']), validateSocialInput, async (req, res) => {
  try {
    const entry = await createSocialEntry(req);
    res.status(201).json({ success: true, entry });
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

router.put('/:id', checkJwt, checkRole(['admin']), validateSocialInput, async (req, res) => {
  try {
    const updated = await updateSocialEntry(req);
    res.status(200).json({ success: true, updated });
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

router.delete('/:id', checkJwt, checkRole(['admin']), async (req, res) => {
  try {
    await deleteSocialEntry(req);
    res.status(204).send();
  } catch (err) {
    res.status(400).json({ success: false, error: req.t('error.invalid_input') });
  }
});

router.use('/plugin', pluginManager('social'));

module.exports = router;
