# Dihya Fonts – Générateur de fixtures de test

import json
import pytest
from meta_fonts import meta_fonts

def generate_fixture():
    with open('meta_fonts_fixture.json', 'w', encoding='utf-8') as f:
        json.dump(meta_fonts, f, ensure_ascii=False, indent=2)
    print("Fixture générée: meta_fonts_fixture.json")

@pytest.fixture
def meta_fonts_fixture():
    with open('meta_fonts_fixture.json', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    generate_fixture()
