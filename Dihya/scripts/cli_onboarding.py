# CLI Python – Onboarding utilisateur
import requests, argparse
parser = argparse.ArgumentParser()
parser.add_argument('--email', required=True)
parser.add_argument('--lang', default='fr')
args = parser.parse_args()
res = requests.post('http://localhost:8001/api/onboarding/', json={'email': args.email, 'lang': args.lang})
print(res.json())
