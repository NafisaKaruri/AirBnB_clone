#!/usr/bin/python3
"""This is the city module that defines City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This Class defines the City attributes
    Args:
        state_id (str): the State.id
        name (str): the state name"""

    state_id = ""  # it will be the State.id
    name = ""
