# Backend Flask – Dihya Coding

Ce dossier contient le backend de l’application Dihya Coding, basé sur Flask.  
Il respecte le cahier des charges : sécurité, modularité, multilingue, extensibilité, bonnes pratiques et tests.

---

## Fonctionnalités principales

- **API RESTful** (Flask)
- Authentification JWT (connexion, inscription, refresh, logout)
- Gestion des utilisateurs (CRUD, rôles, profil)
- Sécurité avancée (CORS, headers, validation, rate limiting)
- Mailing transactionnel (Flask-Mail)
- Internationalisation (Flask-Babel, multilingue/dialectes)
- SEO (robots.txt, sitemap.xml, meta tags)
- Tests unitaires (Pytest/Unittest)
- Configuration par environnement (.env)
- Extensible (services, blueprints, utils, schemas)

---

## Structure des dossiers

```
flask/
├── .env
├── README.md
├── requirements.txt
├── run.py
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── auth.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── user_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   ├── validators.py
│   │   ├── mailing.py
│   │   ├── i18n.py
│   │   └── seo.py
│   ├── schemas/
│   │   └── __init__.py
├── config/
│   └── __init__.py
└── tests/
    ├── test_auth.py
    └── test_user.py
```

---

## Lancement local

1. **Installer les dépendances**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurer l’environnement**  
   Copier `.env` et adapter les variables si besoin.

3. **Lancer le serveur**  
   ```bash
   python run.py
   ```

---

## Bonnes pratiques & sécurité

- CORS activé sur `/api/*`
- Headers de sécurité HTTP ajoutés à chaque réponse
- Validation stricte des entrées (utils/validators.py)
- Authentification JWT (tokens courts, refresh)
- Rôles utilisateurs (admin, user, invité)
- Rate limiting simple (utils/security.py)
- Tests unitaires obligatoires pour chaque route critique

---

## Internationalisation

- Multilingue via Flask-Babel
- Prise en charge des dialectes (voir config et utils/i18n.py)
- Traductions à compléter dans le dossier `i18n/` à la racine du projet

---

## SEO

- robots.txt et sitemap.xml servis automatiquement
- Génération de meta tags dynamique (utils/seo.py)

---

## Tests

- Lancer tous les tests :
  ```bash
  python -m unittest discover tests
  ```

---

## Extensibilité

- Ajouter vos propres services dans `app/services/`
- Ajouter des schémas Marshmallow/Pydantic dans `app/schemas/`
- Ajouter des blueprints pour de nouveaux modules dans `app/routes/`

---

## Licence

Projet open-source sous licence AGPL.  
Voir le fichier `LICENSE` à la racine du projet.

---