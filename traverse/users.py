import json
from pprint import pprint


class User(object):

    def __init__(self, username, email, dirs_to_watch):
        self.username = username
        self.email = email
        self.dirs_to_watch = dirs_to_watch


def load_all_users(data_file):
    users = []
    with open(data_file) as data_file:
        data = json.load(data_file)
        new_user = User("", "", [])
        for user_data in data["users"]:
            new_user.username = user_data["username"]
            new_user.email = user_data["email"]
            new_user.folders = user_data["dirs_to_watch"]
            users.append(new_user)
    return users
