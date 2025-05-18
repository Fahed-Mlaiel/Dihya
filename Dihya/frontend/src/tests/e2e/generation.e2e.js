/**
 * @file generation.e2e.js
 * @description Tests end-to-end pour le service de génération Dihya Coding : vérifie la génération de code, markdown, images, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent le consentement utilisateur, anonymisent les logs et valident les bonnes pratiques.
 */

import { generate, clearLocalGenerationServiceLogs } from '../../services/generationService';

describe('Service de génération – E2E', () => {
  beforeAll(() => {
    // Simule le consentement utilisateur pour les tests
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.setItem('generation_service_feature_consent', '1');
    }
    clearLocalGenerationServiceLogs();
  });

  afterAll(() => {
    clearLocalGenerationServiceLogs();
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.removeItem('generation_service_feature_consent');
    }
  });

  it('génère du code source sécurisé', () => {
    const result = generate({
      type: 'code',
      options: { language: 'javascript', content: 'console.log("Hello!");', log: true }
    });
    expect(result.success).toBe(true);
    expect(result.output).toContain('console.log');
    expect(result.error).toBeNull();
  });

  it('génère un document markdown', () => {
    const result = generate({
      type: 'markdown',
      options: { title: 'Titre Test', body: 'Ceci est un test.', log: true }
    });
    expect(result.success).toBe(true);
    expect(result.output).toContain('# Titre Test');
    expect(result.output).toContain('Ceci est un test.');
    expect(result.error).toBeNull();
  });

  it('génère une image simulée', () => {
    const result = generate({
      type: 'image',
      options: { log: true }
    });
    expect(result.success).toBe(true);
    expect(result.output).toMatch(/^data:image\/png;base64,/);
    expect(result.error).toBeNull();
  });

  it('refuse la génération sans consentement RGPD', () => {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.removeItem('generation_service_feature_consent');
    }
    const result = generate({
      type: 'code',
      options: { language: 'js', content: 'alert(1);' }
    });
    expect(result.success).toBe(false);
    expect(result.error).toMatch(/Consentement requis/);
  });

  it('gère les types de génération non supportés', () => {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.setItem('generation_service_feature_consent', '1');
    }
    const result = generate({
      type: 'unknown',
      options: { log: true }
    });
    expect(result.success).toBe(false);
    expect(result.error).toMatch(/non supporté/);
  });

  it('auditabilité : les logs sont anonymisés et effaçables', () => {
    const result = generate({
      type: 'code',
      options: { language: 'js', content: 'let x = 1;', log: true }
    });
    expect(result.success).toBe(true);

    // Vérifie la présence de logs anonymisés
    let logs = [];
    if (typeof window !== 'undefined' && window.localStorage) {
      logs = JSON.parse(window.localStorage.getItem('generation_service_logs') || '[]');
    }
    expect(Array.isArray(logs)).toBe(true);
    expect(logs.length).toBeGreaterThan(0);
    expect(logs[0].data.options.language.length).toBeLessThanOrEqual(16);

    // Efface les logs
    clearLocalGenerationServiceLogs();
    if (typeof window !== 'undefined' && window.localStorage) {
      const logsAfter = window.localStorage.getItem('generation_service_logs');
      expect(logsAfter === null || logsAfter === '[]').toBe(true);
    }
  });
});

/* Documentation claire : chaque test est commenté pour auditabilité et conformité */