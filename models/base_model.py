#!/usr/bin/python3
"""This module contains the base class of all our future classes."""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new user"""

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""

        class_name = self.__class__.__name__
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        public_attributes = ["id", "created_at", "updated_at"]
        custom_dict = {}
        reversed_dict = dict(reversed(self.__dict__.items()))

        for key, value in reversed_dict.items():
            if key not in public_attributes:
                custom_dict[key] = value

        custom_dict = {
            **custom_dict,
            "__class__": class_name,
            "updated_at": self.updated_at.strftime(iso_format),
            "id": self.id,
            "created_at": self.created_at.strftime(iso_format),
        }

        return custom_dict

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""

        class_name = self.__class__.__name__
        reversed_dict = dict(reversed(self.__dict__.items()))
        return f"[{class_name}] ({self.id}) {reversed_dict}"
