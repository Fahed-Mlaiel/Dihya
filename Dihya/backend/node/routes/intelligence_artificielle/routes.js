"use strict";
/**
 * @fileoverview Routes pour la gestion des projets Intelligence Artificielle.
 * @module routes/intelligence_artificielle
 * @description API REST & GraphQL IA, sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO, fallback IA open source, etc.
 * @author Dihya Team
 * @version 1.0.0
 * @license MIT
 */
const express = require("express");
const { checkJwt, checkRole, validateBody, auditLog, i18nMiddleware, wafMiddleware, ddosMiddleware } = require("../../../../middlewares/security");
const { projectSchema } = require("../../../../schemas/project");
const { getIAFallback } = require("../../../../services/ia_fallback");
const { seoLogger } = require("../../../../middlewares/seo");
const { pluginManager } = require("../../../../plugins/pluginManager");
const router = express.Router();

router.get("/projects", [checkJwt, checkRole(["admin", "user"]), i18nMiddleware, wafMiddleware, ddosMiddleware, seoLogger], async (req, res) => {
  res.json({ success: true, projects: [], i18n: req.i18n });
});

router.post("/projects", [checkJwt, checkRole(["admin"]), validateBody(projectSchema), auditLog, i18nMiddleware, wafMiddleware, ddosMiddleware, seoLogger], async (req, res) => {
  res.status(201).json({ success: true, project: req.body, i18n: req.i18n });
});

const { graphqlHTTP } = require("express-graphql");
const { iaSchema } = require("../../../../graphql/schemas/intelligence_artificielle");
router.use("/graphql", [checkJwt, i18nMiddleware, wafMiddleware, ddosMiddleware], graphqlHTTP({
  schema: iaSchema,
  graphiql: true,
}));

router.use("/plugins", pluginManager("intelligence_artificielle"));

module.exports = router;
