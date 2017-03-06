from watchdog.events import FileSystemEventHandler
import core
import email
import utils
from traverse import users


class EmailNotificationHandler(FileSystemEventHandler):

    def __init__(self, emails_and_folders):
        self.emails_and_folders = emails_and_folders

    def on_created(self, event):
        for user in users.load_all_users(core.DAT_FILE):
            for dir_name in user.dirs_to_watch:
                if dir_name in event.src_path:
                    created_file_name = utils.file_name_in_path(event.src_path)
                    email.send_new_file_notification(user, dir_name, created_file_name)

    def on_deleted(self, event):
        #print event
        pass

    def on_modified(self, event):
        #print event
        pass
