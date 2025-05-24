const exampleTemplate = require('../example_template');
describe('Example Template', () => {
  const tpl = exampleTemplate();
  it('should run in all supported languages', () => {
    ['fr', 'en', 'ar', 'tzr'].forEach(lang => {
      const res = tpl.run({ lang });
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
