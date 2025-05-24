#!/bin/bash
# backup_realtime.sh – Backup automatisé en temps réel (inotify, logs, multilingue, CI/CD-ready)
# Usage : ./backup_realtime.sh
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

msg "[FR] Surveillance en temps réel des modifications pour backup..." "[EN] Real-time backup monitoring..." "[AR] مراقبة النسخ الاحتياطي في الوقت الحقيقي..." "[AMZ] Amedya n uselkim s wakud..."

WATCH_DIR="/workspaces/Dihya"

while true; do
  inotifywait -r -e modify,create,delete,move "$WATCH_DIR"
  bash /workspaces/Dihya/scripts/backup.sh
  msg "[FR] Backup déclenché automatiquement." "[EN] Backup triggered automatically." "[AR] تم تشغيل النسخ الاحتياطي تلقائيًا." "[AMZ] Amedya yettwazen s wakud."
done
