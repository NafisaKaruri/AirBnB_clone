#!/usr/bin/python3
"""This is the user module that defines User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class defines the user attributes
    Attrs:
        email (str): the user's email
        password (str): the user's password
        first_name (str): the user's first name
        last_name (str): the user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
