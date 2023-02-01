from .get_code_path import get_code_path
from os.path import exists


def have_purchased_code():
    """
    Returns True if the user has purchased a code.
    Again, it's not real security, it's just
    to keep honest people honest.
    """
    code_path = get_code_path()
    if exists(code_path):
        return True
    return False
