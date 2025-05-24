"""
Dihya – Initialisation du module Templates Banque & Finance
----------------------------------------------------------
Ce package permet la gestion, l’import et l’extension des templates métiers pour la banque et la finance (contrats, relevés, transactions, audits, IA, plugins).

🇫🇷 Initialisation du package banque & finance (sécurité, extensibilité, multilingue)
🇬🇧 Banking & finance templates package initialization (security, extensibility, multilingual)
🇦🇪 تهيئة حزمة قوالب البنوك والمالية (الأمان، التوسعة، متعدد اللغات)
ⵣ Tazwart n templates n lbnk d tlamin (amatu, extensibility, multilingual)

Ce fichier rend le dossier importable comme package Python, prêt pour l’extension par plugins, assets, IA, ou scripts métiers.
"""

import os

def discover_banque_finance_templates():
    """
    Découvre dynamiquement tous les templates banque & finance présents dans le dossier.
    Returns:
        list: Liste des chemins relatifs des templates détectés.
    """
    templates_dir = os.path.dirname(__file__)
    templates = []
    for fname in os.listdir(templates_dir):
        if fname.endswith(('.json', '.yaml', '.yml', '.py', '.md', '.pdf')) and not fname.startswith('__'):
            templates.append(fname)
    return templates

__all__ = ['discover_banque_finance_templates']

# Sécurité : aucun code exécutable à l’import, pas d’exécution dynamique non contrôlée
# Extensible : ajoutez vos templates, assets, scripts ou plugins métiers dans ce dossier
# Multilingue : voir doc/README pour la documentation multilingue
