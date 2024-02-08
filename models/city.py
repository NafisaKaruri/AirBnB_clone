#!/usr/bin/python3
"""This is the city module that defines City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This Class defines the City attributes
    Args:
        state_id (str): the State.id
        name (str): the state name"""
    def __init__(self, *args, **kwargs):
        """The class constructor"""
        super().__init__(*args, **kwargs)

        state_id = ""
        name = ""
