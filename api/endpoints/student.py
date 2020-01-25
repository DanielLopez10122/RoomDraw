#!/usr/bin/python

import falcon
from utils import *
from private import *
import models.student

import session

class Student(object):
	# without an id, return info on current student
	def on_get(self, request, response):
		ID = None
		try:
			ID = int(get_val(request.params, "id"))
		except ValueError:
			response.media = "Invalid ID"
			return
		except TypeError:
			ID = self.student_id

		student = get_student_by_id(ID)
		response.media = student.dict()

class MyInfo(object):
	def on_get(self, request, response):
		raise falcon.HTTPFound("/student")
