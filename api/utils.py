#!/usr/bin/python

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

def get_val(dictionary, key):
	return dictionary[key] if key in dictionary else None
