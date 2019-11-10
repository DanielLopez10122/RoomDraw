#!/usr/bin/python

from sqlalchemy.ext.declarative import declarative_base

OrmModel = declarative_base()
class Model(object):
	def dict(self, exclude=None, keys=None):
		"""Only serialize public variables (for objects) (those that don't start with '_')"""
		dictionary = self.__dict__

		# Return immediately if the user only wants certain keys
		if keys:
			dictionary = {i: dictionary[i] for i in keys if i in dictionary}
			return dictionary

		if exclude:
			dictionary = {key: dictionary[key] for key, _ in dictionary.items() if key not in exclude}

		dictionary = {key: dictionary[key] for key, _ in dictionary.items() if not key.startswith('_')}
		return dictionary
