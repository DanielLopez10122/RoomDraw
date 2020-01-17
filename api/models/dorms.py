#!/usr/bin/python

from sqlalchemy import Column, Integer, String, Enum, LargeBinary

from models.base import Model, OrmModel

class Dorm(Model, OrmModel):
	__tablename__ = 'Dorms'

	dorm_id   = Column(Integer, primary_key=True)
	dorm_code = Column(String)
	dorm_name = Column(String)
	sex       = Column(Enum('M', 'F'))
	photo     = Column(LargeBinary)
