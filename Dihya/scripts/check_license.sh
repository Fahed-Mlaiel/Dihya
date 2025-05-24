#!/bin/bash
# check_license.sh – Vérification avancée des licences open source (Dihya)
# Usage : ./check_license.sh
# Compatible Linux, CI/CD, Codespaces

set -e

LICENSE_FILES=("LICENSE" "THIRD_PARTY_LICENSES.md" "THIRD_PARTY_DEPENDENCIES.md" "sbom.json" "sbom.lock")

for file in "${LICENSE_FILES[@]}"; do
  if [[ -f "../../$file" ]]; then
    echo "[OK] Fichier $file trouvé."
  else
    echo "[WARN] Fichier $file manquant !"
  fi
done

grep -r --exclude-dir={.git,node_modules,venv,.venv,__pycache__} -E 'license|copyright|gpl|mit|apache|bsd|lgpl|epl|mpl' ../.. || echo "Aucune mention de licence détectée."

echo "Vérification des licences terminée."
