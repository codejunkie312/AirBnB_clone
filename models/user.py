#!/usr/bin/python3
"""This module contains the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a User object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new user"""

        super().__init__(*args, **kwargs)