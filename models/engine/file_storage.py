#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json
import os.path


class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the 'obj' with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f
                )

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)"""
        from models.base_model import BaseModel
        from models.user import User

        class_dict = {
            "BaseModel": BaseModel,
            "User": User
        }

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    FileStorage.__objects[key] = \
                        class_dict[value["__class__"]](**value)
