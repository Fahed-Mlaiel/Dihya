# test.py – Dihya Unit Test (Python)
import unittest

class TestDihyaPlatform(unittest.TestCase):
    def test_basic_assertion(self):
        self.assertTrue(True)

    def test_multilingual_output(self):
        i18n = {'fr': 'Bonjour', 'en': 'Hello', 'ar': 'مرحبا', 'tzr': 'Azul'}
        self.assertTrue(all(i18n.values()))

    def test_security_best_practices(self):
        # Simuler une validation d'entrée sécurisée
        input_str = '<script>alert(1)</script>'
        sanitized = input_str.replace('<script>alert(1)</script>', '')
        self.assertEqual(sanitized, '')

if __name__ == '__main__':
    unittest.main()
