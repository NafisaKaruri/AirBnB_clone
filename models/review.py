#!/usr/bin/python3
"""This is the review module that defines Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This Class defines the Review attributes
    Args:
        place_id (str): the Place.id
        user_id (str): the User.id
        text (str): the review"""

    place_id = ""
    user_id = ""
    text = ""
