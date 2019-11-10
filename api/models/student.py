#!/usr/bin/python

from sqlalchemy import Column, Integer, String, Enum
from models.base import Model, OrmModel

class Student(Model, OrmModel):
	__tablename__ = 'Students'

	student_id    = Column(Integer, primary_key = True)
	first_name    = Column(String(64))
	last_name     = Column(String(64))
	random_number = Column(Integer)
	grade_level   = Column(Integer)
	sex           = Column(Enum('M', 'F'))
	group_id      = Column(Integer)
	roommate_id   = Column(Integer)
