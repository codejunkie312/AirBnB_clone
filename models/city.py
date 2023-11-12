#!/usr/bin/python3
"""This module contains the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance"""
        super().__init__(*args, **kwargs)
