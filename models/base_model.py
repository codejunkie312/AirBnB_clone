#!/usr/bin/python3
""" This module contains the base class of all our future classes. """
import uuid
from datetime import datetime


class BaseModel:
	"""This class defines all common attributes/methods for other classes"""
	
	def __init__(self, *args):
		"""Initializes a new user"""

		self.id = str(uuid.uuid4())
		self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
