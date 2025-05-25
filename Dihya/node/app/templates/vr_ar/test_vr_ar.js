// test_vr_ar.js - Tests unitaires et intégration pour Dihya VR/AR Template
const { initVRARExperience, addEntityVRAR } = require('./template.js');
const jwt = require('jsonwebtoken');

describe('Dihya VR/AR Template', () => {
  const secret = 'dihya_secret';
  const userToken = jwt.sign({ id: 'u1', roles: ['user'] }, secret);
  const adminToken = jwt.sign({ id: 'a1', roles: ['admin'] }, secret);

  it('initVRARExperience crée une expérience avec la bonne langue', () => {
    const exp = initVRARExperience({ lang: 'ar', user: 'u1' });
    expect(exp.lang).toBe('ar');
    expect(exp.entities).toEqual([]);
  });

  it('addEntityVRAR autorise admin/user et refuse invité', () => {
    let exp = initVRARExperience({ user: 'a1' });
    expect(addEntityVRAR(exp, { type: 'avatar', params: {} }, adminToken)).toBe(true);
    exp = initVRARExperience({ user: 'u1' });
    expect(addEntityVRAR(exp, { type: 'object', params: {} }, userToken)).toBe(true);
    const guestToken = jwt.sign({ id: 'g1', roles: ['guest'] }, secret);
    expect(addEntityVRAR(exp, { type: 'avatar', params: {} }, guestToken)).toBe(false);
  });

  it('addEntityVRAR refuse type non supporté', () => {
    const exp = initVRARExperience({ user: 'a1' });
    expect(addEntityVRAR(exp, { type: 'alien', params: {} }, adminToken)).toBe(false);
  });
});
