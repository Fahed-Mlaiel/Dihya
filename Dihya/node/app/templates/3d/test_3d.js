// test_3d.js - Tests unitaires et intégration pour Dihya 3D Template
const { init3DScene, addObject3D } = require('./template.js');
const jwt = require('jsonwebtoken');

describe('Dihya 3D Template', () => {
  const secret = 'dihya_secret';
  const userToken = jwt.sign({ id: 'u1', roles: ['user'] }, secret);
  const adminToken = jwt.sign({ id: 'a1', roles: ['admin'] }, secret);

  it('init3DScene crée une scène avec la bonne langue', () => {
    const scene = init3DScene({ lang: 'en', user: 'u1' });
    expect(scene.lang).toBe('en');
    expect(scene.objects).toEqual([]);
  });

  it('addObject3D autorise admin/user et refuse invité', () => {
    let scene = init3DScene({ user: 'a1' });
    expect(addObject3D(scene, { type: 'cube', params: {} }, adminToken)).toBe(true);
    scene = init3DScene({ user: 'u1' });
    expect(addObject3D(scene, { type: 'sphere', params: {} }, userToken)).toBe(true);
    const guestToken = jwt.sign({ id: 'g1', roles: ['guest'] }, secret);
    expect(addObject3D(scene, { type: 'cube', params: {} }, guestToken)).toBe(false);
  });

  it('addObject3D refuse type non supporté', () => {
    const scene = init3DScene({ user: 'a1' });
    expect(addObject3D(scene, { type: 'pyramid', params: {} }, adminToken)).toBe(false);
  });
});
