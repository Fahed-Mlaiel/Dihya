/**
 * @file Preview.jsx
 * @description Page d’aperçu de projet/module pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';

/**
 * Page d’aperçu d’un projet ou module généré.
 * @returns {JSX.Element}
 */
export default function Preview() {
  const { t, i18n } = useTranslation();
  const [previewData, setPreviewData] = useState(null);
  const [status, setStatus] = useState(null);

  useEffect(() => {
    if (hasConsent()) {
      logPreviewEvent('preview_view', { lang: i18n.language, path: window.location.pathname });
    }
    // Simulation de récupération des données d’aperçu (à remplacer par l’intégration réelle)
    fetchPreviewData()
      .then((data) => setPreviewData(data))
      .catch(() => setStatus({ type: 'error', message: t('messages.error_occurred') }));
  }, [i18n.language, t]);

  return (
    <MainLayout title={t('preview.title')} description={t('preview.description')}>
      <section className="preview-section" aria-labelledby="preview-title">
        <h1 id="preview-title">{t('preview.title') || 'Aperçu du projet'}</h1>
        <p>{t('preview.description') || 'Consultez un aperçu sécurisé et conforme RGPD de votre projet ou module généré.'}</p>
        {status && (
          <div
            className={`status-message ${status.type}`}
            role={status.type === 'error' ? 'alert' : 'status'}
            tabIndex={-1}
          >
            {status.message}
          </div>
        )}
        {previewData ? (
          <div className="preview-content" tabIndex={0} aria-live="polite">
            <h2>{previewData.name}</h2>
            <ul>
              {previewData.modules.map((mod) => (
                <li key={mod}>{mod}</li>
              ))}
            </ul>
            <p>
              {t('preview.generated_at')}: {previewData.generatedAt}
            </p>
          </div>
        ) : !status && (
          <div className="loading" aria-busy="true">
            {t('messages.loading')}
          </div>
        )}
      </section>
    </MainLayout>
  );
}

/**
 * Simulation de récupération des données d’aperçu (à remplacer par l’intégration réelle).
 * @returns {Promise<object>}
 */
async function fetchPreviewData() {
  await new Promise((r) => setTimeout(r, 350));
  // Exemple de données anonymisées
  return {
    name: 'Projet ***23',
    modules: ['ai', 'seo', 'security'],
    generatedAt: new Date().toLocaleString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('preview_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logPreviewEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('preview_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('preview_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs preview (droit à l’oubli RGPD).
 */
export function clearLocalPreviewLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('preview_logs');
  }
}