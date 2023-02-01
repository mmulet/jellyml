from .get_user_data_dir_path import get_user_data_dir_path
from os.path import join


def get_code_path():
    return join(get_user_data_dir_path(), "code")
