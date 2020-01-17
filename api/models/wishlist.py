#!/usr/bin/python

from sqlalchemy import Column, Integer, String, Enum
from models.base import Model, OrmModel

class Wishlist(Model, OrmModel):
	rank    = Column(Integer, primary_key=True)
	dorm_id = Column(Integer)
	room_id = Column(Integer)
	floor   = Column(Integer)

class GroupWishlist(Wishlist):
	__tablename__ = 'GroupWishlists'
	group_id      = Column(Integer, primary_key=True)

class StudentWishlist(Wishlist):
	__tablename__ = 'StudentWishlists'
	group_id      = Column(Integer, primary_key=True)
