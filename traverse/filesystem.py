import logging
import time
from watchdog.observers import Observer

observer = Observer()


def register_dir(dir_to_monitor, event_handler, recursive):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    observer.schedule(event_handler, dir_to_monitor, recursive)


def start_monitoring():
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()