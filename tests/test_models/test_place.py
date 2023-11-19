#!/usr/bin/python3
"""This module contains the unittests for the Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """This class tests the Place class"""

    def test_place_inheritance(self):
        """Tests that Place class inherits from BaseModel"""
        new_place = Place()
        self.assertIsInstance(new_place, Place)
        self.assertTrue(hasattr(new_place, "id"))
        self.assertTrue(hasattr(new_place, "created_at"))
        self.assertTrue(hasattr(new_place, "updated_at"))

    def test_place_attributes(self):
        """Tests that Place class contains the attribute `city_id`"""
        new_place = Place()
        new_place.city_id = "123456"
        self.assertTrue(hasattr(new_place, "city_id"))
        self.assertTrue(hasattr(new_place, "user_id"))
        self.assertTrue(hasattr(new_place, "name"))
        self.assertTrue(hasattr(new_place, "description"))
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertTrue(hasattr(new_place, "amenity_ids"))
        self.assertEqual(new_place.city_id, "123456")

    def test_place_instance(self):
        """Tests that Place class is correctly instantiated"""
        new_place = Place()
        self.assertIsInstance(new_place, Place)


if __name__ == "__main__":
    unittest.main()
