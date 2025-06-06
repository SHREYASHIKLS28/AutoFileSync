#!/bin/bash

echo "📂 Syncing Documents from Windows..."
rsync -av --delete /mnt/c/Users/91841/Documents/ /home/shreyashikls28/DocumentsToWatch/

echo "☁️ Copying to Google Drive..."
rclone copy /home/shreyashikls28/DocumentsToWatch/ gdrive:/backup

echo "📧 Sending email..."
python3 /home/shreyashikls28/send_email.py "✅ Backup completed at $(date)"
