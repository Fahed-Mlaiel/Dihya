/**
 * Tests unitaires et d’intégration pour le module logistique.
 * @module test_logistique
 * @author Dihya Team
 */

const { generateLogistiquePolicy } = require('./template');

describe('Logistique Policy Generator', () => {
  it('génère une politique logistique pour admin', () => {
    const policy = generateLogistiquePolicy({ lang: 'fr', role: 'admin', data: { project: 'Test' } });
    expect(policy).toContain('admin');
    expect(policy).toContain('Test');
  });

  it('refuse un rôle non autorisé', () => {
    expect(() => generateLogistiquePolicy({ lang: 'fr', role: 'hacker' })).toThrow();
  });

  it('génère une politique logistique multilingue', () => {
    const policyEn = generateLogistiquePolicy({ lang: 'en', role: 'user', data: { project: 'Demo' } });
    expect(policyEn).toContain('user');
    expect(policyEn).toContain('Demo');
  });
});
