const vrArTemplate = require('../vr_ar_template');
describe('VR/AR Template', () => {
  const tpl = vrArTemplate();
  it('should launch experience in all supported languages', () => {
    ['fr', 'en', 'ar', 'tzr'].forEach(lang => {
      const res = tpl.launchExperience({ lang });
      expect(res.success).toBe(true);
      expect(typeof res.message).toBe('string');
    });
  });
  it('should log on init', () => {
    const context = { log: jest.fn() };
    tpl.onInit(context);
    expect(context.log).toHaveBeenCalled();
  });
});
