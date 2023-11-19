#!/usr/bin/python3
"""This module contains the test cases for the review class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """This class tests the review class."""

    def test_review_inheritance(self):
        """Tests that review class inherits from BaseModel."""
        new_review = Review()
        self.assertIsInstance(new_review, Review)
        self.assertTrue(hasattr(new_review, "id"))
        self.assertTrue(hasattr(new_review, "created_at"))
        self.assertTrue(hasattr(new_review, "updated_at"))

    def test_review_attributes(self):
        """Tests that review class contains the attribute `place_id`."""
        new_review = Review()
        new_review.place_id = "123456"
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertEqual(new_review.place_id, "123456")

    def test_review_instance(self):
        """Tests that review class is correctly instantiated."""
        new_review = Review()
        self.assertIsInstance(new_review, Review)


if __name__ == "__main__":
    unittest.main()
