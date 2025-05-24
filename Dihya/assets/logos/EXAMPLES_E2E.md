# Dihya Logos – Exemples E2E

## Test E2E Node.js (Jest + supertest)
```js
const request = require('supertest');
const app = require('./serve_logos');
describe('GET /logos/:logo', () => {
  it('doit retourner un SVG accessible', async () => {
    const res = await request(app).get('/logos/dihya-main');
    expect(res.statusCode).toBe(200);
    expect(res.headers['content-type']).toMatch(/svg/);
    expect(res.text).toMatch(/aria-label/);
    expect(res.text).toMatch(/role="img"/);
  });
});
```
