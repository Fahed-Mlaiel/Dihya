# Monitoring automatisé Dihya – Tous modules
import os, subprocess

def monitoring_all():
    print("[MONITORING] Lancement du monitoring automatisé sur tous les dossiers métiers…")
    folders = [
        'ai', 'assets', 'backend', 'blockchain', 'branding', 'demo', 'design', 'devops', 'docs', 'frontend', 'generation', 'i18n', 'marketplace', 'mobile', 'node', 'plugins', 'scripts', 'securite', 'specs', 'uploads'
    ]
    for folder in folders:
        path = os.path.join('Dihya', folder)
        if os.path.exists(path):
            print(f"[MONITORING] → {path}")
            subprocess.run(['python3', 'monitoring.py'], cwd=path, check=False)
            subprocess.run(['node', 'monitoring.js'], cwd=path, check=False)

if __name__ == "__main__":
    monitoring_all()
