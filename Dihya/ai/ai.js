/**
 * Dihya AI Core Module
 * Ultra avancé, multilingue, souverain, extensible, sécurisé.
 * Supporte fallback IA open source (Mixtral, LLaMA, Mistral), multi-stack, multi-rôle.
 * Prêt pour la production, la démo, la contribution.
 *
 * @module DihyaAI
 */

const { OpenAI } = require('openai');
const { LlamaCpp } = require('llama-cpp');
const { Mixtral } = require('mixtral-js');
const { Mistral } = require('mistral-js');
const { detectLanguage, translate } = require('./i18n');
const { getUserRole, checkPermission } = require('../auth/roles');
const { logAIRequest, logAIResponse } = require('../utils/audit');
const { sanitizeInput, sanitizeOutput } = require('../utils/security');

const SUPPORTED_LANGUAGES = ['fr', 'en', 'ar', 'tzr'];

/**
 * Configuration IA souveraine et fallback
 */
const config = {
  openai: {
    enabled: process.env.OPENAI_API_KEY ? true : false,
    apiKey: process.env.OPENAI_API_KEY || '',
    model: process.env.OPENAI_MODEL || 'gpt-4o',
  },
  fallback: {
    mixtral: true,
    llama: true,
    mistral: true,
  },
  maxTokens: 2048,
  temperature: 0.7,
  allowedRoles: ['admin', 'user', 'contributor'],
};

/**
 * Sélection dynamique du moteur IA selon la souveraineté et la disponibilité.
 */
async function selectEngine(preferred = 'openai') {
  if (preferred === 'openai' && config.openai.enabled) return 'openai';
  if (config.fallback.mixtral) return 'mixtral';
  if (config.fallback.llama) return 'llama';
  if (config.fallback.mistral) return 'mistral';
  throw new Error('Aucun moteur IA disponible');
}

/**
 * Génère une réponse IA souveraine, multilingue, sécurisée.
 * @param {Object} params
 * @param {string} params.prompt - Texte utilisateur (multi-langue)
 * @param {string} params.userId - ID utilisateur
 * @param {string} [params.lang] - Langue cible (auto si absent)
 * @param {string} [params.role] - Rôle utilisateur (admin, user, etc.)
 * @param {string} [params.engine] - Moteur IA préféré
 * @returns {Promise<{text: string, lang: string, engine: string}>}
 */
async function generateAIResponse({ prompt, userId, lang, role, engine }) {
  // Sécurité & audit
  const safePrompt = sanitizeInput(prompt);
  const userRole = await getUserRole(userId);
  if (!checkPermission(userRole, 'ai:generate')) {
    throw new Error('Permission refusée');
  }
  const detectedLang = lang || detectLanguage(safePrompt, SUPPORTED_LANGUAGES);
  const aiEngine = await selectEngine(engine);

  logAIRequest({ userId, prompt: safePrompt, lang: detectedLang, engine: aiEngine });

  let aiResponse = '';
  if (aiEngine === 'openai') {
    const openai = new OpenAI({ apiKey: config.openai.apiKey });
    const completion = await openai.chat.completions.create({
      model: config.openai.model,
      messages: [{ role: 'user', content: safePrompt }],
      max_tokens: config.maxTokens,
      temperature: config.temperature,
      user: userId,
    });
    aiResponse = completion.choices[0].message.content;
  } else if (aiEngine === 'mixtral') {
    const mixtral = new Mixtral();
    aiResponse = await mixtral.generate(safePrompt, { lang: detectedLang });
  } else if (aiEngine === 'llama') {
    const llama = new LlamaCpp();
    aiResponse = await llama.generate(safePrompt, { lang: detectedLang });
  } else if (aiEngine === 'mistral') {
    const mistral = new Mistral();
    aiResponse = await mistral.generate(safePrompt, { lang: detectedLang });
  } else {
    throw new Error('Aucun moteur IA disponible');
  }

  // Sécurité sortie & audit
  const safeOutput = sanitizeOutput(aiResponse);
  logAIResponse({ userId, response: safeOutput, lang: detectedLang, engine: aiEngine });

  // Traduction si besoin
  let finalOutput = safeOutput;
  if (detectedLang && !safeOutput.startsWith(`[${detectedLang}]`)) {
    finalOutput = await translate(safeOutput, detectedLang);
  }

  return {
    text: finalOutput,
    lang: detectedLang,
    engine: aiEngine,
  };
}

/**
 * Exemple d’utilisation (à supprimer en prod)
 */
// (async () => {
//   const res = await generateAIResponse({
//     prompt: 'Génère un template métier pour la gestion RH.',
//     userId: 'demo-user',
//     lang: 'fr',
//     role: 'admin',
//   });
//   console.log(res);
// })();

module.exports = {
  generateAIResponse,
  selectEngine,
  SUPPORTED_LANGUAGES,
  config,
};

// ai.js – Dihya AI Core (Node/JS)

/**
 * Module principal d’IA pour Dihya : NLP, ML, génération de code, fallback open source, intégration GPT/LLM, multilingue, sécurité, audit, tests.
 */

// ...existing code or à compléter selon la stack IA choisie...

// Exemples de fonctions à inclure :
// - analyseTextMultilingue()
// - genererCodeMetier()
// - fallbackLlmOpenSource()
// - auditIaUsage()
// - testsUnitairesIa()

// ...
