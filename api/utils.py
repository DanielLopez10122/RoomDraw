#!/usr/bin/python

from private.sql import SQL
import session
import private.stored_procs as procs
import classes.student

def get_session(request):
	return request.headers.get("SESSION-ID")

# checks if session_token is valid
def authenticated(session_token):
	return session.id_from_session(session_token) is not None

def get_student_by_id(student_id):
	if student_id is None:
		return None

	s = SQL()
	item = s.run_stored_proc_for_single_item(procs.get_student, student_id)
	if not item:
		return None
	return classes.student.Student(item)

def get_val(dictionary, key):
	return dictionary[key] if key in dictionary else None
