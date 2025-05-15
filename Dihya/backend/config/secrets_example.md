# secrets_example.md — Gestion sécurisée des secrets Dihya Coding

Ce fichier explique comment gérer les secrets et variables sensibles dans le backend Dihya Coding.

## Bonnes pratiques

- **Ne jamais stocker de secrets ou credentials dans le code source.**
- Utiliser des fichiers `.env` ou des variables d’environnement pour toutes les clés/API/passwords.
- Ajouter `.env` dans `.gitignore` pour éviter tout commit accidentel.
- Restreindre l’accès aux fichiers de secrets (`chmod 600 .env`).
- Documenter chaque variable attendue pour faciliter le déploiement.
- Utiliser des outils de gestion de secrets (Vault, Doppler, GitHub Secrets…) en production.
- Toujours changer les secrets par défaut avant la mise en production.

## Exemple de fichier `.env` (à placer dans `backend/flask/.env`)

```env
# Flask
SECRET_KEY=change_me_please
JWT_SECRET_KEY=change_me_too

# Database
DATABASE_URL=sqlite:///dihya.db

# Mail
SMTP_SERVER=smtp.mailgun.org
SMTP_PORT=587
SMTP_USER=postmaster@dihya.dev
SMTP_PASSWORD=supersecret
FROM_EMAIL=no-reply@dihya.dev

# OAuth2 / Social Auth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret

# IA / API externes
OPENAI_API_KEY=your_openai_key
MISTRAL_API_KEY=your_mistral_key

# Divers
SENDGRID_API_KEY=your_sendgrid_key
MAILGUN_API_KEY=your_mailgun_key
```

## Sécurité

- Toujours supprimer les fichiers `.env` avant de partager ou publier le code.
- Pour la CI/CD, utiliser les variables d’environnement du pipeline (GitHub Actions, GitLab CI…).
- Ne jamais afficher les valeurs de secrets dans les logs ou les erreurs.

---

**Équipe Dihya Coding**