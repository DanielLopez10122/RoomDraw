#!/usr/bin/python

from private import *
import models.wishlist
import session

from utils import *

class StudentWishlist:
	def on_get(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		session_token = get_session(request)

		student_id = session.id_from_session(session_token)
		connection = sql.SQL()
		results = connection.run_stored_proc_for_multiple_items(procs.get_student_wishlist, student_id)

		data = []
		for i in results:
			w = models.wishlist.Wishlist(i)
			data.append(w)
		response.media = data

	def on_delete(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		session_token = get_session(request)
		student_id = session.id_from_session(session_token)

		try:
			rank = int(get_value(request.params, "rank"))
		except ValueError:
			response.media = "Invalid rank"
			return
		except TypeError:
			response.media = "Missing rank"
			return

		connection = sql.SQL()

		connection.run_stored_proc(procs.delete_student_wishlist, student_id, rank)
		connection.commit()

	def on_put(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		session_token = get_session(request)

		student_id = session.id_from_session(session_token)

		try:
			rank       = int(get_val(request.params, "rank"))
			dorm_id    = int(get_val(request.params, "dorm_id"))
			room_id    = int(get_val(request.params, "room_id"))
			floor      = int(get_val(request.params, "floor"))
		except ValueError:
			response.media = "Invalid paramaters"
			return
		except TypeError:
			pass

		if not rank or not dorm_id:
			response.media = "Missing paramaters"
			return

		connection = sql.SQL()

		connection.run_stored_proc(procs.put_student_wishlist,
				student_id, rank, dorm_id, room_id, floor)
		connection.commit()
