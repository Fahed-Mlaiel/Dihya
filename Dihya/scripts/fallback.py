# Fallback IA open source automatisé Dihya – Tous modules
import os, subprocess

def fallback_all():
    print("[FALLBACK] Lancement du fallback IA open source sur tous les dossiers métiers…")
    folders = [
        'ai', 'assets', 'backend', 'blockchain', 'branding', 'demo', 'design', 'devops', 'docs', 'frontend', 'generation', 'i18n', 'marketplace', 'mobile', 'node', 'plugins', 'scripts', 'securite', 'specs', 'uploads'
    ]
    for folder in folders:
        path = os.path.join('Dihya', folder)
        if os.path.exists(path):
            print(f"[FALLBACK] → {path}")
            subprocess.run(['python3', 'fallback.py'], cwd=path, check=False)
            subprocess.run(['node', 'fallback.js'], cwd=path, check=False)

if __name__ == "__main__":
    fallback_all()
