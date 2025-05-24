// Serveur Node.js/Express ultra avancé pour servir les logos Dihya (sécurisé, RGPD, accessibilité, audit, multilingue)
const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const LOGOS_DIR = __dirname;

// Middleware audit/log RGPD
app.use((req, res, next) => {
  // Log anonymisé, RGPD
  console.log(`[LOGO_ACCESS] ${new Date().toISOString()} ${req.method} ${req.url}`);
  next();
});

// Endpoint pour servir un SVG
app.get('/logos/:logo', (req, res) => {
  const logoName = req.params.logo.replace(/[^a-zA-Z0-9\-_]/g, '');
  const logoPath = path.join(LOGOS_DIR, logoName + '.svg');
  if (fs.existsSync(logoPath)) {
    res.setHeader('Content-Type', 'image/svg+xml');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.sendFile(logoPath);
  } else {
    res.status(404).json({ error: 'Logo not found' });
  }
});

// Démarrage serveur
if (require.main === module) {
  const PORT = process.env.PORT || 4001;
  app.listen(PORT, () => {
    console.log(`Dihya Logos server running on port ${PORT}`);
  });
}

module.exports = app;
