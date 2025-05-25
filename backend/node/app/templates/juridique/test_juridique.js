/**
 * Tests unitaires et d’intégration pour le module juridique.
 * @module test_juridique
 * @author Dihya Team
 */

const { generatePolicy } = require('./template');

describe('Juridique Policy Generator', () => {
  it('génère une politique en français pour admin', () => {
    const policy = generatePolicy({ lang: 'fr', role: 'admin', data: { project: 'Test' } });
    expect(policy).toContain('admin');
    expect(policy).toContain('Test');
  });

  it('refuse un rôle non autorisé', () => {
    expect(() => generatePolicy({ lang: 'fr', role: 'hacker' })).toThrow();
  });

  it('génère une politique multilingue', () => {
    const policyEn = generatePolicy({ lang: 'en', role: 'user', data: { project: 'Demo' } });
    expect(policyEn).toContain('user');
    expect(policyEn).toContain('Demo');
  });
});
