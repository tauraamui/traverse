import time
import json
import core


class Travemail(object):

    def __init__(self):
        self.changes = []
        self.time_now = time.time()

    def cache_change(self, change_to_cache):
        self.changes.append(change_to_cache)
        print self.changes

    def update(self):
        data_file = open(core.DAT_FILE)
        data = json.load(data_file)
        if time.time() - self.time_now > data["email_notifciation_rate"]:
            self.time_now = time.time()
            self.send_change_notify_emails()
            self.changes = []

    def send_change_notify_emails(self):
        emails_to_send = []
        existing_email = False
        for change in self.changes:
            for email in emails_to_send:
                if email.user == change.user:
                    existing_email = True
                    if change.created_file_name not in email.email_content:
                        email.email_content.append(change.created_file_name)



class Email(object):

    def __init__(self, user):
        self.user = user
        self.email_content = []
