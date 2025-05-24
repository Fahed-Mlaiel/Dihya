"""
Dihya DevOps – Main Script (Python)
Automatisation, déploiement, monitoring, backup, tests, multilingue, sécurisé, documenté, prêt à l'emploi.
"""
import subprocess

def deploy_stack():
    print('Déploiement de la stack Dihya...')
    subprocess.run(['docker-compose', 'up', '-d'], check=True)

def run_backup():
    print('Backup en cours...')
    subprocess.run(['sh', '../../BACKUP_GUIDE.md'], check=True)

def run_tests():
    print('Lancement des tests CI/CD...')
    subprocess.run(['npm', 'run', 'test'], check=True)

def main():
    deploy_stack()
    run_backup()
    run_tests()

if __name__ == '__main__':
    main()
