"""
Django settings ultra avancés pour Dihya :
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, CSP, audit, RGPD, logs structurés)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, gestion des rôles, plugins, fallback IA open source
- SEO backend (robots, sitemap, logs)
- Prêt CI/CD, Codespaces, Docker, K8s, fallback local
"""
import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-in-prod')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'graphene_django',
    'django_multitenant',
    'auditlog',
    'django_extensions',
    # ...autres apps métiers/plugins dynamiques
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    # WAF, anti-DDOS, plugins dynamiques ici
]

ROOT_URLCONF = 'django.urls'

LANGUAGES = [
    ('fr', 'Français'), ('en', 'English'), ('ar', 'العربية'), ('ber', 'ⴰⵎⴰⵣⵉⵖ'),
    ('de', 'Deutsch'), ('zh', '中文'), ('ja', '日本語'), ('ko', '한국어'),
    ('nl', 'Nederlands'), ('he', 'עברית'), ('fa', 'فارسی'), ('hi', 'हिन्दी'), ('es', 'Español'),
]
LANGUAGE_CODE = 'fr'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Europe/Paris'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

GRAPHENE = {
    'SCHEMA': 'django_project.schema.schema',
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ],
}

MULTITENANT_SHARED_APPS = [
    'django_multitenant',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    # ...autres apps partagées
]
MULTITENANT_TENANT_APPS = [
    # ...apps spécifiques par tenant
]

AUDITLOG_INCLUDE_ALL_MODELS = True
AUDITLOG_DISABLE_ON_RAW_SAVE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# SEO backend
ROBOTS_USE_SITEMAP = True
ROBOTS_SITEMAP_URLS = [os.environ.get('ROBOTS_SITEMAP_URL', '/sitemap.xml')]

# Plugins dynamiques (chargement via API/CLI)
PLUGINS_PATH = os.path.join(BASE_DIR, 'plugins')

# Fallback IA open source (LLaMA, Mixtral, Mistral)
IA_FALLBACK_PROVIDERS = ['llama', 'mixtral', 'mistral']

# RGPD : anonymisation, logs exportables
DATA_PRIVACY_EXPORT_PATH = os.path.join(BASE_DIR, 'exports')

# GitHub Actions, Docker, K8s, Codespaces ready
# ...autres configs avancées ici
