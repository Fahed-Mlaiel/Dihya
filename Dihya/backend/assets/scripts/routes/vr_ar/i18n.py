"""
Dihya Backend – Internationalisation dynamique (i18n)
Support multilingue (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
"""
from django.utils import translation

SUPPORTED_LANGUAGES = [
    'fr', 'en', 'ar', 'kab', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'
]

def set_language(request):
    lang = request.GET.get('lang') or request.headers.get('Accept-Language', 'fr')[:2]
    if lang not in SUPPORTED_LANGUAGES:
        lang = 'fr'
    translation.activate(lang)
