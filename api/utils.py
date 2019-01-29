#!/usr/bin/python

from private.sql import SQL
import private.stored_procs as procs
import classes.student

def get_session(request):
	return request.headers.get("SESSION-ID")

def get_student_by_id(student_id):
	s = SQL()
	item = s.run_stored_proc_for_single_item(procs.get_student, student_id)
	if not item:
		return None
	return classes.student.Student(item)
