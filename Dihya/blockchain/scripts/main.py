"""
Dihya Blockchain – Main Script (Python)
Gestion, audit, test, extension des smart contracts
Multilingue, sécurisé, souverain, documenté, prêt à l'emploi.
"""
import subprocess
import sys

def audit_contract(contract_path):
    """Audit statique du smart contract (ex: slither, mythril)"""
    try:
        print(f'Audit du contrat {contract_path}')
        subprocess.run(['slither', contract_path], check=True)
        print('Audit terminé.')
    except Exception as e:
        print('Erreur audit:', e)

def test_contracts():
    """Lancer les tests unitaires (ex: brownie test)"""
    try:
        subprocess.run(['brownie', 'test'], check=True)
    except Exception as e:
        print('Erreur tests:', e)

def main():
    audit_contract('./contracts/ProjectManager.sol')
    test_contracts()

if __name__ == '__main__':
    main()
