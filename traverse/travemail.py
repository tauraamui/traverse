import time
import json
import core


def get_email_by_user(user, emails):
    for email in emails:
        if email.user.username == user.username:
            return email
    return None


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
        for change in self.changes:
            email_to_send = get_email_by_user(change.user, emails_to_send)
            if email_to_send is not None:
                email_to_send.file_list.append(change.created_file_name)
            else:
                email_to_send = Email(change.user)
                email_to_send.file_list.append(change.created_file_name)
                emails_to_send.append(email_to_send)


class Email(object):

    def __init__(self, user):
        self.user = user
        self.file_list = []
