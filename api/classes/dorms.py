#!/usr/bin/python

class Dorm(dict):
	def __init__(self, info):
		self.info = {}
		self.info["id"]    = info[0]
		self.info["code"]  = info[1]
		self.info["name"]  = info[2]
		self.info["sex"]   = info[3]
		self.info["photo"] = info[4]
		dict.__init__(self, self.info)
