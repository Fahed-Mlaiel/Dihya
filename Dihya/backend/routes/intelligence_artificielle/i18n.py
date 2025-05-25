"""
Internationalisation dynamique ultra avancée pour Intelligence Artificielle (Django routes)
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

IA_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'project': 'Projet IA', 'asset': 'Asset IA', 'created': 'Créé', 'deleted': 'Supprimé'},
    'en': {'project': 'AI Project', 'asset': 'AI Asset', 'created': 'Created', 'deleted': 'Deleted'},
    'ar': {'project': 'مشروع ذكاء اصطناعي', 'asset': 'عنصر ذكاء اصطناعي', 'created': 'تم الإنشاء', 'deleted': 'تم الحذف'},
    'ber': {'project': 'ⴰⵙⴽⴰⵏⴰ ⵏ ⵉⴰⵙⵉⵏⴰⵡⴰⵙ', 'asset': 'ⴰⵙⴰⵏⴻⵔ ⵏ ⵉⴰⵙⵉⵏⴰⵡⴰⵙ', 'created': 'ⴰⴷⵔⴰⵙ', 'deleted': 'ⴰⴷⵔⴰⵙ'},
    'de': {'project': 'KI-Projekt', 'asset': 'KI-Asset', 'created': 'Erstellt', 'deleted': 'Gelöscht'},
    'zh': {'project': '人工智能项目', 'asset': '人工智能资产', 'created': '已创建', 'deleted': '已删除'},
    'ja': {'project': 'AIプロジェクト', 'asset': 'AIアセット', 'created': '作成済み', 'deleted': '削除済み'},
    'ko': {'project': 'AI 프로젝트', 'asset': 'AI 에셋', 'created': '생성됨', 'deleted': '삭제됨'},
    'nl': {'project': 'AI Project', 'asset': 'AI Asset', 'created': 'Aangemaakt', 'deleted': 'Verwijderd'},
    'he': {'project': 'פרויקט בינה מלאכותית', 'asset': 'נכס בינה מלאכותית', 'created': 'נוצר', 'deleted': 'נמחק'},
    'fa': {'project': 'پروژه هوش مصنوعی', 'asset': 'دارایی هوش مصنوعی', 'created': 'ایجاد شد', 'deleted': 'حذف شد'},
    'hi': {'project': 'एआई परियोजना', 'asset': 'एआई संपत्ति', 'created': 'बनाया गया', 'deleted': 'हटाया गया'},
    'es': {'project': 'Proyecto IA', 'asset': 'Recurso IA', 'created': 'Creado', 'deleted': 'Eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return IA_I18N.get(lang, IA_I18N['fr']).get(term, term)
