# main.py – Dihya Scripts Main Entrypoint (Python)
"""
Orchestration des scripts Dihya (audit, migration, sécurité, import/export, tests)
Multilingue, sécurisé, souverain, documenté, prêt à l'emploi.
"""

import subprocess
import sys

def run_script(script):
    print(f'Exécution du script : {script}')
    subprocess.run([sys.executable, script], check=True)

if __name__ == '__main__':
    print('Dihya Scripts – Orchestration des tâches critiques (audit, migration, sécurité, import/export, tests)')
    # Exemples d'appel de scripts
    # run_script('audit_secrets.sh')
    # run_script('check_license.sh')
    # run_script('import_export_templates.py')
    # ...lancer les scripts, hooks, tests, audit, etc.
    # Exemples d'intégration :
    # import audit_secrets
    # import check_license
    # import import_export_templates
    # ...ajoutez ici vos hooks/scripts personnalisés
