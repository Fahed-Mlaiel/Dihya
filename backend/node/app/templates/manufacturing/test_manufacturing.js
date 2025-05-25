/**
 * Tests unitaires et d’intégration pour le module manufacturing.
 * @module test_manufacturing
 * @author Dihya Team
 */

const { generateManufacturingPolicy } = require('./template');

describe('Manufacturing Policy Generator', () => {
  it('génère une politique manufacturing pour admin', () => {
    const policy = generateManufacturingPolicy({ lang: 'fr', role: 'admin', data: { project: 'Test' } });
    expect(policy).toContain('admin');
    expect(policy).toContain('Test');
  });

  it('refuse un rôle non autorisé', () => {
    expect(() => generateManufacturingPolicy({ lang: 'fr', role: 'hacker' })).toThrow();
  });

  it('génère une politique manufacturing multilingue', () => {
    const policyEn = generateManufacturingPolicy({ lang: 'en', role: 'user', data: { project: 'Demo' } });
    expect(policyEn).toContain('user');
    expect(policyEn).toContain('Demo');
  });
});
