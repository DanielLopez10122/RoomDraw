#!/usr/bin/python

from private.sql import *
import private.constants as constants
import private.stored_procs as procs

def get_student_by_id(student_id):
	s = SQL(constants.sql_host, constants.sql_user, constants.sql_db)
	item = s.run_stored_proc_for_single_item(procs.get_student, student_id)
	if not item:
		return None
	return Student(item)

class Student:
	def __init__(self, student_id, first_name, last_name, random_number, grade_level, sex, group_id=None, roommate_id=None):
		self.student_id    = student_id
		self.first_name    = first_name
		self.last_name     = last_name
		self.random_number = random_number
		self.grade_level   = grade_level
		self.sex           = sex
		self.group_id      = group_id
		self.roommate_id   = roommate_id
	def __init__(self, info):
		self.student_id    = info[0]
		self.first_name    = info[1]
		self.last_name     = info[2]
		self.random_number = info[3]
		self.grade_level   = info[4]
		self.sex           = info[5]
		self.group_id      = info[6]
		self.roommate_id   = info[7]
