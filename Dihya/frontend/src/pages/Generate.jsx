/**
 * @file Generate.jsx
 * @description Page de génération de projet/module pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import MainLayout from '../layout/MainLayout';

const MODULES = [
  { value: 'ai', label: 'IA' },
  { value: 'seo', label: 'SEO' },
  { value: 'ecommerce', label: 'E-commerce' },
  { value: 'security', label: 'Sécurité' },
  { value: 'blockchain', label: 'Blockchain' }
];

/**
 * Page de génération de projet/module.
 * @returns {JSX.Element}
 */
export default function Generate() {
  const { t } = useTranslation();
  const [projectName, setProjectName] = useState('');
  const [modules, setModules] = useState([]);
  const [status, setStatus] = useState(null);

  /**
   * Gère la soumission du formulaire de génération.
   * @param {React.FormEvent} e
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus(null);

    if (!hasConsent()) {
      setStatus({ type: 'error', message: t('rgpd.consent_required') });
      return;
    }
    if (!projectName.trim()) {
      setStatus({ type: 'error', message: t('forms.required') });
      return;
    }
    if (modules.length === 0) {
      setStatus({ type: 'error', message: t('forms.required') });
      return;
    }

    try {
      // Simulation de génération (à remplacer par l’intégration réelle)
      await fakeGenerateProject({ projectName, modules });
      logGenerationEvent('generate_project', {
        projectName: anonymizeProjectName(projectName),
        modules,
        timestamp: new Date().toISOString()
      });
      setStatus({ type: 'success', message: t('generation.generation_success') });
      setProjectName('');
      setModules([]);
    } catch (err) {
      setStatus({ type: 'error', message: t('messages.error_occurred') });
    }
  };

  /**
   * Gère la sélection des modules.
   * @param {React.ChangeEvent} e
   */
  const handleModuleChange = (e) => {
    const { value, checked } = e.target;
    setModules((prev) =>
      checked ? [...prev, value] : prev.filter((m) => m !== value)
    );
  };

  return (
    <MainLayout title={t('generation.start')} description={t('app.description')}>
      <section className="generate-section" aria-labelledby="generate-title">
        <h1 id="generate-title">{t('generation.start')}</h1>
        <form onSubmit={handleSubmit} aria-describedby="generate-desc">
          <div id="generate-desc" className="sr-only">
            {t('app.description')}
          </div>
          <label htmlFor="projectName">{t('generation.project_name')}</label>
          <input
            id="projectName"
            name="projectName"
            type="text"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            required
            minLength={3}
            maxLength={64}
            autoComplete="off"
            aria-required="true"
          />

          <fieldset>
            <legend>{t('generation.select_modules')}</legend>
            {MODULES.map((mod) => (
              <label key={mod.value}>
                <input
                  type="checkbox"
                  value={mod.value}
                  checked={modules.includes(mod.value)}
                  onChange={handleModuleChange}
                  aria-checked={modules.includes(mod.value)}
                />
                {mod.label}
              </label>
            ))}
          </fieldset>

          <button type="submit">{t('generation.start')}</button>
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
 * Simulation de génération de projet (à remplacer par l’intégration réelle).
 * @param {object} params
 * @returns {Promise<void>}
 */
async function fakeGenerateProject(params) {
  await new Promise((r) => setTimeout(r, 400));
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('generation_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logGenerationEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('generation_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('generation_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un nom de projet pour les logs.
 * @param {string} name
 * @returns {string}
 */
function anonymizeProjectName(name) {
  if (!name) return '';
  return name.length > 4 ? name.slice(0, 2) + '***' + name.slice(-2) : '***';
}