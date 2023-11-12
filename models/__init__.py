#!/usr/bin/python3
"""This module manages the storage of our AirBnB project"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
