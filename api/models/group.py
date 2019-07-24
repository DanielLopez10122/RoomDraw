#!/usr/bin/python

class GroupInfo(dict):
	def __init__(self, info):
		self.info                  = {}
		self.info["group_id"]      = info[0]
		self.info["random_number"] = info[1]
		self.info["grade_level"]   = info[2]
		dict.__init__(self, self.info)

class Invitations(dict):
	def __init__(self, info):
		self.info                  = {}
		self.info["group_id"]      = info[0]
		self.info["random_number"] = info[1]
		self.info["grade_level"]   = info[2]
		dict.__init__(self, self.info)
