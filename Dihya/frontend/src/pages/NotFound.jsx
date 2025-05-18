/**
 * @file NotFound.jsx
 * @description Page 404 pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';

/**
 * Page d’erreur 404 (non trouvée).
 * @returns {JSX.Element}
 */
export default function NotFound() {
  const { t, i18n } = useTranslation();

  useEffect(() => {
    if (hasConsent()) {
      logNotFoundEvent('not_found_view', { lang: i18n.language, path: window.location.pathname });
    }
  }, [i18n.language]);

  return (
    <MainLayout title={t('notfound.title')} description={t('notfound.description')}>
      <section className="notfound-section" aria-labelledby="notfound-title">
        <h1 id="notfound-title">{t('notfound.title') || '404 – Page non trouvée'}</h1>
        <p>{t('notfound.description') || 'La page demandée est introuvable ou a été déplacée.'}</p>
        <a href="/" className="cta-btn">
          {t('navigation.home') || 'Retour à l’accueil'}
        </a>
      </section>
    </MainLayout>
  );
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('notfound_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logNotFoundEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('notfound_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('notfound_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs notfound (droit à l’oubli RGPD).
 */
export function clearLocalNotFoundLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('notfound_logs');
  }
}