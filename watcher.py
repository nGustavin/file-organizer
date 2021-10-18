import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import getpass
from organizer import organizer
import os


class Watcher:
    user = getpass.getuser()
    DIRECTORY_TO_WATCH = f"/home/{user}/Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            user = getpass.getuser()
            try:
              organizer(user, f'/home/{user}/types.json')
            except:
              print("Organizer cannot move file, be sure you don't have a file with the same name in the destination folder")