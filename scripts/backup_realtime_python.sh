#!/bin/bash
# backup_realtime_python.sh – Backup automatique en temps réel via inotify et script Python métier
WATCH_DIR="/workspaces/Dihya/Dihya/backend"
while true; do
  inotifywait -r -e modify,create,delete,move "$WATCH_DIR"
  python3 /workspaces/Dihya/Dihya/backend/scripts/backup/main.py
  echo "[INFO] Backup Python déclenché automatiquement."
  sleep 2
  # (optionnel) git add/commit/push ici si besoin
  # (optionnel) notification email ici si besoin
  done
