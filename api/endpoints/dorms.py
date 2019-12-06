#!/usr/bin/python

from private import *
import models.dorms
import session

from utils import *

class Dorm(Endpoint):
	# Get information on dorms
	def on_get(self, request, response):
		response.media = {}
		try:
			dorm_id = int(get_val(request.params, "dorm"))
		except ValueError: # Anything other than an int but not None
			response.media = "Invalid paramaters"
			return
		except TypeError: # if parameter wasn't provided
			response.media = "No dorm provided"
			return

		if dorm_id:
			results = sql_run_stored_proc_for_single_item(procs.get_single_dorm, dorm_id)
			if results:
				response.media = models.dorms.Dorm(results)
		else:
			results = sql_run_stored_proc_for_multiple_items(procs.get_dorms)

			dorm_list = []
			if results:
				for i in results:
					dorm = models.dorms.Dorm(i)
					dorm_list.append(dorm)

			response.media = dorm_list
