// Test E2E Node.js/Jest + supertest pour l’API logos Dihya
const request = require('supertest');
const app = require('./serve_logos');

describe('Dihya Logos API', () => {
  const logos = [
    'dihya-main','dihya-amazigh','dihya-dark','dihya-light','dihya-minimal','brandmark','favicon','dihya-ar','dihya-en','dihya-fr','dihya-tzr','education','health','legal','blockchain','cloud','finance','industry','rh','souverainete','theme','test'
  ];

  logos.forEach(logo => {
    it(`GET /logos/${logo} should return SVG`, async () => {
      const res = await request(app).get(`/logos/${logo}`);
      expect(res.statusCode).toBe(200);
      expect(res.headers['content-type']).toMatch(/svg/);
      expect(res.text).toMatch(/<svg/);
      expect(res.text).toMatch(/aria-label/);
      expect(res.text).toMatch(/role="img"/);
    });
  });

  it('GET /logos/unknown should return 404', async () => {
    const res = await request(app).get('/logos/unknown');
    expect(res.statusCode).toBe(404);
  });
});
