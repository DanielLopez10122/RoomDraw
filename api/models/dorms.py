#!/usr/bin/python

from sqlalchemy import Column, Integer, String, Enum, LargeBinary

from models.base import OrmModel

class Dorm(OrmModel):
	__tablename__ = 'Dorms'

	dorm_id   = Column(Integer, primary_key=True)
	dorm_code = Column(String)
	dorm_name = Column(String)
	sex       = Column(Enum('M', 'F'))
	photo     = Column(LargeBinary)

