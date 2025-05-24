const ecommerceTemplate = require('../ecommerce_template');
describe('E-commerce Template', () => {
  const tpl = ecommerceTemplate();
  it('should checkout in all supported languages', () => {
    ['fr', 'en', 'ar', 'tzr'].forEach(lang => {
      const res = tpl.checkout({}, { lang });
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
