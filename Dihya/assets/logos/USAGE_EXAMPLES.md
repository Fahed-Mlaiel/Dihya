# Dihya Logos – Exemples d’intégration

## Frontend (React)
```jsx
import { Logos } from './index';
<Logos.main aria-label="Logo Dihya" role="img" />
```

## Backend (Django)
```python
from Dihya.assets.logos.meta_logos import get_logo_path
path = get_logo_path('dihya-main')
```

## Node.js/Express
```js
const express = require('express');
const path = require('path');
const app = express();
app.get('/logos/:logo', (req, res) => {
  const logo = req.params.logo.replace(/[^a-zA-Z0-9\-_]/g, '');
  const logoPath = path.join(__dirname, logo + '.svg');
  res.sendFile(logoPath);
});
```

## Plugins
- Ajoutez vos scripts dans le dossier, ils seront détectés automatiquement.

---

**Projet Dihya – Souveraineté numérique, sécurité, accessibilité, multilingue, auditabilité, production-ready.**
