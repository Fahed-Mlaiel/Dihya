/**
 * @file App.js
 * @description Composant principal de Dihya Coding : gestion du routage, navigation, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Version finale conforme au cahier des charges : interface moderne, responsive, multilingue, extensible, souveraine.
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

// Import UI/UX (ex: Tailwind, Material UI, thème amazigh)
import './styles/main.css'; // Fichier CSS principal (responsive, thème, etc.)

/**
 * Composant principal de l’application Dihya Coding.
 * Gère la navigation, le consentement RGPD, l’auditabilité et le rendu des pages métiers.
 */
function App() {
  const [route, setRoute] = useState(getCurrentRoute());
  const [consent, setConsentState] = useState(hasConsent('app'));
  const [content, setContent] = useState(null);

  useEffect(() => {
    onRouteChange(setRoute);
  }, []);

  useEffect(() => {
    setConsentState(hasConsent('app'));
  }, []);

  useEffect(() => {
    if (!consent) {
      setContent(null);
      return;
    }
    switch (route) {
      case '/ecommerce':
        setContent(
          <div
            className="card"
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
            className="card"
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
            className="card"
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
      case '/generate':
        setContent(
          <section className="card">
            <h2>Générer un projet</h2>
            <p>
              Saisissez votre cahier des charges (texte ou vocal) pour générer un projet complet (frontend + backend).
            </p>
            {/* Zone de saisie texte/vocal, assistant IA, import/export */}
            <textarea className="input" placeholder="Décrivez votre projet..." rows={5} />
            <div className="actions">
              <button className="btn-primary">Générer</button>
              <button className="btn-secondary">Entrée vocale</button>
              <button className="btn-tertiary">Importer cahier des charges</button>
            </div>
            <small>Support multilingue, dialectes inclus.</small>
          </section>
        );
        break;
      case '/templates':
        setContent(
          <section className="card">
            <h2>Templates métiers</h2>
            <ul className="template-list">
              <li>Santé</li>
              <li>Juridique</li>
              <li>Immobilier</li>
              <li>Banque/Finance</li>
              <li>Assurance</li>
              <li>RH</li>
              <li>Industrie</li>
              <li>Logistique</li>
              <li>Transport</li>
              <li>Énergie</li>
              <li>Tourisme</li>
              <li>IT/DevOps</li>
              <li>Blockchain</li>
              <li>IA</li>
              <li>Recherche</li>
              <li>...etc.</li>
            </ul>
            <button className="btn-secondary">Importer/Exporter un template</button>
          </section>
        );
        break;
      case '/plugins':
        setContent(
          <section className="card">
            <h2>Marketplace de plugins</h2>
            <p>Ajoutez des fonctionnalités à votre projet (analytics, paiement, CMS, etc.).</p>
            <button className="btn-secondary">Découvrir les plugins</button>
          </section>
        );
        break;
      case '/demo':
        setContent(
          <section className="card">
            <h2>Démo instantanée</h2>
            <p>Testez votre projet généré en live, partagez le lien sans installation.</p>
            <button className="btn-primary">Voir la démo</button>
          </section>
        );
        break;
      case '/admin':
        setContent(
          <section className="card">
            <h2>Administration</h2>
            <p>Gestion des utilisateurs, templates, plugins, logs.</p>
            <button className="btn-secondary">Accéder à l’admin</button>
          </section>
        );
        break;
      default:
        setContent(
          <section className="hero">
            <img src="/img/dihya-logo.svg" alt="Logo Dihya Coding" className="logo" />
            <h1>Dihya Coding</h1>
            <p className="subtitle">
              De l’idée au code, en toute souveraineté.<br />
              Générateur No-Code/Low-Code multi-métiers, open-source, souverain, multilingue.
            </p>
            <div className="actions">
              <button className="btn-primary" onClick={() => fallbackNavigate('/generate')}>Générer un projet</button>
              <button className="btn-secondary" onClick={() => fallbackNavigate('/templates')}>Voir les templates</button>
              <button className="btn-tertiary" onClick={() => fallbackNavigate('/demo')}>Démo instantanée</button>
            </div>
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
    if (Ecommerce.clearLocalEcommerceTemplateLogs) Ecommerce.clearLocalEcommerceTemplateLogs();
    if (Education.clearLocalEducationTemplateLogs) Education.clearLocalEducationTemplateLogs();
    if (Social.clearLocalSocialTemplateLogs) Social.clearLocalSocialTemplateLogs();
    clearLocalDataPurgeLogs();
    clearLocalSecurityUtilsLogs();
    alert('Données locales purgées (RGPD).');
    setContent(
      <section className="hero">
        <img src="/img/dihya-logo.svg" alt="Logo Dihya Coding" className="logo" />
        <h1>Dihya Coding</h1>
        <p className="subtitle">
          De l’idée au code, en toute souveraineté.<br />
          Générateur No-Code/Low-Code multi-métiers, open-source, souverain, multilingue.
        </p>
        <div className="actions">
          <button className="btn-primary" onClick={() => fallbackNavigate('/generate')}>Générer un projet</button>
          <button className="btn-secondary" onClick={() => fallbackNavigate('/templates')}>Voir les templates</button>
          <button className="btn-tertiary" onClick={() => fallbackNavigate('/demo')}>Démo instantanée</button>
        </div>
      </section>
    );
    fallbackNavigate('/');
  }

  return (
    <div className="app-root" role="main">
      <header className="header">
        <nav aria-label="Navigation principale">
          <ul className="nav-list">
            <li><a href="#/" onClick={e => { e.preventDefault(); fallbackNavigate('/'); }}>Accueil</a></li>
            <li><a href="#/generate" onClick={e => { e.preventDefault(); fallbackNavigate('/generate'); }}>Générer</a></li>
            <li><a href="#/templates" onClick={e => { e.preventDefault(); fallbackNavigate('/templates'); }}>Templates</a></li>
            <li><a href="#/plugins" onClick={e => { e.preventDefault(); fallbackNavigate('/plugins'); }}>Plugins</a></li>
            <li><a href="#/demo" onClick={e => { e.preventDefault(); fallbackNavigate('/demo'); }}>Démo</a></li>
            <li><a href="#/admin" onClick={e => { e.preventDefault(); fallbackNavigate('/admin'); }}>Admin</a></li>
          </ul>
        </nav>
      </header>

      {!consent && (
        <section className="consent-banner" aria-label="Consentement RGPD">
          <p>
            Ce site utilise des fonctionnalités nécessitant votre consentement RGPD pour l’auditabilité et la sécurité.
          </p>
          <button onClick={() => handleConsent(true)} data-testid="consent-accept" className="btn-primary">Accepter</button>
          <button onClick={() => handleConsent(false)} data-testid="consent-decline" className="btn-secondary">Refuser</button>
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

      <footer className="footer">
        <small>
          &copy; {new Date().getFullYear()} Dihya Coding – Sécurité, conformité RGPD, auditabilité, extensibilité, robustesse.<br />
          <span className="footer-links">
            <a href="https://github.com/dihya-coding" target="_blank" rel="noopener noreferrer">GitHub</a> | 
            <a href="#/docs" onClick={e => { e.preventDefault(); fallbackNavigate('/docs'); }}>Documentation</a> | 
            <a href="#/contact" onClick={e => { e.preventDefault(); fallbackNavigate('/contact'); }}>Contact</a>
          </span>
        </small>
      </footer>
    </div>
  );
}

export default App;

/* Documentation claire : chaque fonction et composant est commenté pour auditabilité et conformité */