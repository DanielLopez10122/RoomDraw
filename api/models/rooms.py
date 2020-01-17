#!/usr/bin/python

from sqlalchemy import Column, Integer, String, Enum, LargeBinary

from models.base import Model, OrmModel

class Room(Model, OrmModel):
	__tablename__ = 'Rooms'

	room_number     = Column(Integer, primary_key=True)
	dorm_id         = Column(Integer, primary_key=True)
	capacity        = Column(Integer)
	available_spots = Column(Integer)
	description     = Column(String)
	floor           = Column(Integer)
