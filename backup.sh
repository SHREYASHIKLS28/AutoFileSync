#!/bin/bash

rclone sync /mnt/c/Users/Username/Documents gdrive:DocumentsBackup --log-file=/mnt/c/Users/Username/backup.log --log-level INFO
if [ $? -ne 0 ]; then
    echo "Backup FAILED at $(date)" >> /mnt/c/Users/Username/backup_error.log
    # Call your alert function here
    /mnt/c/Users/Username/send_alert.sh "Backup Failed on $(date)"
fi



