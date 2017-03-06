import logging
import sys
import time

from watchdog.observers import Observer
from eventhandlers import EmailNotificationHandler


class Application(object):
    def __init__(self):
        self.dir_to_monitor = ""
        self.observer = Observer()

    def start(self):
        self.load_params()
        self.register_dir()
        self.start_monitoring()

    def load_params(self):
        if len(sys.argv) > 1:
            self.dir_to_monitor = sys.argv[1]
        else:
            print "Dir path param missing..."
            exit(-1)

    def register_dir(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        event_handler = EmailNotificationHandler()
        self.observer.schedule(event_handler, self.dir_to_monitor, recursive=True)

    def start_monitoring(self):
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


if __name__ == "__main__":
    app = Application()
    app.start()
