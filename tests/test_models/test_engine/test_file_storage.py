#!/usr/bin/python3
"""This module containt the unittests for the FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """This class tests the FileStorage class"""
    def setUp(self):
        """Sets up the testing environment"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "file.json.temp")
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """Cleans up the testing environment after each test by removing the JSON
        file created"""
        del self.storage
        del self.model
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("file.json.temp"):
            os.rename("file.json.temp", "file.json")

    def test_all(self):
        """Test that all return the __objects dictionary"""
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)
    
    def test_new(self):
        """Test that new adds an object to the __objects dictionary"""
        self.storage.new(self.model)
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, FileStorage._FileStorage__objects)

    def test_save(self):
        """Test that save serializes __objects to the JSON file (path: __file_path)"""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
    
    def test_reload(self):
        """Test that reload deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised)"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = self.model.__class__.__name__ + "." + self.model.id
        self.assertIn(key, FileStorage._FileStorage__objects)
    
    def test_reload_no_file(self):
        """Test that reload does not raise an exception if the JSON file does not
        exist"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)
    
    def test_reload_empty_file(self):
        """Test that reload does not raise an exception if the JSON file is empty"""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write("")
        try:
            self.storage.reload()
        except:
            pass
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)

    def test_reload_invalid_file(self):
        """Test that reload does not raise an exception if the JSON file is invalid"""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write("{")
        try:
            self.storage.reload()
        except:
            pass
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)
    
    def test_reload_invalid_file_format(self):
        """Test that reload does not raise an exception if the JSON file is invalid"""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write("This is not a JSON file")
        try:
            self.storage.reload()
        except:
            pass
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)
    
    def test_reload_invalid_file_content(self):
        """Test that reload does not raise an exception if the JSON file is invalid"""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write("[]")
        try:
            self.storage.reload()
        except:
            pass
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)
    
    def test_reload_invalid_file_content2(self):
        """Test that reload does not raise an exception if the JSON file is invalid"""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write("[{}]")
        try:
            self.storage.reload()
        except:
            pass
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)
    
    def test_reload_invalid_file_content3(self):
        """Test that reload does not raise an exception if the JSON file is invalid"""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            f.write("[{}, {}]")
        try:
            self.storage.reload()
        except:
            pass
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
