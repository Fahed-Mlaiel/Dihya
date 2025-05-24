const plugin = require('../plugin');
describe('Generic Plugin', () => {
  it('should initialize and run', () => {
    const context = { log: jest.fn() };
    const p = plugin({});
    const res = p.run({ lang: 'fr' }, context);
    expect(res.success).toBe(true);
    expect(typeof res.message).toBe('string');
    expect(context.log).toHaveBeenCalled();
  });
  it('should support all languages', () => {
    const p = plugin({});
    ['fr', 'en', 'ar', 'tzr'].forEach(lang => {
      const res = p.run({ lang });
      expect(res.success).toBe(true);
    });
  });
});
