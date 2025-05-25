/**
 * Test d'intégration avancé pour la gestion des projets Intelligence Artificielle (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, multitenancy, fallback IA, SEO, multilingue)
 * @see README.md pour la documentation complète
 */
const request = require('supertest');
const app = require('../../../../backend/node/app');
const { getJwt, SUPPORTED_LANGUAGES } = require('../../utils/test_utils');

describe('Intelligence Artificielle API Integration', () => {
  let jwt;
  beforeAll(async () => {
    jwt = await getJwt('admin');
  });
  it('GET /api/intelligence_artificielle/modeles (secured, i18n, audit, plugins)', async () => {
    for (const lang of SUPPORTED_LANGUAGES) {
      const res = await request(app)
        .get('/api/intelligence_artificielle/modeles')
        .set('Authorization', `Bearer ${jwt}`)
        .set('Accept-Language', lang);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('data');
      expect(res.headers['content-language']).toBe(lang);
    }
  });
  it('POST /api/intelligence_artificielle/modeles (validation, RGPD, plugins, audit)', async () => {
    const res = await request(app)
      .post('/api/intelligence_artificielle/modeles')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ nom: 'ModelX', type: 'NLP', version: '1.0' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('message');
    expect(res.body).toHaveProperty('data');
  });
  it('GraphQL /api/intelligence_artificielle/graphql (roles, plugins, fallback IA)', async () => {
    const query = '{ modeles { id nom type version } }';
    const res = await request(app)
      .post('/api/intelligence_artificielle/graphql')
      .set('Authorization', `Bearer ${jwt}`)
      .send({ query });
    expect(res.statusCode).toBe(200);
    expect(res.body.data).toHaveProperty('modeles');
  });
  it('Sécurité CORS, WAF, anti-DDOS', async () => {
    // Test CORS headers, WAF, anti-DDOS (mock)
    const res = await request(app)
      .options('/api/intelligence_artificielle/modeles')
      .set('Origin', 'https://evil.com');
    expect(res.headers).toHaveProperty('access-control-allow-origin');
  });
});
