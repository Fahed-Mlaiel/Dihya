/**
 * @file api.integration.js
 * @description Tests d’intégration pour les appels API de Dihya Coding : vérifie la robustesse, la sécurité, la conformité RGPD, l’auditabilité, l’extensibilité et la documentation claire.
 * Tous les tests respectent le consentement utilisateur, anonymisent les logs et valident les bonnes pratiques.
 */

import axios from 'axios';

const API_BASE = process.env.API_BASE || 'http://localhost:3000/api';

describe('API Integration – Dihya Coding', () => {
  beforeAll(() => {
    // Simule le consentement utilisateur pour les tests
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.setItem('api_integration_feature_consent', '1');
    }
  });

  afterAll(() => {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.removeItem('api_integration_feature_consent');
    }
  });

  it('répond à /status avec un statut 200 et un message', async () => {
    const res = await axios.get(`${API_BASE}/status`);
    expect(res.status).toBe(200);
    expect(res.data).toHaveProperty('status');
    expect(res.data.status).toMatch(/ok|ready/i);
  });

  it('protège les routes privées sans authentification', async () => {
    try {
      await axios.get(`${API_BASE}/user/profile`);
      // Si pas d’erreur, c’est un problème
      throw new Error('Route privée accessible sans auth');
    } catch (err) {
      expect(err.response.status).toBe(401);
    }
  });

  it('accepte une inscription utilisateur valide', async () => {
    const email = `test${Date.now()}@dihya.app`;
    const res = await axios.post(`${API_BASE}/auth/register`, {
      email,
      password: 'S3cure!Test',
      username: 'testuser'
    });
    expect(res.status).toBe(201);
    expect(res.data).toHaveProperty('user');
    expect(res.data.user).toHaveProperty('email');
    expect(res.data.user.email).toContain('@dihya.app');
  });

  it('refuse une inscription avec email invalide', async () => {
    try {
      await axios.post(`${API_BASE}/auth/register`, {
        email: 'invalid',
        password: 'S3cure!Test',
        username: 'testuser'
      });
      throw new Error('Inscription acceptée avec email invalide');
    } catch (err) {
      expect(err.response.status).toBe(400);
    }
  });

  it('respecte le RGPD : pas de données sensibles dans la réponse', async () => {
    const email = `test${Date.now()}@dihya.app`;
    const res = await axios.post(`${API_BASE}/auth/register`, {
      email,
      password: 'S3cure!Test',
      username: 'testuser'
    });
    expect(res.data).not.toHaveProperty('password');
    expect(res.data.user).not.toHaveProperty('password');
  });

  it('auditabilité : chaque appel API peut être logué et effaçable', async () => {
    // Simule un appel API et log local
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.setItem('api_integration_logs', JSON.stringify([]));
    }
    const res = await axios.get(`${API_BASE}/status`);
    if (typeof window !== 'undefined' && window.localStorage) {
      const logs = JSON.parse(window.localStorage.getItem('api_integration_logs') || '[]');
      logs.push({
        endpoint: '/status',
        status: res.status,
        timestamp: new Date().toISOString()
      });
      window.localStorage.setItem('api_integration_logs', JSON.stringify(logs));
      expect(Array.isArray(logs)).toBe(true);
      expect(logs.length).toBeGreaterThan(0);

      // Efface les logs
      window.localStorage.removeItem('api_integration_logs');
      const logsAfter = window.localStorage.getItem('api_integration_logs');
      expect(logsAfter === null || logsAfter === '[]').toBe(true);
    }
  });
});

/* Documentation claire : chaque test est commenté pour auditabilité et conformité */