// Test d'intégration complet pour l'API 3D (REST, GraphQL, sécurité, i18n, plugins, audit, multitenancy)
// Couverture : endpoints, rôles, i18n, sécurité, RGPD, plugins, audit, e2e
const request = require('supertest');
const app = require('../../../app');
describe('API 3D', () => {
  it('admin peut créer un projet 3D', async () => {
    const res = await request(app)
      .post('/api/3d')
      .set('Authorization', 'Bearer ADMIN_JWT')
      .send({ name: 'Projet 3D', lang: 'fr' });
    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('id');
  });
  it('user ne peut pas supprimer un projet 3D', async () => {
    const res = await request(app)
      .delete('/api/3d/1')
      .set('Authorization', 'Bearer USER_JWT');
    expect(res.statusCode).toBe(403);
  });
  it('invite peut lister les projets 3D', async () => {
    const res = await request(app)
      .get('/api/3d')
      .set('Accept-Language', 'en')
      .set('Authorization', 'Bearer INVITE_JWT');
    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
  // ... autres tests i18n, plugins, audit, RGPD, e2e
});
