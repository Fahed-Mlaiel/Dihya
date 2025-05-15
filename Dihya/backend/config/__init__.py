"""
Configuration de l'application Flask pour Dihya Coding.
Inclut les paramètres de sécurité, mail, JWT, Babel, et autres options globales.
"""

import os

class Config:
    """Configuration de base pour Dihya Coding."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = os.environ.get("DEBUG", "False") == "True"
    TESTING = os.environ.get("TESTING", "False") == "True"

    # Flask-Mail
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.example.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "True") == "True"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", "noreply@dihya.coding")

    # JWT
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600))  # 1h

    # Babel (i18n)
    LANGUAGES = ["fr", "en", "ar", "ber", "tzm"]
    BABEL_DEFAULT_LOCALE = os.environ.get("BABEL_DEFAULT_LOCALE", "fr")
    BABEL_DEFAULT_TIMEZONE = os.environ.get("BABEL_DEFAULT_TIMEZONE", "Europe/Paris")

    # Sécurité
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True

    # SEO
    BASE_URL = os.environ.get("BASE_URL", "http://localhost:5000")

# Pour d'autres environnements, héritez de Config (ex: ProductionConfig, TestingConfig)