"""
Dihya – Initialisation du module Templates Beauté & Bien-être
------------------------------------------------------------
Ce package permet la gestion, l’import et l’extension des templates métiers pour la beauté et le bien-être (fiches soins, diagnostics, routines, produits, IA, plugins).

🇫🇷 Initialisation du package beauté (sécurité, extensibilité, multilingue)
🇬🇧 Beauty templates package initialization (security, extensibility, multilingual)
🇦🇪 تهيئة حزمة قوالب الجمال (الأمان، التوسعة، متعدد اللغات)
ⵣ Tazwart n templates n tazwit (amatu, extensibility, multilingual)

Ce fichier rend le dossier importable comme package Python, prêt pour l’extension par plugins, assets, IA, ou scripts métiers.
"""

import os

def discover_beaute_templates():
    """
    Découvre dynamiquement tous les templates beauté présents dans le dossier.
    Returns:
        list: Liste des chemins relatifs des templates détectés.
    """
    templates_dir = os.path.dirname(__file__)
    templates = []
    for fname in os.listdir(templates_dir):
        if fname.endswith(('.json', '.yaml', '.yml', '.py', '.md', '.pdf')) and not fname.startswith('__'):
            templates.append(fname)
    return templates

__all__ = ['discover_beaute_templates']

# Sécurité : aucun code exécutable à l’import, pas d’exécution dynamique non contrôlée
# Extensible : ajoutez vos templates, assets, scripts ou plugins métiers dans ce dossier
# Multilingue : voir doc/README pour la documentation multilingue
