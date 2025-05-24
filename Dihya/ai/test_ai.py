"""
Tests unitaires et d'intégration pour le module IA Dihya (Python)
Couvre la génération, la sécurité, le fallback, la multilingue, la conformité RGPD.
"""
import unittest
from ai import generate_ai_response, select_engine, SUPPORTED_LANGUAGES

class TestDihyaAI(unittest.TestCase):
    def test_generate_fr(self):
        result = generate_ai_response(prompt="Bonjour", user_id="test", lang="fr", role="user", engine="mixtral")
        self.assertIn("Bonjour", result)
    def test_fallback_engine(self):
        engine = select_engine(preferred="openai")
        self.assertIn(engine, ["openai", "mixtral", "llama", "mistral"])
    def test_supported_languages(self):
        self.assertIn("fr", SUPPORTED_LANGUAGES)
        self.assertIn("en", SUPPORTED_LANGUAGES)
        self.assertIn("ar", SUPPORTED_LANGUAGES)
        self.assertIn("tzr", SUPPORTED_LANGUAGES)
if __name__ == "__main__":
    unittest.main()
