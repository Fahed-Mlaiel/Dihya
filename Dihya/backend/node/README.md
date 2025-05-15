# Backend Node.js – Dihya Coding

Ce dossier contient le backend Node.js de l’application Dihya Coding.  
Il respecte le cahier des charges : sécurité, modularité, bonnes pratiques, API RESTful, extensibilité et tests.

---

## Fonctionnalités principales

- **API RESTful** (Express.js)
- Authentification JWT (connexion, inscription, refresh, logout)
- Gestion des utilisateurs (CRUD, rôles, profil)
- Sécurité avancée (CORS, Helmet, validation, rate limiting)
- Mailing transactionnel (nodemailer ou équivalent)
- Internationalisation (i18n, multilingue/dialectes)
- SEO (robots.txt, sitemap.xml, meta tags)
- Tests unitaires (Jest/Mocha)
- Configuration par environnement (.env)
- Extensible (routes, controllers, middleware, services)

---

## Structure des dossiers

```
node/
├── .env
├── README.md
├── package.json
├── src/
│   ├── index.js
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   └── routes/
└── tests/
```

---

## Lancement local

1. **Installer les dépendances**  
   ```bash
   npm install
   ```

2. **Configurer l’environnement**  
   Copier `.env` et adapter les variables si besoin.

3. **Lancer le serveur**  
   ```bash
   npm start
   ```
   ou  
   ```bash
   node src/index.js
   ```

---

## Bonnes pratiques & sécurité

- CORS activé sur `/api/*`
- Headers de sécurité HTTP via Helmet
- Validation stricte des entrées (middleware/validators)
- Authentification JWT (tokens courts, refresh)
- Rôles utilisateurs (admin, user, invité)
- Rate limiting (express-rate-limit)
- Tests unitaires obligatoires pour chaque route critique

---

## Internationalisation

- Multilingue via i18n
- Prise en charge des dialectes (voir config et middleware)
- Traductions à compléter dans le dossier `i18n/` à la racine du projet

---

## SEO

- robots.txt et sitemap.xml servis automatiquement
- Génération de meta tags dynamique (middleware/seo.js)

---

## Tests

- Lancer tous les tests :
  ```bash
  npm test
  ```

---

## Extensibilité

- Ajouter vos propres services dans `src/services/`
- Ajouter des middlewares personnalisés dans `src/middleware/`
- Ajouter des routes ou controllers pour de nouveaux modules dans `src/routes/` et `src/controllers/`

---

## Licence

Projet open-source sous licence AGPL.  
Voir le fichier `LICENSE` à la racine du projet.

---