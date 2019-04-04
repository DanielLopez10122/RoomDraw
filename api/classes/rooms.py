#!/usr/bin/python

class Room(dict):
	def __init__(self, info):
		self.info = {}
		self.info["room_number"]     = info[0]
		self.info["dorm_id"]         = info[1]
		self.info["capacity"]        = info[2]
		self.info["available_spots"] = info[3]
		self.info["description"]     = info[4]
		self.info["floor"]           = info[5]
		dict.__init__(self, self.info)
