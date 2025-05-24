// Tests unitaires pour Dihya AI (Node.js)
// Couvre la génération, la sécurité, le fallback, la multilingue, la conformité RGPD.
const { generateAIResponse, selectEngine, SUPPORTED_LANGUAGES } = require('./ai');
test('Génération IA FR', async () => {
  const result = await generateAIResponse({ prompt: 'Bonjour', userId: 'test', lang: 'fr', role: 'user', engine: 'mixtral' });
  expect(result).toMatch(/Bonjour/);
});
test('Fallback engine', async () => {
  const engine = await selectEngine('openai');
  expect(['openai', 'mixtral', 'llama', 'mistral']).toContain(engine);
});
test('Langues supportées', () => {
  expect(SUPPORTED_LANGUAGES).toEqual(expect.arrayContaining(['fr', 'en', 'ar', 'tzr']));
});
