import json
from pprint import pprint


class User(object):

    def __init__(self, username, email, folders):
        self.username = username
        self.email = email
        self.folders = folders


def load_all_users(data_file):
    with open(data_file) as data_file:
        data = json.load(data_file)
    pprint(data)
    return data
