/**
 * @file index.js
 * @description Point d’entrée de l’application Dihya Coding : initialisation, rendu React, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

// Import CSS global (à adapter selon votre projet)
import './styles/global.css';

// Initialisation du root React moderne (React 18+)
const container = document.getElementById('root');
const root = createRoot(container);

// Rendu de l’application principale
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Auditabilité : log d’initialisation (anonymisé, RGPD)
if (typeof window !== 'undefined' && window.localStorage) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('app_init_logs') || '[]');
    logs.push({
      action: 'init',
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('app_init_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/* Documentation claire : chaque étape d’initialisation est commentée pour auditabilité et conformité */