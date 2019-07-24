#!/usr/bin/python

import private.sql as sql
import private.constants as constants
import private.stored_procs as procs
import classes.dorms
import session

from utils import *

class Dorm:
	# Get information on dorms
	def on_get(self, request, response):
		response.media = {}

		session_token = get_session(request)

		try:
			dorm_id = int(get_val(request.params, "dorm"))
		except ValueError: # Anything other than an int but not None
			response.media = "Invalid paramaters"
			return
		except TypeError: # if parameter wasn't provided
			response.media = "No dorm provided"
			return

		connection = sql.SQL()
		if dorm_id:
			results = connection.run_stored_proc_for_single_item(procs.get_single_dorm, dorm_id)
			if results:
				response.media = classes.dorms.Dorm(results)
		else:
			results = connection.run_stored_proc_for_multiple_items(procs.get_dorms)

			dorm_list = []
			if results:
				for i in results:
					dorm = classes.dorms.Dorm(i)
					dorm_list.append(dorm)

			response.media = dorm_list
