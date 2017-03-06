import sys
import filesystem
import eventhandlers
from watchdog.observers import Observer
from traverse import users


class Application(object):
    def __init__(self):
        self.dir_to_monitor = ""
        self.observer = Observer()

    def start(self):
        self.load_params()
        users

    def load_params(self):
        if len(sys.argv) > 1:
            self.dir_to_monitor = sys.argv[1]
        else:
            print "Dir path param missing..."
            exit(-1)


if __name__ == "__main__":
    users = users.load_all_users("traverse.dat")
    app = Application()
    app.start()
