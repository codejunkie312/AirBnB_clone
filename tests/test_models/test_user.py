#!/usr/bin/python3
"""This module contains the test cases for the User class"""
import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up method for User tests."""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "Code"
        self.user.last_name = "Junkie"

    def tearDown(self):
        """Tear down method."""
        del self.user

    def test_init(self):
        """Test the __init__ method."""
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "Code")
        self.assertEqual(self.user.last_name, "Junkie")

    def test_init_kwargs(self):
        """Test initialization with keyword arguments."""
        date = datetime.now()
        date_str = date.isoformat()
        user = User(email="user@example.com", password="root", 
                    first_name="Jane", last_name="Smith", 
                    created_at=date_str, updated_at=date_str)
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "root")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")
        self.assertEqual(user.created_at, date)
        self.assertEqual(user.updated_at, date)

    def test_str(self):
        """Test the __str__ method."""
        string_representation = str(self.user)
        self.assertIn("[User]", string_representation)
        self.assertIn("test@example.com", string_representation)
        self.assertIn("Code", string_representation)
        self.assertIn("Junkie", string_representation)

if __name__ == '__main__':
    unittest.main()
