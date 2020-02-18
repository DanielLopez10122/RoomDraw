#!/usr/bin/python

import falcon
from private import *
import models
import session

from utils import *

class Dorm(object):
	# Get information on dorms
	def on_get(self, request, response):
		dorm_id = INT(request.params.get("dorm"), nullable=True)

		student = get_student_by_id(self.student_id)

		sql = sql_create_session()
		results = sql.query(models.Dorm).filter_by(sex=student.sex)

		if dorm_id is not None:
			response.media = results.filter_by(dorm_id=dorm_id).first().dict()
		else:
			response.media = []
			for dorm in results:
				response.media.append(dorm.dict())
