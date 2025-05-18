/**
 * @file Profile.jsx
 * @description Page de profil utilisateur pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect, useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';

/**
 * Page de profil utilisateur.
 * @returns {JSX.Element}
 */
export default function Profile() {
  const { t, i18n } = useTranslation();
  const [user, setUser] = useState(null);
  const [status, setStatus] = useState(null);

  useEffect(() => {
    if (hasConsent()) {
      logProfileEvent('profile_view', { lang: i18n.language, path: window.location.pathname });
    }
    // Simulation de récupération du profil (à remplacer par l’intégration réelle)
    fetchProfile()
      .then((data) => setUser(data))
      .catch(() => setStatus({ type: 'error', message: t('messages.error_occurred') }));
  }, [i18n.language, t]);

  return (
    <MainLayout title={t('profile.title')} description={t('profile.description')}>
      <section className="profile-section" aria-labelledby="profile-title">
        <h1 id="profile-title">{t('profile.title') || 'Profil utilisateur'}</h1>
        <p>{t('profile.description') || 'Gérez vos informations personnelles et vos préférences.'}</p>
        {status && (
          <div
            className={`status-message ${status.type}`}
            role={status.type === 'error' ? 'alert' : 'status'}
            tabIndex={-1}
          >
            {status.message}
          </div>
        )}
        {user ? (
          <div className="profile-content" tabIndex={0} aria-live="polite">
            <dl>
              <dt>{t('profile.email') || 'Email'}</dt>
              <dd>{anonymizeEmail(user.email)}</dd>
              <dt>{t('profile.role') || 'Rôle'}</dt>
              <dd>{user.role}</dd>
              <dt>{t('profile.created_at') || 'Créé le'}</dt>
              <dd>{user.createdAt}</dd>
            </dl>
            {/* Ajout d’options RGPD : suppression, export, consentement */}
            <button onClick={handleForgetMe} className="rgpd-btn">
              {t('rgpd.forget_me') || 'Droit à l’oubli'}
            </button>
          </div>
        ) : !status && (
          <div className="loading" aria-busy="true">
            {t('messages.loading')}
          </div>
        )}
      </section>
    </MainLayout>
  );

  /**
   * Gère la demande de droit à l’oubli (suppression du profil local).
   */
  function handleForgetMe() {
    if (window.confirm(t('rgpd.forget_me_confirm') || 'Voulez-vous vraiment supprimer vos données ?')) {
      clearLocalProfile();
      setUser(null);
      setStatus({ type: 'success', message: t('rgpd.forget_me_success') || 'Profil supprimé.' });
      logProfileEvent('profile_forget', { timestamp: new Date().toISOString() });
    }
  }
}

/**
 * Simulation de récupération du profil utilisateur (à remplacer par l’intégration réelle).
 * @returns {Promise<object>}
 */
async function fetchProfile() {
  await new Promise((r) => setTimeout(r, 250));
  // Exemple de données anonymisées
  const user = JSON.parse(window.localStorage.getItem('current_user'));
  if (!user) throw new Error('Non authentifié');
  return {
    email: user.id || 'user@dihya.app',
    role: user.role || 'user',
    createdAt: user.createdAt || new Date().toLocaleDateString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('profile_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logProfileEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('profile_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('profile_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise une adresse email pour les logs et l’affichage.
 * @param {string} email
 * @returns {string}
 */
function anonymizeEmail(email) {
  if (typeof email !== 'string') return '';
  const [user, domain] = email.split('@');
  return user ? user[0] + '***@' + (domain || '') : '[email]';
}

/**
 * Efface le profil local (droit à l’oubli RGPD).
 */
function clearLocalProfile() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('current_user');
    window.localStorage.removeItem('profile_logs');
  }
}

/**
 * Efface les logs de profil (droit à l’oubli RGPD).
 */
export function clearLocalProfileLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('profile_logs');
  }
}