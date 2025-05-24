// Script Node.js/Express pour servir les icônes Dihya (sécurisé, RGPD, accessibilité)
const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const ICONS_DIR = path.join(__dirname);

// Middleware audit/log RGPD
app.use((req, res, next) => {
  // Log anonymisé, RGPD
  console.log(`[ICON_ACCESS] ${new Date().toISOString()} ${req.method} ${req.url}`);
  next();
});

// Endpoint pour servir un SVG
app.get('/icons/:icon', (req, res) => {
  const iconName = req.params.icon.replace(/[^a-zA-Z0-9\-_]/g, '');
  const iconPath = path.join(ICONS_DIR, iconName + '.svg');
  if (fs.existsSync(iconPath)) {
    res.setHeader('Content-Type', 'image/svg+xml');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.sendFile(iconPath);
  } else {
    res.status(404).json({ error: 'Icon not found' });
  }
});

// Démarrage serveur
if (require.main === module) {
  const PORT = process.env.PORT || 4000;
  app.listen(PORT, () => {
    console.log(`Dihya Icons server running on port ${PORT}`);
  });
}

module.exports = app;
