import os
from sys import platform
from os import stat
from pwd import getpwuid


WINDOWS = 0
LINUX = 1
MAC_OS = 2


def file_name_in_path(path):
    return os.path.basename(os.path.normpath(path))


def get_os():
    if platform == "linux" or platform == "linux2":
        return LINUX
    elif platform == "darwin":
        return MAC_OS
    elif platform == "win32":
        return WINDOWS


def file_owner_name(filename):
    if get_os() == LINUX:
        return getpwuid(stat(filename).st_uid).pw_name