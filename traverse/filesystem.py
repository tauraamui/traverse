import logging
import time


def register_dir(self, event_handler, recursive):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    self.observer.schedule(event_handler, self.dir_to_monitor, recursive)


def start_monitoring(self):
    self.observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        self.observer.stop()
    self.observer.join()