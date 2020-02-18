#!/usr/bin/python

from sqlalchemy import Column, Integer, Enum
from models.base import Model, OrmModel

class Group(Model, OrmModel):
	__tablename__ = 'Groups'

	group_id = Column(Integer, primary_key=True)
	random_number = Column(Integer)
	grade_level = Column(Integer)
	sex = Column(Enum('M', 'F'))

class Invitation(Model, OrmModel):
	__tablename__ = 'GroupInvites'

	student_id = Column(Integer, primary_key=True)
	group_id = Column(Integer, primary_key=True)
