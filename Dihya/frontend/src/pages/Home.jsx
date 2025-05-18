/**
 * @file Home.jsx
 * @description Page d’accueil de Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';

/**
 * Page d’accueil principale.
 * @returns {JSX.Element}
 */
export default function Home() {
  const { t, i18n } = useTranslation();

  useEffect(() => {
    if (hasConsent()) {
      logHomeEvent('home_view', { lang: i18n.language, path: window.location.pathname });
    }
  }, [i18n.language]);

  return (
    <MainLayout title={t('app.title')} description={t('app.description')}>
      <section className="home-section" aria-labelledby="home-title">
        <h1 id="home-title">{t('app.title')}</h1>
        <p>{t('app.description')}</p>
        <ul className="features-list">
          <li>{t('generation.start')}</li>
          <li>{t('security.security')}</li>
          <li>{t('rgpd.privacy_policy')}</li>
          <li>{t('docs.documentation')}</li>
        </ul>
        <a href="/generate" className="cta-btn">
          {t('generation.start')}
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
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('home_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logHomeEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('home_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('home_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs home (droit à l’oubli RGPD).
 */
export function clearLocalHomeLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('home_logs');
  }
}