#!/usr/bin/python3
"""This is the state module that defines State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This Class defines the State attributes
    Args:
        name (str): the state name"""

    name = ""
