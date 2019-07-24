#!/usr/bin/python

class Wishlist(dict):
	def __init__(self, info):
		self.info            = {}
		self.info["rank"]    = info[0]
		self.info["dorm_id"] = info[1]
		self.info["room_id"] = info[2]
		self.info["floor"]   = info[3]
		dict.__init__(self, self.info)
