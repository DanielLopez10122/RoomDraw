#!/usr/bin/python

import falcon
from private.sql import *
from private import stored_procs as procs
import session
import models.student

def get_session(request):
	return request.headers.get("SESSION-ID")

def get_student_by_id(student_id, session=None):
	if student_id is None:
		return None
	# useful if we want to update data
	if session is None:
		session = sql_create_session()

	return session.query(models.student.Student).filter_by(student_id=student_id).first()

def INT(value, nullable=False):
	"""
	Cast 'value' to int.  On failure, send Bad Request.
	NOTE: Only use for user input such as parameters or headers.
	We don't want to send a Bad Request if it wasn't the user's fault.
	"""
	ret = None
	try:
		ret = int(value)
	except ValueError:
		raise falcon.HTTPBadRequest
	except TypeError:
		if not nullable:
			raise falcon.HTTPBadRequest
		return None
	return ret
