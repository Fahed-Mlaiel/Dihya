/**
 * Point d'entrée du backend Node.js pour Dihya Coding.
 * Respecte le cahier des charges : sécurité, modularité, bonnes pratiques, API RESTful.
 */

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const morgan = require('morgan');
require('dotenv').config();

const app = express();

// Middlewares globaux
app.use(express.json());
app.use(cors({ origin: '*' }));
app.use(helmet());
app.use(morgan('dev'));

// Rate limiting (anti-DDoS)
const limiter = rateLimit({
  windowMs: 1 * 60 * 1000, // 1 minute
  max: 100, // max 100 requêtes/minute/IP
});
app.use('/api/', limiter);

// Routes principales (à compléter dans /routes)
app.get('/', (req, res) => {
  res.json({
    message: "Bienvenue sur l'API Node.js de Dihya Coding.",
    version: "1.0.0",
    documentation: "/api/docs"
  });
});

// Healthcheck
app.get('/api/health', (req, res) => {
  res.json({ status: "ok", message: "Dihya Node API opérationnelle" });
});

// Importer et utiliser les routes modulaires
// Exemple :
// const authRoutes = require('./routes/auth');
// app.use('/api/auth', authRoutes);

// Gestion des erreurs globales
app.use((req, res) => {
  res.status(404).json({ error: "Ressource non trouvée" });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: "Erreur interne du serveur" });
});

// Lancement du serveur
const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
  console.log(`Dihya Node.js API lancée sur le port ${PORT}`);
});