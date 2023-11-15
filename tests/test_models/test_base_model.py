#!/usr/bin/python3
"""This module defines the unittests for models/base_model.py"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from os import path
from models.engine.file_storage import FileStorage
import json


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class"""

    def setUp(self):
        """Sets up the testing environment"""
        self.model = BaseModel()
        self.model.name = "Test model"
        self.model.number = 123

    def tearDown(self):
        """Tears down the testing environment by deleting the instance"""
        del self.model
    
    def test_init(self):
        """Tests the __init__ method"""
        self.assertTrue(isinstance(self.model, BaseModel))
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "number"))

    def test_init_kwargs(self):
        """Tests the __init__ method using kwargs"""
        date = datetime.now()
        date_str = date.isoformat()
        model = BaseModel(id="123", created_at=date_str, updated_at=date_str, name="Test", number=123)
        self.assertTrue(isinstance(model, BaseModel))
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertTrue(hasattr(model, "name"))
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.number, 123)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, date)
        self.assertEqual(model.updated_at, date)

    def test_save(self):
        """Tests the save method"""
        old_updated_at = self.model.updated_at
        self.model.save()
        with open(FileStorage._FileStorage__file_path, "r") as f:
            json_dict = json.load(f)
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertTrue(key in json_dict)
        self.assertEqual(json_dict[key], self.model.to_dict())
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertTrue(isinstance(self.model.updated_at, datetime))
        self.assertTrue(path.isfile(FileStorage._FileStorage__file_path))
        
    
    def test_to_dict(self):
        """Tests the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], 'Test model')
        self.assertEqual(model_dict['number'], 123)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
    
    def test_str(self):
        """Test the __str__ method."""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(f"({self.model.id})", string)
        self.assertIn("'name': 'Test model'", string)
        self.assertIn("'number': 123", string)

if __name__ == "__main__":
    unittest.main()