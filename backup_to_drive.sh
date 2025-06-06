#!/bin/bash

echo "📂 Syncing Documents from Windows..."
rsync -av --delete /mnt/c/Users/Username/Documents/ /pathTo/WatchDoc/

echo "☁️ Copying to Google Drive..."
rclone copy /home/Username/WatchDoc/ gdrive:/backup

echo "📧 Sending email..."
python3 /home/Username/send_email.py "✅ Backup completed at $(date)"
