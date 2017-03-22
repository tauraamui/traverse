import time
import json
import core
from traverse import utils


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
            email_to_send = get_email_by_user(change.user_to_notify, emails_to_send)
            if email_to_send is not None:
                email_to_send.change_list.append(change)
            else:
                email_to_send = Email(change.user_to_notify)
                email_to_send.change_list.append(change)
                emails_to_send.append(email_to_send)

        for email in emails_to_send:
            #print email.user.username
            #print email.user.email
            print self.create_email_content(email)


    def create_email_content(self, email):
        data_file = open(core.DAT_FILE)
        data = json.load(data_file)
        total_content = "Files have been updated:\n\n"
        for change in email.change_list:
            file_name = utils.file_name_in_path(change.source_path)
            file_owner = utils.file_owner_name(change.source_path)
            complete_path_to_output = change.source_path.replace(data["root_dir"], "").replace(file_name, "")
            total_content += "File "+file_name+" has been created in "+complete_path_to_output+" by user "+file_owner+"\n"
        return total_content


class Email(object):

    def __init__(self, user):
        self.user = user
        self.change_list = []
