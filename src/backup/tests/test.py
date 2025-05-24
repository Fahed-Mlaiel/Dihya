# Test d’intégration backup Dihya Coding
# Sécurité, monitoring, RGPD, accessibilité, CI/CD, plugins, audit
import unittest
from utils.utils import check_backup, check_security, check_monitoring, check_gdpr, check_accessibility, check_ci, check_plugins, check_audit

class TestBackup(unittest.TestCase):
    def test_advanced_backup(self):
        self.assertTrue(check_backup())
        self.assertTrue(check_security())
        self.assertTrue(check_monitoring())
        self.assertTrue(check_gdpr())
        self.assertTrue(check_accessibility())
        self.assertTrue(check_ci())
        self.assertTrue(check_plugins())
        self.assertTrue(check_audit())

if __name__ == '__main__':
    unittest.main()
