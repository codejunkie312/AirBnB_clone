#!/usr/bin/python3
"""This module contains the test case for the state class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """This class tests the state class."""

    def test_state_inheritance(self):
        """Tests that state class inherits from BaseModel."""
        new_state = State()
        self.assertIsInstance(new_state, State)
        self.assertTrue(hasattr(new_state, "id"))
        self.assertTrue(hasattr(new_state, "created_at"))
        self.assertTrue(hasattr(new_state, "updated_at"))

    def test_state_attributes(self):
        """Tests that state class contains the attribute `name`."""
        new_state = State()
        new_state.name = "California"
        self.assertTrue(hasattr(new_state, "name"))
        self.assertEqual(new_state.name, "California")

    def test_state_instance(self):
        """Tests that state class is correctly instantiated."""
        new_state = State()
        self.assertIsInstance(new_state, State)


if __name__ == "__main__":
    unittest.main()
