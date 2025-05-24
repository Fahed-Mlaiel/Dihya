# Export RGPD automatisé Dihya – Tous modules
import os, subprocess

def export_all():
    print("[EXPORT RGPD] Lancement de l’export RGPD automatisé sur tous les dossiers métiers…")
    folders = [
        'ai', 'assets', 'backend', 'blockchain', 'branding', 'demo', 'design', 'devops', 'docs', 'frontend', 'generation', 'i18n', 'marketplace', 'mobile', 'node', 'plugins', 'scripts', 'securite', 'specs', 'uploads'
    ]
    for folder in folders:
        path = os.path.join('Dihya', folder)
        if os.path.exists(path):
            print(f"[EXPORT RGPD] → {path}")
            subprocess.run(['python3', 'export_rgpd.py'], cwd=path, check=False)
            subprocess.run(['node', 'export_rgpd.js'], cwd=path, check=False)

if __name__ == "__main__":
    export_all()
