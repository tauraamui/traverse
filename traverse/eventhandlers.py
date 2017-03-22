from watchdog.events import FileSystemEventHandler
import core
import travemail
import utils
import users
from filesystem import ChangeType
from filesystem import Change


class EmailNotificationHandler(FileSystemEventHandler):

    def __init__(self, emails_and_folders):
        self.emails_and_folders = emails_and_folders
        self.travemail = travemail.Travemail()

    def on_created(self, event):
        for user in users.load_all_users(core.DAT_FILE):
            for dir_name in user.dirs_to_watch:
                if dir_name in event.src_path:
                    #if user.username != utils.file_owner_name(event.src_path):
                        new_change = Change(user, dir_name, event.src_path, ChangeType.CREATED)
                        self.travemail.cache_change(new_change)

    def on_deleted(self, event):
        #print event
        pass

    def on_modified(self, event):
        #print event
        pass

    def update(self):
        self.travemail.update()
