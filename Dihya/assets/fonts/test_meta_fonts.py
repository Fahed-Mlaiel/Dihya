import pytest
from meta_fonts import meta_fonts, get_font_path
import os

"""
Tests avancés sur les polices Dihya : RGPD, accessibilité, multilingue, plugins, audit, CI/CD.
"""

def test_meta_fonts_structure():
    assert isinstance(meta_fonts, dict)
    assert "description" in meta_fonts
    assert "fr" in meta_fonts["description"]
    assert meta_fonts["accessibility"]["contrast"] == "AAA"
    assert meta_fonts["rgpd"]["conformite"] is True
    assert meta_fonts["audit"]["result"] == "passed"
    assert "font-accessibility-checker" in meta_fonts["plugins"]
    assert meta_fonts["integration"]["django"] is True
    assert meta_fonts["integration"]["rest"] is True
    assert meta_fonts["integration"]["graphql"] is True

def test_meta_fonts_multilingue():
    langs = ["fr", "en", "ar", "tzm", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es"]
    for lang in langs:
        assert lang in meta_fonts["description"]

def test_get_font_path_fallback():
    # Simule la présence d'un fichier pour le fallback
    open(os.path.join(os.path.dirname(__file__), 'lang-fr.ttf'), 'a').close()
    path = get_font_path('fr')
    assert path.endswith('lang-fr.ttf')
    os.remove(path)
