/**
 * Tests unitaires et d’intégration pour le module médias.
 * @module test_medias
 * @author Dihya Team
 */

const { generateMediasPolicy } = require('./template');

describe('Medias Policy Generator', () => {
  it('génère une politique médias pour admin', () => {
    const policy = generateMediasPolicy({ lang: 'fr', role: 'admin', data: { project: 'Test' } });
    expect(policy).toContain('admin');
    expect(policy).toContain('Test');
  });

  it('refuse un rôle non autorisé', () => {
    expect(() => generateMediasPolicy({ lang: 'fr', role: 'hacker' })).toThrow();
  });

  it('génère une politique médias multilingue', () => {
    const policyEn = generateMediasPolicy({ lang: 'en', role: 'user', data: { project: 'Demo' } });
    expect(policyEn).toContain('user');
    expect(policyEn).toContain('Demo');
  });
});
