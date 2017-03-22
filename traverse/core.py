import json
import eventhandlers
from watchdog.events import FileSystemEventHandler
import filesystem


DAT_FILE = "traverse.dat"


class Application(object):

    def __init__(self):
        self.event_handler = eventhandlers.EmailNotificationHandler(FileSystemEventHandler())

    def register_root(self):
        with open(DAT_FILE) as data_file:
            data = json.load(data_file)
            filesystem.register_dir(data["root_dir"], self.event_handler, data["watch_subdirs"])
            data_file.close()


if __name__ == "__main__":
    app = Application()
    app.register_root()
    filesystem.start_monitoring(app.event_handler)
