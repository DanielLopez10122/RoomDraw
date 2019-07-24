#!/usr/bin/python

class Student(dict):
	def __init__(self, info):
		self.info = {}
		self.info["student_id"]    = info[0]
		self.info["first_name"]    = info[1]
		self.info["last_name"]     = info[2]
		self.info["random_number"] = info[3]
		self.info["grade_level"]   = info[4]
		self.info["sex"]           = info[5]
		self.info["group_id"]      = info[6]
		self.info["roommate_id"]   = info[7]
		dict.__init__(self, self.info)
