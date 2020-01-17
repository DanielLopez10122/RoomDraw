#!/usr/bin/python

import falcon
from private import *
import models.dorms
import session

from utils import *
from endpoints.hooks import on_request

@falcon.before(on_request)
class Dorm(object):
	# Get information on dorms
	def on_get(self, request, response):
		response.media = {}
		dorm_id = None
		try:
			dorm_id = int(get_val(request.params, "dorm"))
		except ValueError: # Anything other than an int but not None
			response.media = "Invalid paramaters"
			return
		except TypeError: # if parameter wasn't provided
			pass

		student = get_student_by_id(self.student_id)

		sql = sql_create_session()
		results = sql.query(models.dorms.Dorm).filter_by(sex=student.sex)

		if dorm_id is not None:
			response.media = results.filter_by(dorm_id=dorm_id).first().dict()
		else:
			response.media = []
			for dorm in results:
				response.media.append(dorm.dict())
