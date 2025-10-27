import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 🔧 Jenkins Job Configuration
JENKINS_URL = "http://localhost:8080/job/DesktopAssistantPipeline/build?token=YOUR_TRIGGER_TOKEN"

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"[INFO] Detected change in: {event.src_path}")
            try:
                # Trigger Jenkins Job
                response = requests.post(JENKINS_URL)
                if response.status_code == 201:
                    print("✅ Jenkins job triggered successfully.")
                else:
                    print(f"⚠️ Failed to trigger Jenkins job. Status code: {response.status_code}")
            except Exception as e:
                print(f"❌ Error triggering Jenkins job: {e}")

# 🔍 Watch current directory
path = '.'
observer = Observer()
event_handler = Watcher()
observer.schedule(event_handler, path, recursive=True)
observer.start()

print("👀 Watching for changes in Python files...")

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Stopping watcher...")
    observer.stop()

observer.join()
