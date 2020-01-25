import falcon
from private import *
import models.wishlist

from utils import *
from endpoints.hooks import on_request

@falcon.before(on_request)
class GroupWishlist(object):
	def on_get(self, request, response):
		student = get_student_by_id(self.student_id)
		group_id = student.group_id

		sql = sql_create_session()
		wishlist = sql.query(models.wishlist.GroupWishlist).filter_by(group_id=group_id).all()

		response.media = []
		for item in wishlist:
			response.media.append(item.dict(exclude='group_id'))

	def on_delete(self, request, response):
		student = get_student_by_id(self.student_id)
		sql = sql_create_session()

		group_id = student.group_id

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

		sql.query(models.wishlist.GroupWishlist).filter_by(rank=rank, group_id=group_id).delete()
		wishlist = sql.query(models.wishlist.GroupWishlist).filter(models.wishlist.GroupWishlist.rank > rank)
			.filter_by(group_id=group_id)all()

		for option in wishlist:
			option.rank -= 1
		sql.commit()
	
	def on_put(self, request, response):
		student = get_student_by_id(self.student_id)

		group_id = student.group_id

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

		wishlist = sql.query(models.wishlist.GroupWishlist).filter_by(group_id=group_id).all()

		for value in wishlist:
			if value.rank >= rank:
				value.rank += 1

		item = models.wishlist.GroupWishlist(group_id=group_id, rank=rank, dorm_id=dorm_id, room_id=room_id, floor=floor)
		sql.add(item)
		sql.commit()
