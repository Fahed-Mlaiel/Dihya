// Test unitaire Node.js – Onboarding
const axios = require('axios');
(async () => {
  const res = await axios.post('http://localhost:8002/api/onboarding/', { email: 'test@dihya.com', lang: 'fr' });
  if (!res.data.message.includes('Bienvenue')) throw new Error('Pas de bienvenue');
  try {
    await axios.post('http://localhost:8002/api/onboarding/', { lang: 'fr' });
    throw new Error('Erreur RGPD non détectée');
  } catch(e) {
    if (!e.response.data.error.includes('Email')) throw e;
  }
  console.log('Tests onboarding Node.js OK');
})();
