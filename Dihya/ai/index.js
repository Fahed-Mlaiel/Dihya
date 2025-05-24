/**
 * Dihya AI – Point d'entrée module IA (Node.js)
 * Ultra avancé, multilingue, souverain, extensible, sécurisé.
 * Exporte toutes les fonctions et configurations IA pour usage multi-stack.
 *
 * @module DihyaAI
 */

// index.js – Entrée du module IA Dihya (Node/JS)

console.log("Dihya AI module – NLP, ML, fallback open source, multilingue, sécurité, audit.");
// ...lancer les tests, les scripts, l’audit, etc.

const { generateAIResponse, selectEngine, SUPPORTED_LANGUAGES, config } = require('./ai');

// Middleware Express pour intégration API REST
function aiMiddleware(req, res, next) {
  const { prompt, lang, engine } = req.body;
  const userId = req.user?.id || 'anonymous';
  const role = req.user?.role || 'user';

  generateAIResponse({ prompt, userId, lang, role, engine })
    .then(result => res.json(result))
    .catch(err => {
      res.status(400).json({ error: err.message });
    });
}

// Exemple d'intégration Express.js
// const express = require('express');
// const router = express.Router();
// router.post('/ai/generate', aiMiddleware);

module.exports = {
  generateAIResponse,
  selectEngine,
  SUPPORTED_LANGUAGES,
  config,
  aiMiddleware,
};
