from watchdog.events import FileSystemEventHandler
import core
import email


class EmailNotificationHandler(FileSystemEventHandler):

    def __init__(self, emails_and_folders):
        self.emails_and_folders = emails_and_folders

    def on_created(self, event):

        print event

    def on_deleted(self, event):
        print event

    def on_modified(self, event):
        user = core.User("dkuser1", "dkuser1@testing.com", ["dkuser1"])
        email.send_notification(user)
        print event
