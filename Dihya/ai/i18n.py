"""
Internationalisation dynamique ultra avancée pour Dihya AI (Python)
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

AI_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'ai': 'Intelligence Artificielle', 'generate': 'Générer', 'error': 'Erreur', 'success': 'Succès'},
    'en': {'ai': 'Artificial Intelligence', 'generate': 'Generate', 'error': 'Error', 'success': 'Success'},
    'ar': {'ai': 'الذكاء الاصطناعي', 'generate': 'توليد', 'error': 'خطأ', 'success': 'نجاح'},
    'tzr': {'ai': 'ⵉⵏⵜⴰⵍⵍⵉⴰⵏⴻⵏ ⴰⵙⵉⴷⴰⵡⵉⵏ', 'generate': 'ⴰⴷⵔⴰⵙ', 'error': 'ⴰⵙⴳⴰⴷ', 'success': 'ⴰⵏⴼⴰⵍ'},
    'de': {'ai': 'Künstliche Intelligenz', 'generate': 'Generieren', 'error': 'Fehler', 'success': 'Erfolg'},
    'zh': {'ai': '人工智能', 'generate': '生成', 'error': '错误', 'success': '成功'},
    'ja': {'ai': '人工知能', 'generate': '生成', 'error': 'エラー', 'success': '成功'},
    'ko': {'ai': '인공지능', 'generate': '생성', 'error': '오류', 'success': '성공'},
    'nl': {'ai': 'Kunstmatige Intelligentie', 'generate': 'Genereren', 'error': 'Fout', 'success': 'Succes'},
    'he': {'ai': 'בינה מלאכותית', 'generate': 'ליצור', 'error': 'שגיאה', 'success': 'הצלחה'},
    'fa': {'ai': 'هوش مصنوعی', 'generate': 'تولید', 'error': 'خطا', 'success': 'موفقیت'},
    'hi': {'ai': 'कृत्रिम बुद्धिमत्ता', 'generate': 'जनरेट करें', 'error': 'त्रुटि', 'success': 'सफलता'},
    'es': {'ai': 'Inteligencia Artificial', 'generate': 'Generar', 'error': 'Error', 'success': 'Éxito'},
}

def ai_translate(term: str, lang: str = 'fr') -> str:
    return AI_I18N.get(lang, AI_I18N['fr']).get(term, term)
