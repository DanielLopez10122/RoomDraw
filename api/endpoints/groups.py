#!/usr/bin/python

import json
import private.sql as sql
import private.constants as constants
import private.stored_procs as procs
import endpoints.student as student
from session import sessions

class Group:
	def on_get(self, request, response):
		session_token = request.headers.get("SESSION-ID")
		current_id = -1
		if session_token in sessions:
			current_id = sessions[session_token]
		else:
			response.media = "Not authenticated"
			return
		stud = student.get_student_by_id(current_id)
		print("Group id is " + str(stud.group_id))

		connection = sql.SQL()
		results = connection.run_stored_proc_for_multiple_items(procs.get_group, stud.group_id)
		if results:
			response.media = str(results)
		else:
			response.media = "{}"
