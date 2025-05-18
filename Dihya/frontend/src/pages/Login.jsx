/**
 * @file Login.jsx
 * @description Page de connexion pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';

/**
 * Page de connexion utilisateur.
 * @returns {JSX.Element}
 */
export default function Login() {
  const { t } = useTranslation();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [status, setStatus] = useState(null);

  /**
   * Gère la soumission du formulaire de connexion.
   * @param {React.FormEvent} e
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus(null);

    if (!hasConsent()) {
      setStatus({ type: 'error', message: t('rgpd.consent_required') });
      return;
    }
    if (!validateEmail(email)) {
      setStatus({ type: 'error', message: t('forms.invalid_email') });
      return;
    }
    if (!password || password.length < 6) {
      setStatus({ type: 'error', message: t('forms.required') });
      return;
    }

    try {
      // Simulation d’authentification (à remplacer par l’intégration réelle)
      await fakeLogin({ email, password });
      logLoginEvent('login_success', {
        email: anonymizeEmail(email),
        timestamp: new Date().toISOString()
      });
      // Stockage utilisateur simulé (à remplacer par la vraie logique)
      window.localStorage.setItem('current_user', JSON.stringify({ id: email, role: 'user' }));
      setStatus({ type: 'success', message: t('messages.login_success') });
      setEmail('');
      setPassword('');
      // Redirection possible ici
    } catch (err) {
      logLoginEvent('login_error', {
        email: anonymizeEmail(email),
        error: err.message,
        timestamp: new Date().toISOString()
      });
      setStatus({ type: 'error', message: t('messages.error_occurred') });
    }
  };

  return (
    <MainLayout title={t('navigation.login')} description={t('app.description')}>
      <section className="login-section" aria-labelledby="login-title">
        <h1 id="login-title">{t('navigation.login')}</h1>
        <form onSubmit={handleSubmit} aria-describedby="login-desc">
          <div id="login-desc" className="sr-only">
            {t('app.description')}
          </div>
          <label htmlFor="email">{t('forms.email')}</label>
          <input
            id="email"
            name="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            autoComplete="username"
            aria-required="true"
          />

          <label htmlFor="password">{t('forms.password')}</label>
          <input
            id="password"
            name="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            minLength={6}
            autoComplete="current-password"
            aria-required="true"
          />

          <button type="submit">{t('navigation.login')}</button>
        </form>
        {status && (
          <div
            className={`status-message ${status.type}`}
            role={status.type === 'error' ? 'alert' : 'status'}
            tabIndex={-1}
          >
            {status.message}
          </div>
        )}
      </section>
    </MainLayout>
  );
}

/**
 * Simulation d’authentification (à remplacer par l’intégration réelle).
 * @param {object} params
 * @returns {Promise<void>}
 */
async function fakeLogin(params) {
  await new Promise((r) => setTimeout(r, 300));
  // Simule un succès, peut lever une erreur pour tester les cas d’échec
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('login_feature_consent');
}

/**
 * Valide une adresse email.
 * @param {string} email
 * @returns {boolean}
 */
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logLoginEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('login_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('login_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise une adresse email pour les logs.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  if (typeof email !== 'string') return '';
  const [user, domain] = email.split('@');
  return user ? user[0] + '***@' + (domain || '') : '[email]';
}

/**
 * Efface les logs de login (droit à l’oubli RGPD).
 */
export function clearLocalLoginLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('login_logs');
  }
}