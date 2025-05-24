# Test unitaire Python – Onboarding
import requests

def test_onboarding_ok():
    r = requests.post('http://localhost:8001/api/onboarding/', json={'email': 'test@dihya.com', 'lang': 'fr'})
    assert r.status_code == 200
    assert 'Bienvenue' in r.json().get('message','')

def test_onboarding_rgpd():
    r = requests.post('http://localhost:8001/api/onboarding/', json={'lang': 'fr'})
    assert r.status_code == 400
    assert 'Email' in r.json().get('error','')
