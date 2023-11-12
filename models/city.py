#!/usr/bin/python3
"""This module contains the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City"""

    def __init__(*args, **kwargs):
        """Initializes a new State instance"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
