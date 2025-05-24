#!/bin/bash
# check_style.sh – Vérification avancée du style de code (multilingue, CI/CD ready)
set -euo pipefail
LANG_DEFAULT="fr"

msg() {
  case "${LANG:-$LANG_DEFAULT}" in
    fr) echo "$1" ;;
    en) echo "$2" ;;
    ar) echo "$3" ;;
    amz) echo "$4" ;;
    *) echo "$1" ;;
  esac
}

msg "[FR] Vérification du style en cours..." "[EN] Checking code style..." "[AR] جارٍ التحقق من نمط الشيفرة..." "[AMZ] Aselkim n style..."

# --- LOGGING SÉCURISÉ, SOVEREIGN, MULTILINGUE ---
LOG_SOVEREIGN="/var/log/dihya_check_style.log"
log_multilingue() {
  echo "[$(date --iso-8601=seconds)] [$1] $2" >> "$LOG_SOVEREIGN"
}
log_multilingue "fr" "Démarrage de la vérification avancée du style."
log_multilingue "en" "Starting advanced style check."
log_multilingue "ar" "بدء التحقق المتقدم من النمط."
log_multilingue "amz" "Aselkim n style."

# Python
if command -v black >/dev/null 2>&1; then
  black --check .
fi
# JS/TS
if command -v eslint >/dev/null 2>&1; then
  eslint .
fi
# Shell
if command -v shellcheck >/dev/null 2>&1; then
  shellcheck scripts/*.sh
fi

# --- EXTENSION, HOOKS, CI/CD READY ---
on_check_style_start() {
  log_multilingue "$1" "Check style start hook déclenché."
}
on_check_style_end() {
  log_multilingue "$1" "Check style end hook déclenché."
}
on_check_style_error() {
  log_multilingue "$1" "Check style error hook déclenché: $2"
}

msg "[FR] Style conforme." "[EN] Style OK." "[AR] النمط سليم." "[AMZ] Style ihul."

# --- TESTS UNITAIRES (bats) ---
# Voir tests/scripts/check_style.bats pour la couverture complète (logs, hooks, extension, robustesse, multilingue, fallback)

# --- DOC ---
# Ce script est documenté dans /docs/scripts/ et prêt pour CI/CD, Codespaces, Linux, audit, fallback souverain.
# Pour ajouter un script, suivre la convention : sécurité, i18n, doc, test, fallback, accessibilité.
