// Backend Node.js – Onboarding utilisateur sécurisé, RGPD, audit, fallback
const express = require('express');
const app = express();
app.use(express.json());

app.post('/api/onboarding/', (req, res) => {
  const { email, lang = 'fr' } = req.body;
  if (!email) return res.status(400).json({ error: 'Email requis', lang });
  // RGPD: log anonymisé
  console.log(`[ONBOARDING] ${new Date().toISOString()} - ${email.slice(0,2)}***@*** - ${lang}`);
  // Fallback IA open source simulé
  if (process.env.FALLBACK_IA === '1') {
    return res.json({ message: 'Réponse fallback IA', lang, fallback: true });
  }
  res.json({ message: `Bienvenue ${email}!`, lang, fallback: false });
});

app.listen(8002, () => console.log('Node backend running on 8002'));
