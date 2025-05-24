# Audit automatisé Dihya – Tous modules
import os, subprocess

def audit_all():
    print("[AUDIT] Lancement de l’audit automatisé sur tous les dossiers métiers…")
    folders = [
        'ai', 'assets', 'backend', 'blockchain', 'branding', 'demo', 'design', 'devops', 'docs', 'frontend', 'generation', 'i18n', 'marketplace', 'mobile', 'node', 'plugins', 'scripts', 'securite', 'specs', 'uploads'
    ]
    for folder in folders:
        path = os.path.join('Dihya', folder)
        if os.path.exists(path):
            print(f"[AUDIT] → {path}")
            subprocess.run(['python3', 'audit.py'], cwd=path, check=False)
            subprocess.run(['node', 'audit.js'], cwd=path, check=False)

if __name__ == "__main__":
    audit_all()
