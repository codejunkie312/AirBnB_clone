#!/usr/bin/python3
"""This module contains the base class of all our future classes."""
import uuid
from datetime import datetime


class BaseModel:
	"""This class defines all common attributes/methods for other classes"""
	
	def __init__(self):
		"""Initializes a new user"""

		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def save(self):
		"""Updates the updated_at attribute with the current datetime"""

		self.updated_at = datetime.now()
	
	def __str__(self):
		"""Returns a string representation of the BaseModel instance"""

		class_name = self.__class__.__name__
		return f"[{class_name}] ({self.id}) {self.__dict__}"
