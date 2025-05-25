// Exemple de firewall/WAF Node.js ultra avancé pour Dihya
const express = require('express');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const app = express();

app.use(helmet());
app.use(cors({ origin: ['https://dihya.app', 'http://localhost:3000'], credentials: true }));
app.use(express.json());

// Rate limiting/anti-DDOS
const limiter = rateLimit({ windowMs: 60 * 1000, max: 100 });
app.use(limiter);

// Audit/logs structurés
app.use((req, res, next) => {
  console.log(JSON.stringify({
    time: new Date().toISOString(),
    method: req.method,
    url: req.url,
    user: req.user ? req.user.id : null
  }));
  next();
});

// JWT auth middleware
app.use((req, res, next) => {
  const auth = req.headers['authorization'];
  if (auth && auth.startsWith('Bearer ')) {
    try {
      req.user = jwt.verify(auth.slice(7), process.env.JWT_SECRET || 'dev');
    } catch (e) {
      return res.status(401).json({ error: 'Invalid token' });
    }
  }
  next();
});

// Plugins sécurité dynamiques (exemple)
const plugins = {};
function registerPlugin(name, fn) { plugins[name] = fn; }
function getPlugin(name) { return plugins[name]; }
registerPlugin('audit', (req) => console.log('Audit plugin', req.url));

// RGPD export/anonymisation (exemple)
app.get('/export', (req, res) => {
  res.json({ logs: 'Exported logs (anonymized)' });
});

app.listen(4000, () => console.log('Firewall/WAF Dihya running on 4000'));
