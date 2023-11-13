#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_instantiation(unittest.TestCase):
    """unittests for testing the BaseModel methods"""

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_one_instance(self):
        self.assertIsInstance(self.model, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertEqual(type(self.model.id), str)
        self.assertEqual(type(self.model.created_at), datetime)
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_unique_id(self):
        b = BaseModel()
        self.assertNotEqual(self.model.id, b.id)

    def test_id_type(self):
        self.assertNotEqual(type(self.model.id), uuid.UUID)


if __name__ == '__main__':
    unittest.main()
