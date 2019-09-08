#!/usr/bin/python

from base64 import b64encode
class Dorm(dict):
	def __init__(self, info):
		self.info = {}
		self.info["id"]    = info[0]
		self.info["code"]  = info[1]
		self.info["name"]  = info[2]
		self.info["sex"]   = info[3]
		self.info["photo"] = b64encode(info[4])
		dict.__init__(self, self.info)
