import pytest
from meta_logos import meta_logos, get_logo_path
import os

def test_meta_logos_structure():
    assert isinstance(meta_logos, dict)
    assert "description" in meta_logos
    assert "fr" in meta_logos["description"]
    assert meta_logos["accessibility"]["contrast"] == "AAA"
    assert meta_logos["rgpd"]["conformite"] is True
    assert meta_logos["audit"]["result"] == "passed"
    assert "logo-accessibility-checker" in meta_logos["plugins"]
    assert meta_logos["integration"]["django"] is True
    assert meta_logos["integration"]["rest"] is True
    assert meta_logos["integration"]["graphql"] is True

def test_meta_logos_multilingue():
    langs = ["fr", "en", "ar", "tzm", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es"]
    for lang in langs:
        assert lang in meta_logos["description"]

def test_get_logo_path_fallback():
    open(os.path.join(os.path.dirname(__file__), 'dihya-main.svg'), 'a').close()
    path = get_logo_path('dihya-main')
    assert path.endswith('dihya-main.svg')
    os.remove(path)
