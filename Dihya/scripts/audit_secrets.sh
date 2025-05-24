#!/bin/bash
echo "Recherche de secrets potentiels dans le code..."
grep -r --exclude-dir={.git,node_modules,venv,.venv,__pycache__} -E '(SECRET|TOKEN|PASSWORD|API_KEY|PRIVATE_KEY|DSN|PWD|PASS)[ =:]' ../.. || echo "Aucun secret détecté."
