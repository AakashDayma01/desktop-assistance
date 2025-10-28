


import os, shutil, time, requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Jenkins trigger URL
JENKINS_URL = "http://Aakash:11ece22e27ebaff5bc55031650d9a193f8@localhost:8080/job/DesktopAssistantPipeline/build?token=CODE_SAVE_TRIGGER_TOKEN"

# Shared folder Jenkins can access (instead of Jenkins workspace)
JENKINS_SYNC_DIR = r"C:\Temp\jenkins_sync"

# Your local project folder
LOCAL_PROJECT = r"C:\Users\LENOVO\Desktop\pythonfiles"

# Ensure Jenkins sync folder exists
os.makedirs(JENKINS_SYNC_DIR, exist_ok=True)

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"[INFO] Detected change in: {event.src_path}")
            try:
                print("[SYNC] Copying local code to Jenkins sync folder...")

                for root, _, files in os.walk(LOCAL_PROJECT):
                    for file in files:
                        if file.endswith(".py"):
                            src = os.path.join(root, file)
                            rel_path = os.path.relpath(src, LOCAL_PROJECT)
                            dest = os.path.join(JENKINS_SYNC_DIR, rel_path)
                            os.makedirs(os.path.dirname(dest), exist_ok=True)

                            # Safe copy — skip locked/in-use files
                            try:
                                shutil.copy2(src, dest)
                            except PermissionError:
                                print(f"[WARN] Skipping locked file: {src}")
                            except Exception as copy_err:
                                print(f"[WARN] Could not copy {src}: {copy_err}")

                # Trigger Jenkins Job
                response = requests.post(JENKINS_URL)
                if response.status_code == 201:
                    print("✅ Jenkins job triggered successfully.")
                else:
                    print(f"⚠️ Jenkins trigger failed (Status: {response.status_code})")
            except Exception as e:
                print(f"❌ Error during Jenkins trigger process: {e}")

# Watch for changes in local project folder
observer = Observer()
event_handler = Watcher()
observer.schedule(event_handler, LOCAL_PROJECT, recursive=True)
observer.start()

print("👀 Watching for changes in Python files...")

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()



