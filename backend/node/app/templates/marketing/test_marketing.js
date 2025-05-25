/**
 * Tests unitaires et d’intégration pour le module marketing.
 * @module test_marketing
 * @author Dihya Team
 */

const { generateMarketingPolicy } = require('./template');

describe('Marketing Policy Generator', () => {
  it('génère une politique marketing pour admin', () => {
    const policy = generateMarketingPolicy({ lang: 'fr', role: 'admin', data: { project: 'Test' } });
    expect(policy).toContain('admin');
    expect(policy).toContain('Test');
  });

  it('refuse un rôle non autorisé', () => {
    expect(() => generateMarketingPolicy({ lang: 'fr', role: 'hacker' })).toThrow();
  });

  it('génère une politique marketing multilingue', () => {
    const policyEn = generateMarketingPolicy({ lang: 'en', role: 'user', data: { project: 'Demo' } });
    expect(policyEn).toContain('user');
    expect(policyEn).toContain('Demo');
  });
});
