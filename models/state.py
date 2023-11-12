#!/usr/bin/python3
"""This module contains the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state"""

    def __init__(*args, **kwargs):
        """Initializes a new State instance"""
        super().__init__(*args, **kwargs)
        self.name = ""
