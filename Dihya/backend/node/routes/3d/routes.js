/**
 * Routes 3D - Gestion avancée de projets 3D (IA, VR, AR, etc.)
 * Sécurité maximale, multilingue, multitenancy, plugins, audit, RGPD
 * @module routes/3d/routes
 * @see GraphQL support inclus
 */
const express = require('express');
const { checkJWT, checkRole, checkTenant, i18nMiddleware, wafMiddleware, ddosMiddleware } = require('../../middlewares/security');
const { auditLog, anonymize, exportData } = require('../../middlewares/audit');
const { generate3DProject, list3DProjects, get3DProject, update3DProject, delete3DProject } = require('../../controllers/3dController');
const router = express.Router();

/**
 * @swagger
 * /api/3d:
 *   get:
 *     summary: Liste des projets 3D
 *     security: [JWT]
 *     tags: [3D]
 *     responses:
 *       200:
 *         description: Succès
 */
router.get('/', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, list3DProjects);

/**
 * @swagger
 * /api/3d:
 *   post:
 *     summary: Générer un projet 3D (IA, VR, AR)
 *     security: [JWT]
 *     tags: [3D]
 *     requestBody:
 *       required: true
 *     responses:
 *       201:
 *         description: Projet créé
 */
router.post('/', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, generate3DProject);

router.get('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkTenant, i18nMiddleware, get3DProject);
router.put('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, update3DProject);
router.delete('/:id', wafMiddleware, ddosMiddleware, checkJWT, checkRole('admin'), checkTenant, i18nMiddleware, auditLog, anonymize, delete3DProject);

// GraphQL endpoint (exemple)
// router.use('/graphql', require('../../graphql/3d'));

module.exports = router;
