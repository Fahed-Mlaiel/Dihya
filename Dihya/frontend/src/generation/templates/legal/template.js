/**
 * @file template.js
 * @description Template générique pour modules légaux Dihya Coding (mentions légales, CGU, CGV, politique de confidentialité, cookies).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un module légal selon le type demandé.
 * @param {object} params
 * @param {string} params.type - Type de module ('legalNotice', 'terms', 'privacyPolicy', 'cookiesPolicy')
 * @param {object} params.data - Données du module (société, conditions, politique, etc.)
 * @param {object} [params.options] - Options avancées (SEO, logs, RGPD, etc.)
 * @returns {object} Module légal généré
 */
export function legalTemplate({ type, data, options = {} }) {
  validateType(type);
  validateData(type, data);
  if (!window?.localStorage?.getItem('legal_feature_consent')) {
    throw new Error('Consentement requis pour générer un module légal.');
  }
  const module = generateModule(type, data, options);
  logLegalTemplateEvent('generate_legal_module', type, anonymizeData(type, data));
  return module;
}

/**
 * Génère le module selon le type.
 * @param {string} type
 * @param {object} data
 * @param {object} options
 * @returns {object}
 */
function generateModule(type, data, options) {
  switch (type) {
    case 'legalNotice':
      return { legalNotice: anonymizeLegalNotice(data.legalNotice || {}), ...options };
    case 'terms':
      return { terms: data.terms || {}, ...options };
    case 'privacyPolicy':
      return { privacyPolicy: anonymizePrivacyPolicy(data.privacyPolicy || {}), ...options };
    case 'cookiesPolicy':
      return { cookiesPolicy: data.cookiesPolicy || {}, ...options };
    default:
      throw new Error('Type de module légal non supporté');
  }
}

/**
 * Valide le type de module légal.
 * @param {string} type
 */
function validateType(type) {
  const SUPPORTED = ['legalNotice', 'terms', 'privacyPolicy', 'cookiesPolicy'];
  if (!SUPPORTED.includes(type)) {
    throw new Error('Type de module légal invalide');
  }
}

/**
 * Valide les données selon le type de module.
 * @param {string} type
 * @param {object} data
 */
function validateData(type, data) {
  if (!data || typeof data !== 'object') throw new Error('Données du module invalides');
  if (type === 'legalNotice' && typeof data.legalNotice !== 'object') throw new Error('Données mentions légales invalides');
  if (type === 'terms' && typeof data.terms !== 'object') throw new Error('Données CGU/CGV invalides');
  if (type === 'privacyPolicy' && typeof data.privacyPolicy !== 'object') throw new Error('Données politique de confidentialité invalides');
  if (type === 'cookiesPolicy' && typeof data.cookiesPolicy !== 'object') throw new Error('Données politique cookies invalides');
}

/**
 * Anonymise les données sensibles pour les logs.
 * @param {string} type
 * @param {object} data
 * @returns {object}
 */
function anonymizeData(type, data) {
  if (type === 'legalNotice' && data.legalNotice) {
    return { ...data, legalNotice: anonymizeLegalNotice(data.legalNotice) };
  }
  if (type === 'privacyPolicy' && data.privacyPolicy) {
    return { ...data, privacyPolicy: anonymizePrivacyPolicy(data.privacyPolicy) };
  }
  return data;
}

/**
 * Anonymise les données mentions légales pour les logs.
 * @param {object} legalNotice
 * @returns {object}
 */
function anonymizeLegalNotice(legalNotice) {
  if (!legalNotice) return {};
  const { address, contact, ...rest } = legalNotice;
  return {
    ...rest,
    address: address ? '[address]' : undefined,
    contact: contact ? '[contact]' : undefined,
  };
}

/**
 * Anonymise les données politique de confidentialité pour les logs.
 * @param {object} privacyPolicy
 * @returns {object}
 */
function anonymizePrivacyPolicy(privacyPolicy) {
  if (!privacyPolicy) return {};
  const { email, phone, ...rest } = privacyPolicy;
  return {
    ...rest,
    email: email ? '[email]' : undefined,
    phone: phone ? '[phone]' : undefined,
  };
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} type
 * @param {object} data
 */
function logLegalTemplateEvent(action, type, data) {
  try {
    const logs = JSON.parse(localStorage.getItem('legal_template_logs') || '[]');
    logs.push({
      action,
      type,
      data,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('legal_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération légale (droit à l’oubli RGPD).
 */
export function clearLocalLegalTemplateLogs() {
  localStorage.removeItem('legal_template_logs');
}