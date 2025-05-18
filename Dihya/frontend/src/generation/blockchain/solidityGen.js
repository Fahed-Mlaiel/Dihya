/**
 * @file solidityGen.js
 * @description Générateur de smart contracts Solidity pour Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un smart contract Solidity à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.name - Nom du contrat (validé, anonymisé pour logs)
 * @param {string} params.type - Type de contrat (ex: 'ERC20', 'ERC721')
 * @param {object} [params.options] - Options avancées (supply, owner, symbol, etc.)
 * @returns {Promise<{success: boolean, contract: string, warnings?: string[]}>}
 */
export async function generateSolidityContract({ name, type, options = {} }) {
  validateContractName(name);
  validateContractType(type);
  if (!window?.localStorage?.getItem('blockchain_feature_consent')) {
    throw new Error('Consentement requis pour générer un smart contract.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/blockchain/solidity/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ name, type, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du smart contract');
  const data = await res.json();
  logSolidityGenEvent('generate_contract', anonymizeContractName(name), type);
  return data;
}

/**
 * Valide le nom du contrat.
 * @param {string} name
 */
function validateContractName(name) {
  if (!name || typeof name !== 'string' || name.length < 3 || name.length > 64) {
    throw new Error('Nom de contrat invalide');
  }
}

/**
 * Valide le type de contrat.
 * @param {string} type
 */
function validateContractType(type) {
  const SUPPORTED_TYPES = ['ERC20', 'ERC721', 'ERC1155', 'custom'];
  if (!SUPPORTED_TYPES.includes(type)) {
    throw new Error('Type de contrat non supporté');
  }
}

/**
 * Anonymise le nom du contrat pour les logs (pas de données personnelles).
 * @param {string} name
 * @returns {string}
 */
function anonymizeContractName(name) {
  return name.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [type]
 */
function logSolidityGenEvent(action, value, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('solidity_gen_logs') || '[]');
    logs.push({
      action,
      value,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('solidity_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération Solidity (droit à l’oubli RGPD).
 */
export function clearLocalSolidityGenLogs() {
  localStorage.removeItem('solidity_gen_logs');
}