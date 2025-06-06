#!/bin/bash

SOURCE="/mnt/c/Users/91841/Documents/"
DEST="/home/shreyashikls28/DocumentsToWatch/"

while true
do
    echo "🔁 Syncing from Windows Documents..."
    rsync -av --delete "$SOURCE" "$DEST"
    sleep 5  # Sync every 5 seconds
done
