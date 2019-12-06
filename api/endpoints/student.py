#!/usr/bin/python

from utils import *
from private import *
import models.student

import session

class Student(Endpoint):
	# without an id, return info on current student
	def on_get(self, request, response):
		ID = None
		try:
			ID = int(get_val(request.params, "id"))
		except ValueError:
			response.media = "Invalid ID"
			return
		except TypeError:
			ID = self.session_id

		student = get_student_by_id(ID)
		response.media = student.dict()

class MyInfo:
	def on_get(self, request, response):
		s = Student()
		if "id" in request.params:
			del request.params["id"]

		s.on_get(request, response)
