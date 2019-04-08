#!/usr/bin/python

from private.sql import *
from utils import *
import private.constants as constants
import private.stored_procs as procs
import classes.student

import session

class Student:
	# without an id, return info on current student
	def on_get(self, request, response):
		session_token = get_session(request)
		if not authenticated(session_token):
			response.media = "Not authenticated"
			return

		ID = None
		try:
			ID = int(get_val(request.params, "id"))
		except ValueError:
			response.media = "Invalid ID"
			return
		except TypeError:
			ID = session.id_from_session(session_token)

		student = get_student_by_id(ID)
		response.media = student

class MyInfo:
	def on_get(self, request, response):
		s = Student()
		if "id" in request.params:
			del request.params["id"]

		s.on_get(request, response)
