# Dihya AI – Générateur de fixtures de test

import json
import pytest
from ai import generate_ai_response

def generate_fixture():
    fixture = generate_ai_response(
        prompt="Génère un template métier pour la gestion RH.",
        user_id="fixture-user",
        lang="fr",
        role="admin"
    )
    with open('ai_fixture.json', 'w', encoding='utf-8') as f:
        json.dump(fixture, f, ensure_ascii=False, indent=2)
    print("Fixture générée: ai_fixture.json")

@pytest.fixture
def ai_fixture():
    with open('ai_fixture.json', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    generate_fixture()
