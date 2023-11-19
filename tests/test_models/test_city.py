#!/usr/bin/python3
"""This module contains the unittests for the city class."""
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """This class tests the city class."""

    def setUp(self):
        """Sets up the testing environment."""
        self.new_city = City()

    def tearDown(self):
        """Tears down the testing environment."""
        del self.new_city

    def test_city_inheritance(self):
        """Tests that city class inherits from BaseModel."""
        new_city = City()
        self.assertIsInstance(new_city, City)
        self.assertTrue(hasattr(new_city, "id"))
        self.assertTrue(hasattr(new_city, "created_at"))
        self.assertTrue(hasattr(new_city, "updated_at"))

    def test_city_attributes(self):
        """Tests that city class contains the attribute `name`."""
        new_city = City()
        new_city.name = "San Francisco"
        self.assertTrue(hasattr(new_city, "name"))
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertEqual(new_city.name, "San Francisco")

    def test_city_instance(self):
        """Tests that city class is correctly instantiated."""
        new_city = City()
        self.assertIsInstance(new_city, City)

    def test_city_attributes_str(self):
        """Tests that city class attributes are strings."""
        new_city = City()
        self.assertEqual(type(new_city.name), str)

    def test_city_attributes_none(self):
        """Tests that city class attributes are none."""
        new_city = City()
        self.assertEqual(new_city.name, "")

    def test_city_attributes_format(self):
        """Tests that city class attributes are formatted correctly."""
        new_city = City()
        self.assertEqual(new_city.name, "")

    def test_city_attributes_type(self):
        """Tests that city class attributes are of the correct type."""
        new_city = City()
        self.assertEqual(type(new_city.state_id), str)
        self.assertEqual(type(new_city.name), str)

    def test_city_attributes_datetime(self):
        """Tests that city class attributes are datetimes."""
        new_city = City()
        self.assertEqual(type(new_city.created_at), datetime)
        self.assertEqual(type(new_city.updated_at), datetime)

    def test_city_attributes_format(self):
        """Tests that city class attributes are formatted correctly."""
        new_city = City()
        self.assertEqual(new_city.created_at.isoformat(),
                         new_city.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(new_city.updated_at.isoformat(),
                         new_city.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    def test_city_save(self):
        """Tests that city class saves correctly."""
        new_city = City()
        new_city.save()
        self.assertNotEqual(new_city.created_at, new_city.updated_at)

    def test_city_to_dict(self):
        """Tests that city class to_dict method works correctly."""
        new_city = City()
        new_city_dict = new_city.to_dict()
        self.assertEqual(new_city_dict["__class__"], "City")
        self.assertEqual(type(new_city_dict["created_at"]), str)
        self.assertEqual(type(new_city_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
