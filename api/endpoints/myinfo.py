#!/usr/bin/python

from private.sql import *
from utils import *
import private.constants as constants
import private.stored_procs as procs
import classes.student

import session

class MyInfo:
	def on_get(self, request, response):
		session_token = get_session(request)
		ID = session.id_from_session(session_token)
		current_student = get_student_by_id(ID)
		if current_student is not None:
			response.media = current_student
		else:
			response.media = "Not authenticated"
			return
