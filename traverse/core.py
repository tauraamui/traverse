import json

import eventhandlers
from watchdog.events import FileSystemEventHandler

import filesystem


DAT_FILE = "traverse.dat"


def register_root():
    with open(DAT_FILE) as data_file:
        data = json.load(data_file)
        filesystem.register_dir(data["root_dir"], eventhandlers.EmailNotificationHandler(FileSystemEventHandler()), data["watch_subdirs"])

if __name__ == "__main__":
    register_root()
    filesystem.start_monitoring()
