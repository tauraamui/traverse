from watchdog.events import FileSystemEventHandler
import core
import email
from traverse import users


class EmailNotificationHandler(FileSystemEventHandler):

    def __init__(self, emails_and_folders):
        self.emails_and_folders = emails_and_folders

    def on_created(self, event):
        for user in users.load_all_users(core.DAT_FILE):
            print user.username
        print event

    def on_deleted(self, event):
        #print event
        pass

    def on_modified(self, event):
        #print event
        pass
