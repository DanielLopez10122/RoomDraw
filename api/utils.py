#!/usr/bin/python

from private.sql import *
from private import stored_procs as procs
import session
import models.student

def get_session(request):
	return request.headers.get("SESSION-ID")

def get_student_by_id(student_id):
	if student_id is None:
		return None

	item = sql_run_stored_proc_for_single_item(procs.get_student, student_id)
	if not item:
		return None
	return models.student.Student(item)

def get_val(dictionary, key):
	return dictionary[key] if key in dictionary else None
