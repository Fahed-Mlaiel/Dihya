/**
 * @file App.js
 * @description Composant principal de Dihya Coding : gestion du routage, navigation, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect, useState } from 'react';

// Import des templates métiers (fonctions génératrices HTML)
import Ecommerce from './templates/ecommerce';
import Education from './templates/education';
import Social from './templates/social';

// Import des utilitaires RGPD, sécurité, logs
import { hasConsent, setConsent } from './utils/rgpd';
import { clearLocalDataPurgeLogs } from './utils/dataPurge';
import { clearLocalSecurityUtilsLogs } from './utils/security';

// Routage fallback simple (hash)
import { getCurrentRoute, onRouteChange, fallbackNavigate } from './utils/fallbackRouter';

/**
 * Composant principal de l’application Dihya Coding.
 * Gère la navigation, le consentement RGPD, l’auditabilité et le rendu des pages métiers.
 */
function App() {
  const [route, setRoute] = useState(getCurrentRoute());
  const [consent, setConsentState] = useState(hasConsent('app'));
  const [content, setContent] = useState(null);

  useEffect(() => {
    // Écoute les changements de route (fallback)
    onRouteChange(setRoute);
  }, []);

  useEffect(() => {
    // Vérifie le consentement RGPD au chargement
    setConsentState(hasConsent('app'));
  }, []);

  useEffect(() => {
    // Met à jour le contenu affiché selon la route
    if (!consent) {
      setContent(null);
      return;
    }
    switch (route) {
      case '/ecommerce':
        setContent(
          <div
            dangerouslySetInnerHTML={{
              __html: Ecommerce.generateProductPage({
                id: 'p1',
                name: 'T-shirt Dihya',
                description: 'T-shirt bio, moderne et confortable.',
                price: 29.99,
                image: '/img/tshirt.png'
              })
            }}
          />
        );
        break;
      case '/education':
        setContent(
          <div
            dangerouslySetInnerHTML={{
              __html: Education.generateCoursePage({
                id: 'c1',
                title: 'Introduction au RGPD',
                description: 'Comprendre la conformité RGPD en développement web.',
                modules: [],
                image: '/img/rgpd.png'
              })
            }}
          />
        );
        break;
      case '/social':
        setContent(
          <div
            dangerouslySetInnerHTML={{
              __html: Social.generateProfilePage({
                id: 'u1',
                username: 'dihya_user',
                bio: 'Développeur passionné par la conformité RGPD.',
                avatar: '/img/avatar.png',
                followers: 42
              })
            }}
          />
        );
        break;
      default:
        setContent(
          <section>
            <h1>Bienvenue sur Dihya Coding</h1>
            <p>Choisissez un module métier dans la navigation.</p>
          </section>
        );
    }
  }, [route, consent]);

  /**
   * Gère la demande de consentement RGPD utilisateur.
   */
  function handleConsent(val) {
    setConsent('app', val, { log: true });
    setConsentState(val);
  }

  /**
   * Purge tous les logs et données sensibles (droit à l’oubli RGPD).
   */
  function handlePurge() {
    // Purge les logs des templates métiers
    if (Ecommerce.clearLocalEcommerceTemplateLogs) Ecommerce.clearLocalEcommerceTemplateLogs();
    if (Education.clearLocalEducationTemplateLogs) Education.clearLocalEducationTemplateLogs();
    if (Social.clearLocalSocialTemplateLogs) Social.clearLocalSocialTemplateLogs();
    // Purge les logs utilitaires
    clearLocalDataPurgeLogs();
    clearLocalSecurityUtilsLogs();
    alert('Données locales purgées (RGPD).');
    setContent(
      <section>
        <h1>Bienvenue sur Dihya Coding</h1>
        <p>Choisissez un module métier dans la navigation.</p>
      </section>
    );
    fallbackNavigate('/');
  }

  return (
    <div className="app-root" role="main">
      <header>
        <nav aria-label="Navigation principale">
          <ul>
            <li><a href="#/" onClick={e => { e.preventDefault(); fallbackNavigate('/'); }}>Accueil</a></li>
            <li><a href="#/ecommerce" onClick={e => { e.preventDefault(); fallbackNavigate('/ecommerce'); }}>E-commerce</a></li>
            <li><a href="#/education" onClick={e => { e.preventDefault(); fallbackNavigate('/education'); }}>Éducation</a></li>
            <li><a href="#/social" onClick={e => { e.preventDefault(); fallbackNavigate('/social'); }}>Social</a></li>
          </ul>
        </nav>
      </header>

      {!consent && (
        <section className="consent-banner" aria-label="Consentement RGPD">
          <p>
            Ce site utilise des fonctionnalités nécessitant votre consentement RGPD pour l’auditabilité et la sécurité.
          </p>
          <button onClick={() => handleConsent(true)} data-testid="consent-accept">Accepter</button>
          <button onClick={() => handleConsent(false)} data-testid="consent-decline">Refuser</button>
        </section>
      )}

      {consent && (
        <section className="main-content">
          {content}
          <button onClick={handlePurge} className="purge-btn" aria-label="Purger les données locales">
            Purger mes données (RGPD)
          </button>
        </section>
      )}

      <footer>
        <small>
          &copy; {new Date().getFullYear()} Dihya Coding – Sécurité, conformité RGPD, auditabilité, extensibilité, robustesse.
        </small>
      </footer>
    </div>
  );
}

export default App;

/* Documentation claire : chaque fonction et composant est commenté pour auditabilité et conformité */