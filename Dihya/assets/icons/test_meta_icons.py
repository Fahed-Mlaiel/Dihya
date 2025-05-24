import pytest
from meta_icons import meta_icons, get_icon_path
import os

"""
Tests avancés sur les icônes Dihya : RGPD, accessibilité, multilingue, plugins, audit, CI/CD.
"""

def test_meta_icons_structure():
    assert isinstance(meta_icons, dict)
    assert "description" in meta_icons
    assert "fr" in meta_icons["description"]
    assert meta_icons["accessibility"]["contrast"] == "AAA"
    assert meta_icons["rgpd"]["conformite"] is True
    assert meta_icons["audit"]["result"] == "passed"
    assert "icon-accessibility-checker" in meta_icons["plugins"]
    assert meta_icons["integration"]["django"] is True
    assert meta_icons["integration"]["rest"] is True
    assert meta_icons["integration"]["graphql"] is True

def test_meta_icons_multilingue():
    langs = ["fr", "en", "ar", "tzm", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es"]
    for lang in langs:
        assert lang in meta_icons["description"]

def test_get_icon_path_fallback():
    # Simule la présence d'un fichier pour le fallback
    open(os.path.join(os.path.dirname(__file__), 'accessibility.svg'), 'a').close()
    path = get_icon_path('accessibility')
    assert path.endswith('accessibility.svg')
    os.remove(path)
