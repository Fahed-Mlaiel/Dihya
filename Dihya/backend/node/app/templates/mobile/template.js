/**
 * Mobile Template - Dihya
 *
 * @module mobile/template
 * @description Template REST/GraphQL pour gestion mobile IA/VR/AR.
 * @i18n Support: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @security CORS, JWT, validation, audit, WAF, anti-DDOS
 * @roles admin, user, invité
 * @plugins extensible
 * @seo robots, sitemap, logs
 * @compliance RGPD, auditabilité
 */

const express = require('express');
const router = express.Router();
const { checkJwt, checkRole, i18nMiddleware } = require('../../middlewares');
const { generateMobileProject } = require('../../services/mobileService');

/**
 * @route POST /api/mobile/generate
 * @desc Génère un projet mobile IA/VR/AR
 * @access admin, user
 * @returns {object} Projet généré
 */
router.post('/generate', checkJwt, checkRole(['admin', 'user']), i18nMiddleware, async (req, res) => {
  try {
    const { type, lang } = req.body;
    const project = await generateMobileProject(type, lang);
    res.status(201).json({ success: true, project });
  } catch (err) {
    req.auditLog('mobile_generate_error', { error: err.message });
    res.status(500).json({ success: false, error: req.t('error.internal') });
  }
});

module.exports = router;
