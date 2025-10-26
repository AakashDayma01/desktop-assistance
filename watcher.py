import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            os.system('git add . && git commit -m "auto commit" && git push origin main')

path = '.'
observer = Observer()
event_handler = Watcher()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
