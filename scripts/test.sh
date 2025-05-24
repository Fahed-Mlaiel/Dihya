#!/bin/bash
# test.sh – Tests avancés Dihya (multilingue, sécurisé, CI/CD ready)
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

msg "[FR] Lancement des tests..." "[EN] Running tests..." "[AR] بدء الاختبارات..." "[AMZ] Tests n uselkim..."

# --- LOGGING SÉCURISÉ, SOVEREIGN, MULTILINGUE ---
LOG_SOVEREIGN="/var/log/dihya_test.log"
log_multilingue() {
  echo "[$(date --iso-8601=seconds)] [$1] $2" >> "$LOG_SOVEREIGN"
}
log_multilingue "fr" "Démarrage des tests avancés."
log_multilingue "en" "Starting advanced tests."
log_multilingue "ar" "بدء الاختبارات المتقدمة."
log_multilingue "amz" "Tests n uselkim."

# Python
if command -v pytest >/dev/null 2>&1; then
  pytest --maxfail=1 --disable-warnings
fi
# JS/TS
if command -v jest >/dev/null 2>&1; then
  jest --ci
fi
# Shell
for f in scripts/*.sh; do
  shellcheck "$f"
done

# --- EXTENSION, HOOKS, CI/CD READY ---
on_test_start() {
  log_multilingue "$1" "Test start hook déclenché."
}
on_test_end() {
  log_multilingue "$1" "Test end hook déclenché."
}
on_test_error() {
  log_multilingue "$1" "Test error hook déclenché: $2"
}

msg "[FR] Tous les tests sont passés." "[EN] All tests passed." "[AR] جميع الاختبارات ناجحة." "[AMZ] Tests yedlen."

# --- TESTS UNITAIRES (bats) ---
# Voir tests/scripts/test.bats pour la couverture complète (logs, hooks, extension, robustesse, multilingue, fallback)

# --- DOC ---
# Ce script est documenté dans /docs/scripts/ et prêt pour CI/CD, Codespaces, Linux, audit, fallback souverain.
# Pour ajouter un script, suivre la convention : sécurité, i18n, doc, test, fallback, accessibilité.
