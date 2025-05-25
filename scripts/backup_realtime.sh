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

  # Synchronisation automatique Git (hors backups)
  git add .
  git commit -m "[AutoSync] Sauvegarde et synchronisation Codespaces -> Git (hors backups)"
  git push
  if [ $? -ne 0 ]; then
    msg "[FR] Erreur de synchronisation Git !" "[EN] Git sync error!" "[AR] خطأ في مزامنة Git!" "[AMZ] Tuccfa n Git!"
    echo "[$(date --iso-8601=seconds)] [ERROR] Git push failed during backup realtime sync." >> backup_realtime.log
    # Notification email (nécessite mailutils/postfix configuré)
    echo "Dihya: Erreur de synchronisation Git lors du backup en temps réel." | mail -s "[Dihya] Git Sync Error" admin@dihya.dev || true
  fi
done
