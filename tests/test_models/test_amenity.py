#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

import unittest
import models
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class"""

    def test_init(self):
        """Tests the __init__ method"""

        self.assertEqual(Amenity, type(Amenity()))
        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))
        self.assertIn(Amenity(), models.storage.all().values())

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_init_kwargs(self):
        """Tests the __init__ method using kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="123", created_at=dt_iso, updated_at=dt_iso, name="Test", number=123)
        self.assertTrue(isinstance(am, Amenity))
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))
        self.assertTrue(hasattr(am, "name"))
        self.assertEqual(am.name, "Test")
        self.assertEqual(am.number, 123)
        self.assertEqual(am.id, "123")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

if __name__ == "__main__":
    unittest.main()
