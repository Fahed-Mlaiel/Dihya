"""
Dihya – Initialisation avancée du module Templates Éducation
------------------------------------------------------------
Ce package gère la découverte, l’import, l’extension et la sécurisation des templates métiers pour l’éducation (cours, examens, évaluations, IA, plugins).

🇫🇷 Initialisation du package éducation (sécurité, extensibilité, multilingue, souveraineté numérique)
🇬🇧 Education templates package initialization (security, extensibility, multilingual, digital sovereignty)
🇦🇪 تهيئة حزمة قوالب التعليم (الأمان، التوسعة، متعدد اللغات، السيادة الرقمية)
ⵣ Tazwart n templates n tazrawt n tamedyazt (amatu, extensibility, multilingual, tasertit n digital)

Ce fichier rend le dossier importable comme package Python, prêt pour l’extension par plugins, assets, IA, ou scripts métiers.
Aucun code exécutable à l’import. Sécurité maximale. Extensible et multilingue.
"""

import os
from typing import List

SUPPORTED_TEMPLATE_EXTENSIONS = ('.json', '.yaml', '.yml', '.py', '.md', '.pdf')

def discover_education_templates(lang: str = "fr") -> List[str]:
    """
    Découvre dynamiquement tous les templates éducation présents dans le dossier.
    Dynamically discovers all education templates in the directory.
    يكتشف جميع قوالب التعليم في هذا المجلد.
    Ittwazzen akk templates n tazrawt n tamedyazt deg umeslay.

    Args:
        lang (str): Code langue pour la documentation (fr, en, ar, tz). Default: "fr".

    Returns:
        List[str]: Liste des chemins relatifs des templates détectés.

    Sécurité :
        - Ignore les fichiers système ou cachés (__*, .*)
        - Ne lit que les extensions autorisées
        - Aucun code dynamique exécuté

    Extensible :
        - Ajoutez vos templates, assets, scripts ou plugins métiers dans ce dossier

    Multilingue :
        - Voir doc/README pour la documentation multilingue
    """
    templates_dir = os.path.dirname(__file__)
    templates = []
    for fname in os.listdir(templates_dir):
        if (
            fname.endswith(SUPPORTED_TEMPLATE_EXTENSIONS)
            and not fname.startswith('__')
            and not fname.startswith('.')
        ):
            templates.append(fname)
    return templates

__all__ = ['discover_education_templates']

# Sécurité : aucun code exécutable à l’import, pas d’exécution dynamique non contrôlée
# Extensible : ajoutez vos templates, assets, scripts ou plugins métiers dans ce dossier
# Multilingue : voir doc/README pour la documentation multilingue
# Souveraineté numérique : aucun tracking, aucune dépendance cloud propriétaire, 100% open source

# Exemple d’utilisation (à ne pas exécuter à l’import) :
if __name__ == "__main__":
    import json
    print(json.dumps({
        "fr": discover_education_templates("fr"),
        "en": discover_education_templates("en"),
        "ar": discover_education_templates("ar"),
        "tz": discover_education_templates("tz"),
    }, ensure_ascii=False, indent=2))
