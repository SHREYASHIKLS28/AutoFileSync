import sys
import smtplib
from email.mime.text import MIMEText
import os
import traceback
import time
import zipfile
import subprocess
from datetime import datetime
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler

observer = PollingObserver()

# Email function
def send_email(message):
    sender = "shreyashiofficial28@gmail.com"
    receivers = ["shreyashioff28@gmail.com"]
    password = "prxzrkqsbnjmqoca"  # App password as string

    if not password:
        print("❌ GMAIL_APP_PASSWORD not loaded.")
        return

    msg = MIMEText(message)
    msg['Subject'] = "Backup Alert"
    msg['From'] = sender
    msg['To'] = ", ".join(receivers)

    try:
        print("🔐 Connecting to Gmail SMTP...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, password)
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()
        print("✅ Email sent successfully")
    except Exception as e:
        print("❌ Failed to send email:")
        traceback.print_exc()

# Paths
WATCH_FOLDER = "/home/shreyashikls28/DocumentsToWatch"

BACKUP_DIR = "/mnt/c/Users/91841/DocumentsBackup"
ZIP_PATH = os.path.join(BACKUP_DIR, "backup.zip")

def zip_folder(source_folder, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_folder):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, source_folder)
                zipf.write(full_path, arcname)
    print(f"✅ Folder zipped: {output_zip}")

def upload_to_drive():
    try:
        subprocess.run(["rclone", "copy", ZIP_PATH, "gdrive:backup-folder"], check=True)
        print("✅ Backup uploaded to Google Drive.")
    except subprocess.CalledProcessError:
        print("❌ Failed to upload to Google Drive.")

def backup_and_notify():
    zip_folder(WATCH_FOLDER, ZIP_PATH)
    upload_to_drive()
    send_email("📂 Backup completed and uploaded to Google Drive.")

class BackupHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"🔔 Detected event: {event.event_type} on {event.src_path}")
        print(f"📌 Modified: {event.src_path}")

        backup_and_notify()

    def on_created(self, event):
        print(f"🔔 Detected event: {event.event_type} on {event.src_path}")
        print(f"📁 Created: {event.src_path}")
        backup_and_notify()

    def on_deleted(self, event):
        print(f"🔔 Detected event: {event.event_type} on {event.src_path}")
        print(f"🗑️ Deleted: {event.src_path}")
        backup_and_notify()

def start_file_watcher():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"📡 Watching folder: {WATCH_FOLDER}")
    observer.schedule(BackupHandler(), WATCH_FOLDER, recursive=True)
    print("✅ PollingObserver initialized.")
    observer.start()
    try:
        while True:
            time.sleep(1)
            print(".", end="", flush=True)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_email(sys.argv[1])
    else:
        start_file_watcher()
