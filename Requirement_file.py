# DO NOT USE THIS FILE. YOU MAY COPY ITS CONTENT INTO ANOTHER SCRIPT.

"""
    There are a few libs imported here, their use is only optional
    you may import other libs as well but you need to provide
    a requirements.txt if you use any third-party libs.
"""

import random  # https://docs.python.org/3.6/library/random.html
import sqlite3  # https://docs.python.org/3.6/library/sqlite3.html
import string  # https://docs.python.org/3.6/library/string.html


def generate_password(length: int, complexity: int) -> str:
    """Generate a random password with given length and complexity

    Complexity levels:
        Complexity == 1: return a password with only lowercase chars
        Complexity ==  2: Previous level plus at least 1 digit
        Complexity ==  3: Previous levels plus at least 1 uppercase char
        Complexity ==  4: Previous levels plus at least 1 punctuation char

    :param length: number of characters
    :param complexity: complexity level
    :returns: generated password
    """
    pass


def check_password_level(password: str) -> int:
    """Return the password complexity level for a given password

    Complexity levels:
        Return complexity 1: If password has only lowercase chars
        Return complexity 2: Previous level condition and at least 1 digit
        Return complexity 3: Previous levels condition and at least 1 uppercase char
        Return complexity 4: Previous levels condition and at least 1 punctuation

    Complexity level exceptions (override previous results):
        Return complexity 2: password has length >= 8 chars and only lowercase chars
        Return complexity 3: password has length >= 8 chars and only lowercase and digits

    :param password: password
    :returns: complexity level
    """
    pass


def create_user(db_path: str) -> None:  # you may want to use: http://docs.python-requests.org/en/master/
    """Retrieve a random user from https://randomuser.me/api/
    and persist the user (full name and email) into the given SQLite db

    :param db_path: path of the SQLite db file (to do: sqlite3.connect(db_path))
    :return: None
    """
    pass
