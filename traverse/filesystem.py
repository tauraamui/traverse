import logging
import time
from watchdog.observers import Observer

class ChangeType:
    CREATED = 1
    DELETED = 2
    MODIFIED = 3
    NONE = -1


class Change(object):

    def __init__(self, user, dir_name, created_file_name, change_type=None):
        self.user = user
        self.dir_name = dir_name
        self.created_file_name = created_file_name
        if change_type is None:
            self.type = ChangeType.NONE
        else:
            self.type = change_type


observer = Observer()


def register_dir(dir_to_monitor, event_handler, recursive):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    observer.schedule(event_handler, dir_to_monitor, recursive)


def start_monitoring(event_handler):
    observer.start()
    try:
        while True:
            event_handler.update()
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
