from watchdog.events import FileSystemEventHandler


class EmailNotificationHandler(FileSystemEventHandler):
    def on_created(self, event):
        print event

    def on_deleted(self, event):
        print event

    def on_modified(self, event):
        print event