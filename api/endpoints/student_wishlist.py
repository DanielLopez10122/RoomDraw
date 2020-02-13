#!/usr/bin/python

from private import *
import models

from utils import *

class StudentWishlist(object):
	def on_get(self, request, response):
		sql = sql_create_session()
		wishlist = sql.query(models.StudentWishlist).filter_by(student_id=self.student_id).all()

		response.media = []
		for item in wishlist:
			response.media.append(item.dict(exclude='student_id'))

	def on_delete(self, request, response):
		rank = INT(request.params.get("rank"))

		sql.query(models.StudentWishlist).filter_by(rank=rank, student_id=self.student_id).delete()
		wishlist = sql.query(models.StudentWishlist).filter(models.StudentWishlist.rank > rank).filter_by(student_id=self.student_id).all()

		for option in wishlist:
			option.rank -= 1
		sql.commit()

	def on_put(self, request, response):
		rank = INT(request.params.get("rank"))
		dorm_id = INT(request.params.get("dorm_id"))
		room_id = INT(request.params.get("room_id"), nullable=True)
		floor = INT(request.params.get("floor"), nullable=True)

		wishlist = sql.query(models.StudentWishlist).filter_by(student_id=self.student_id).all()

		for value in wishlist:
			if value.rank >= rank:
				value.rank += 1

		item = models.StudentWishlist(student_id=self.student_id, rank=rank, dorm_id=dorm_id, room_id=room_id, floor=floor)
		sql.add(item)
		sql.commit()
