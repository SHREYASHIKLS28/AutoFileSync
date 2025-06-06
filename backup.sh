#!/bin/bash

rclone sync /mnt/c/Users/91841/Documents gdrive:DocumentsBackup --log-file=/mnt/c/Users/91841/backup.log --log-level INFO
if [ $? -ne 0 ]; then
    echo "Backup FAILED at $(date)" >> /mnt/c/Users/91841/backup_error.log
    # Call your alert function here
    /mnt/c/Users/91841/send_alert.sh "Backup Failed on $(date)"
fi



