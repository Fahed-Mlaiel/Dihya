const threeDTemplate = require('../3d_template');
describe('3D Template', () => {
  const tpl = threeDTemplate();
  it('should render in all supported languages', () => {
    ['fr', 'en', 'ar', 'tzr'].forEach(lang => {
      const res = tpl.render({}, { lang });
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
