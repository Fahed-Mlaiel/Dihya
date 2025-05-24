// Test Node.js/Jest pour valider l’import et l’accessibilité des icônes Dihya
const request = require('supertest');
const app = require('./serve_icons');
const fs = require('fs');
const path = require('path');

describe('Dihya Icons API', () => {
  const icons = [
    'admin','dihya-logo','lang-ar','lang-en','lang-fr','lang-tzr','plugin','security','template','user','audit','blockchain','cloud','finance','health','industry','rh','souverainete','test','theme','accessibility'
  ];

  icons.forEach(icon => {
    it(`GET /icons/${icon} should return SVG`, async () => {
      const res = await request(app).get(`/icons/${icon}`);
      expect(res.statusCode).toBe(200);
      expect(res.headers['content-type']).toMatch(/svg/);
      expect(res.text).toMatch(/<svg/);
      // Vérifie la présence d’aria-label et role="img"
      expect(res.text).toMatch(/aria-label/);
      expect(res.text).toMatch(/role="img"/);
    });
  });

  it('GET /icons/unknown should return 404', async () => {
    const res = await request(app).get('/icons/unknown');
    expect(res.statusCode).toBe(404);
  });
});
