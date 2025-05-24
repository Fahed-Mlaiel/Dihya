# Dihya Logos – Exemples Node.js/Express

```js
const express = require('express');
const path = require('path');
const app = express();

app.get('/logos/:logo', (req, res) => {
  const logo = req.params.logo.replace(/[^a-zA-Z0-9\-_]/g, '');
  const logoPath = path.join(__dirname, logo + '.svg');
  res.setHeader('Content-Type', 'image/svg+xml');
  res.sendFile(logoPath);
});

app.listen(4000, () => console.log('Serveur logos Dihya sur 4000'));
```
