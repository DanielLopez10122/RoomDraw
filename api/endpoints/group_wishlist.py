from private import *
import models.wishlist

from utils import *

class GroupWishlist(Endpoint):
	def on_get(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		current_student = get_student_by_id(self.student_id)

		group_id = None
		if current_student:
			group_id = int(current_student["group_id"])

		# TODO Check this
		results = sql_run_stored_proc_for_multiple_items(procs.get_group_wishlist, group_id)

		data = []
		print(results)
		for i in results:
			w = models.wishlist.Wishlist(i)
			data.append(w)
			print(i)
		response.media = data

	def on_delete(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		current_student = get_student_by_id(self.student_id)

		group_id = None
		if current_student:
			group_id = current_student["gid"]

		try:
			rank = int(get_val(request.params, "rank"))
		except ValueError:
			response.media = "Invalid rank"
			return
		except TypeError:
			response.media = "No rank provided"
			return

		if rank is None:
			response.media = "Need a rank"
			return

		sql_run_stored_proc(procs.delete_group_wishlist, group_id, rank)
	
	def on_put(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		current_student = get_student_by_id(self.student_id)

		group_id = None
		if current_student:
			group_id = current_student["gid"]

		try:
			rank     = int(request.params["rank"]) if "rank" in request.params else None
			dorm_id  = int(request.params["dorm_id"]) if "dorm_id" in request.params else None
			room_id  = int(request.params["room_id"]) if "room_id" in request.params else None
			floor    = int(request.params["floor"]) if "floor" in request.params else None
		except ValueError:
			response.media = "Invalid paramaters"
			return

		if not group_id or not rank or not dorm_id:
			response.media = "Missing paramaters"
			return

		sql_run_stored_proc(procs.put_group_wishlist,
				group_id, rank, dorm_id, room_id, floor)
