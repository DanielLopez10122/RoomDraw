#!/usr/bin/python

from private import *
import models.rooms
import session

from utils import *

class Room:
	def on_get(self, request, response):
		response.media = {}
		session_token = get_session(request)

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

		# TODO add option to search for a particular room (not a priority)
		results = sql_run_stored_proc_for_multiple_items(procs.get_rooms,
				dorm, room_number, spots_left, floor)
		room_list = []
		if results:
			for room in results:
				room_list.append(models.rooms.Room(room))
			response.media = room_list
