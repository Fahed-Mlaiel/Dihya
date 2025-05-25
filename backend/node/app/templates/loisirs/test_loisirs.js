/**
 * Tests unitaires et d’intégration pour le module loisirs.
 * @module test_loisirs
 * @author Dihya Team
 */

const { generateLoisirsPolicy } = require('./template');

describe('Loisirs Policy Generator', () => {
  it('génère une politique loisirs pour admin', () => {
    const policy = generateLoisirsPolicy({ lang: 'fr', role: 'admin', data: { project: 'Test' } });
    expect(policy).toContain('admin');
    expect(policy).toContain('Test');
  });

  it('refuse un rôle non autorisé', () => {
    expect(() => generateLoisirsPolicy({ lang: 'fr', role: 'hacker' })).toThrow();
  });

  it('génère une politique loisirs multilingue', () => {
    const policyEn = generateLoisirsPolicy({ lang: 'en', role: 'user', data: { project: 'Demo' } });
    expect(policyEn).toContain('user');
    expect(policyEn).toContain('Demo');
  });
});
