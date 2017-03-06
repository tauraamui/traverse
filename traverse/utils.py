import os


def file_name_in_path(path):
    return os.path.basename(os.path.normpath(path))