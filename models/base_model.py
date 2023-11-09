#!/usr/bin/python3
"""This module contains the base class of all our future classes."""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initializes a new user"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""

        class_name = self.__class__.__name__
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"

        custom_dict = {
            **self.__dict__,
            "__class__": class_name,
            "id": self.id,
            "created_at": self.created_at.strftime(iso_format),
            "updated_at": self.updated_at.strftime(iso_format),
        }

        return custom_dict

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
