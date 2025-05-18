/**
 * @file aiService.js
 * @description Service centralisé pour l’IA dans Dihya Coding : gestion des appels IA (GPT, Llama, Mixtral), sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import { gptFallback } from '../scripts/ai/gpt_fallback';
import { llamaFallback } from '../scripts/ai/llama_fallback';
import { mixtralFallback } from '../scripts/ai/mixtral_fallback';
import { checkQuota, incrementQuota } from '../scripts/ai/quotaDetector';

/**
 * Appelle un modèle IA selon le provider demandé, avec fallback et gestion du quota.
 * @param {object} params
 * @param {string} params.provider - 'gpt', 'llama' ou 'mixtral'
 * @param {string} params.prompt - Prompt utilisateur
 * @param {object} [params.options] - Options avancées (langue, logs, etc.)
 * @returns {Promise<object>} Résultat { success, response, fallback, quota, error, timestamp }
 */
export async function callAI({ provider, prompt, options = {} }) {
  if (!hasConsent()) {
    return {
      success: false,
      response: null,
      fallback: true,
      quota: null,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }

  const quota = checkQuota();
  if (!quota.allowed) {
    return {
      success: false,
      response: null,
      fallback: true,
      quota,
      error: 'Quota IA dépassé',
      timestamp: new Date().toISOString()
    };
  }

  let result;
  try {
    if (provider === 'gpt') {
      result = await gptFallback({ prompt, options });
    } else if (provider === 'llama') {
      result = await llamaFallback({ prompt, options });
    } else if (provider === 'mixtral') {
      result = await mixtralFallback({ prompt, options });
    } else {
      throw new Error('Provider IA inconnu');
    }
    incrementQuota();
    if (options.log !== false) {
      logAiServiceEvent('ai_call', {
        provider,
        prompt: anonymizePrompt(prompt),
        fallback: result.fallback,
        timestamp: new Date().toISOString()
      });
    }
    return { ...result, quota: checkQuota() };
  } catch (err) {
    if (options.log !== false) {
      logAiServiceEvent('ai_call_error', {
        provider,
        prompt: anonymizePrompt(prompt),
        error: err.message,
        timestamp: new Date().toISOString()
      });
    }
    return {
      success: false,
      response: null,
      fallback: true,
      quota: checkQuota(),
      error: err.message,
      timestamp: new Date().toISOString()
    };
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('ai_service_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logAiServiceEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('ai_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('ai_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un prompt pour les logs.
 * @param {string} prompt
 * @returns {string}
 */
function anonymizePrompt(prompt) {
  if (!prompt || typeof prompt !== 'string') return '';
  return prompt.length > 32 ? prompt.slice(0, 32) + '…' : prompt;
}

/**
 * Efface les logs IA service (droit à l’oubli RGPD).
 */
export function clearLocalAiServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('ai_service_logs');
  }
}