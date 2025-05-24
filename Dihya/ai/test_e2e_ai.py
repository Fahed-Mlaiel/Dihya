# Dihya AI – Test e2e d’export et d’intégration

import subprocess
import json

def test_export_json():
    result = subprocess.run([
        'python', 'export_ai_rgpd.py', '--export', 'json'
    ], capture_output=True, text=True, check=True)
    log = json.loads(result.stdout)
    assert log["prompt"]
    assert log["response"]
    assert log["lang"] == "fr"
    assert log["engine"] == "mixtral"

def test_generate_fixture():
    result = subprocess.run([
        'python', 'generate_fixture.py'
    ], capture_output=True, text=True, check=True)
    assert "Fixture générée" in result.stdout
