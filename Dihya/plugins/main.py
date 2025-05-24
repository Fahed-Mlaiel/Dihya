"""
Dihya Plugins – Main Entrypoint (Python)
Gestion, audit, extension, sécurité, compatibilité multi-stack, multilingue, documenté, prêt à l'emploi.
"""
from .plugin import DihyaPlugin
from .metiers import *

def list_plugins():
    return ['DihyaPlugin'] + [name for name in globals() if name.endswith('Plugin')]

if __name__ == '__main__':
    print('Plugins Dihya disponibles :', list_plugins())
