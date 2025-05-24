// CLI Node.js – Onboarding utilisateur
const axios = require('axios');
const argv = require('yargs').option('email', { demandOption: true, type: 'string' }).option('lang', { default: 'fr', type: 'string' }).argv;
axios.post('http://localhost:8002/api/onboarding/', { email: argv.email, lang: argv.lang })
  .then(res => console.log(res.data))
  .catch(err => console.error(err.response?.data || err.message));
