#!/usr/bin/python3
"""This module defines the unittests for models/base_model.py"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import json
import os


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class"""

    def setUp(self):
        """Sets up the testing environment"""
        pass

    def tearDown(self):
        """Tears down the testing environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """Tests the initialization of the base model instance"""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))

    def test_init_id(self):
        """Tests the id of the base model instance"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.id), str)

    def test_init_created_at(self):
        """Tests the created_at attribute of the base model instance"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.created_at), datetime)

    def test_init_updated_at(self):
        """Tests the updated_at attribute of the base model instance"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.updated_at), datetime)

    def test_init_kwargs(self):
        """Tests the initialization of the base model instance with kwargs"""
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(isinstance(my_new_model, BaseModel))
        self.assertTrue(my_new_model.name, "ALX")
        self.assertTrue(my_new_model.my_number, 89)

    def test_str(self):
        """Tests the __str__ method of the base model instance"""
        my_model = BaseModel()
        expected = "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.__dict__)
        actual = str(my_model)
        self.assertEqual(expected, actual)

    def test_save(self):
        """Tests the save method of the base model instance"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method of the base model instance"""
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        expected = {
            'id': my_model.id,
            '__class__': my_model.__class__.__name__,
            'created_at': my_model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'updated_at': my_model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'name': "ALX",
            'my_number': 89
        }
        self.assertDictEqual(expected, my_model_json)

    def test_to_dict_isoformat(self):
        """Tests the to_dict method of the base model instance with isoformat
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_json["updated_at"],
                         my_model.updated_at.isoformat())
        self.assertEqual(my_model_json["__class__"], "BaseModel")
