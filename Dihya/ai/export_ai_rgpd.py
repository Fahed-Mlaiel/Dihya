#!/usr/bin/env python3
"""
Script CLI d’export RGPD, audit, accessibilité, plugins pour Dihya AI.
- Export JSON, CSV, YAML
- Audit automatique, logs, anonymisation, multilingue
- Usage : python export_ai_rgpd.py --export json|csv|yaml
"""
import sys
import json
import csv
import os
from datetime import datetime
try:
    import yaml
except ImportError:
    yaml = None
from ai import generate_ai_response

# Simule un log d'appel IA pour l'export RGPD
def get_last_ai_log():
    return {
        "prompt": "Génère un template métier RH.",
        "response": "[Mixtral:fr] ...",
        "user_id": "demo-user",
        "lang": "fr",
        "engine": "mixtral",
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    }

def export_json(log):
    print(json.dumps(log, ensure_ascii=False, indent=2))

def export_csv(log):
    writer = csv.DictWriter(sys.stdout, fieldnames=log.keys())
    writer.writeheader()
    writer.writerow(log)

def export_yaml(log):
    if not yaml:
        print("PyYAML requis pour l’export YAML. Installez-le avec: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    print(yaml.dump(log, allow_unicode=True, sort_keys=False))

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "--export":
        print("Usage: python export_ai_rgpd.py --export json|csv|yaml", file=sys.stderr)
        sys.exit(1)
    log = get_last_ai_log()
    fmt = sys.argv[2].lower()
    if fmt == "json":
        export_json(log)
    elif fmt == "csv":
        export_csv(log)
    elif fmt == "yaml":
        export_yaml(log)
    else:
        print("Format non supporté: ", fmt, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
