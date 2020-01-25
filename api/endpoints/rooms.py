#!/usr/bin/python

import falcon
from private import *
import models.rooms

from utils import *

class Room(object):
	def on_get(self, request, response):
		response.media = {}

		room_number = get_val(request.params, "number")
		spots_left = get_val(request.params, "spots_left")
		floor = get_val(request.params, "floor")
		dorm = get_val(request.params, "dorm")

		# look for rooms in a certain dorm
		# TODO send correct status code, etc
		if dorm is None:
			response.media = "I need a dorm id to continue"
			return

		try:
			room_number = int(room_number)
			spots_left  = int(spots_left)
			floor       = int(floor)
		except (TypeError, ValueError):
			response.media = "Bad or missing parameter somewhere"
			return

		sql = sql_create_session()
		response.media = sql.query(models.rooms.Room).filter_by(dorm_id=dorm, room_number=room_number, available_spots=spots_left, floor=floor).first().dict()
