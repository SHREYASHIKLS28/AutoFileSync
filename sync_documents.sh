#!/bin/bash

SOURCE="/mnt/c/Users/Username/Documents/"
DEST="/home/WSL-USERNAME/DocumentsToWatch/"

while true
do
    echo "🔁 Syncing from Windows Documents..."
    rsync -av --delete "$SOURCE" "$DEST"
    sleep 5  # Sync every 5 seconds
done
