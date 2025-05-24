const stripePlugin = require('../stripe_plugin');
describe('Stripe Plugin', () => {
  it('should initialize and process payment', () => {
    const context = { log: jest.fn() };
    const plugin = stripePlugin({ apiKey: 'test' });
    const res = plugin.processPayment({ amount: 100, currency: 'EUR' }, context);
    expect(res.success).toBe(true);
    expect(typeof res.message).toBe('string');
    expect(context.log).toHaveBeenCalled();
  });
  it('should handle errors gracefully', () => {
    const plugin = stripePlugin({ apiKey: null });
    const context = { log: jest.fn() };
    const res = plugin.processPayment({ amount: 0 }, context);
    expect(res.success).toBe(false);
    expect(context.log).toHaveBeenCalled();
  });
});
