#!/usr/bin/python

import falcon
from utils import *
from private import *
import models

import session

class Student(object):
	# without an id, return info on current student
	def on_get(self, request, response):
		ID = INT(request.params.get("id"), nullable=True)
		if ID is None: ID = self.student_id

		student = get_student_by_id(ID)
		response.media = student.dict()

class MyInfo(object):
	def on_get(self, request, response):
		raise falcon.HTTPFound("/student")
