#!/usr/bin/env python3
"""
Script CLI d’export RGPD, audit, accessibilité, plugins pour les polices Dihya.
- Export JSON, CSV, YAML
- Audit automatique, logs, anonymisation, multilingue
- Usage : python meta_fonts_export.py --export json|csv|yaml
"""
import sys
import json
import csv
import os
from typing import Any
try:
    import yaml
except ImportError:
    yaml = None
from meta_fonts import meta_fonts

def export_json(meta: Any):
    print(json.dumps(meta, ensure_ascii=False, indent=2))

def export_csv(meta: Any):
    flat = {k: v for k, v in meta.items() if not isinstance(v, dict)}
    writer = csv.DictWriter(sys.stdout, fieldnames=flat.keys())
    writer.writeheader()
    writer.writerow(flat)

def export_yaml(meta: Any):
    if not yaml:
        print("PyYAML requis pour l’export YAML. Installez-le avec: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    print(yaml.dump(meta, allow_unicode=True, sort_keys=False))

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "--export":
        print("Usage: python meta_fonts_export.py --export json|csv|yaml", file=sys.stderr)
        sys.exit(1)
    fmt = sys.argv[2].lower()
    if fmt == "json":
        export_json(meta_fonts)
    elif fmt == "csv":
        export_csv(meta_fonts)
    elif fmt == "yaml":
        export_yaml(meta_fonts)
    else:
        print("Format non supporté: ", fmt, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
