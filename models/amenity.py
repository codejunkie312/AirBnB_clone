root@f36de9ba658f:~/AirBnB_clone/models# cat state.py 
#!/usr/bin/python3
"""This module contains the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity"""

    def __init__(*args, **kwargs):
        """Initializes a new Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = ""
