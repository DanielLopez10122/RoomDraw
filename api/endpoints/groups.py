#!/usr/bin/python

import private.sql as sql
import private.constants as constants
import private.stored_procs as procs
import classes.group as group
import classes.student as student
import session

from utils import *

class Group:
	def on_get(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		session_token = get_session(request)
		if not authenticated(session_token):
			response.media = "Not authenticated"
			return

		ID = session.id_from_session(session_token)
		stud = get_student_by_id(ID)
		gid = stud.info["group_id"]

		connection = sql.SQL()
		results = connection.run_stored_proc_for_single_item(procs.get_group, gid)

		if results:
			g = group.GroupInfo(results)
			response.media = g
		else:
			response.media = "{}"
	
	def on_delete(self, request, response):
		# TODO add stored proc for leaving the group
		session_token = get_session(request)
		if not authenticated(session_token):
			response.media = "Not authenticated"
			return

		student_id = session.id_from_session(session_token)
		connection = sql.SQL()
		connection.run_stored_proc(procs.leave_group, student_id)
		connection.commit()

class GroupMembers:
	def on_get(self, request, response):
		response.media = {}
		# TODO make sure the database is up, otherwise send status code 5xx
		session_token = get_session(request)
		if not authenticated(session_token):
			response.media = "Not authenticated"
			return

		ID = session.id_from_session(session_token)
		stud = get_student_by_id(ID)
		gid = stud.info["group_id"]

		connection = sql.SQL()
		results = connection.run_stored_proc_for_multiple_items(procs.get_group_members, gid)

		group_list = []
		if results:
			for person in results:
				group_list.append(student.Student(person))
			response.media = group_list

# TODO do this!
class GroupInvite:
	def on_get(self, request, response):
		session_token = get_session(request)
		if not authenticated(session_token):
			response.media = "Not authenticated"
			return

		ID = session.id_from_session(session_token)
		results = connection.run_stored_proc_for_multiple_items(procs.get_group_members, gid)

		invitations = []
		if results:
			for inv in results:
				invitations.append(Groups.Invitations(inv))
			response.media = invitations
	# Invite a student
	def on_put(self, request, response):
		session_token = get_session(request)
		if not authenticated(session_token):
			response.media = "Not authenticated"
			return
