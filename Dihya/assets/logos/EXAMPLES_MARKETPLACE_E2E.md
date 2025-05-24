# Dihya Logos – Exemple test E2E marketplace

## Test E2E publication logo via API
```js
const request = require('supertest');
const app = require('./marketplace_api');
describe('Marketplace API', () => {
  it('publie un logo et le retrouve', async () => {
    await request(app)
      .post('/api/marketplace/logos')
      .send({ name: 'cloud', file: 'cloud.svg' })
      .expect(201);
    const res = await request(app).get('/api/marketplace/logos/cloud.svg');
    expect(res.statusCode).toBe(200);
    expect(res.text).toMatch(/<svg/);
  });
});
```
