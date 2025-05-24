# Dihya Fonts – Test e2e d’export et d’intégration

import subprocess
import json

def test_export_json():
    result = subprocess.run([
        'python', 'meta_fonts_export.py', '--export', 'json'
    ], capture_output=True, text=True, check=True)
    meta = json.loads(result.stdout)
    assert meta["name"] == "Dihya Fonts"
    assert meta["rgpd"]["conformite"] is True
    assert meta["accessibility"]["contrast"] == "AAA"

def test_generate_fixture():
    result = subprocess.run([
        'python', 'generate_fixture.py'
    ], capture_output=True, text=True, check=True)
    assert "Fixture générée" in result.stdout
