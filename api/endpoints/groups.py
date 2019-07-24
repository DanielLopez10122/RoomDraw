#!/usr/bin/python

import json
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
		session_token = get_session(request)

		student_id = session.id_from_session(session_token)
		connection = sql.SQL()
		connection.run_stored_proc(procs.leave_group, student_id)
		connection.commit()

class GroupMembers:
	def on_get(self, request, response):
		response.media = {}
		# TODO make sure the database is up, otherwise send status code 5xx
		session_token = get_session(request)

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

class GroupInvite:
	def on_get(self, request, response):
		session_token = get_session(request)

		sid = session.id_from_session(session_token)

		connection = sql.SQL()
		results = connection.run_stored_proc_for_multiple_items(procs.get_group_invites, sid)

		d = []
		if results:
			for inv in results:
				d.append(classes.group.Invitations(inv))
			response.media = d
	# Invite a student
	# TODO prevent student from inviting another to a different group
	def on_post(self, request, response):
		session_token = get_session(request)
		params = json.loads(request.stream.read())
		ID = session.id_from_session(session_token)
		stud = get_student_by_id(ID)

		sid = get_val(params, "student_id")
		gid = stud["group_id"]

		if sid is None or gid is None:
			response.media = "Missing parameters"
			return

		connection = sql.SQL()
		connection.run_stored_proc(procs.invite_to_group, sid, gid)
		connection.commit()

	# Accept an invite
	def on_put(self, request, response):
		session_token = get_session(request)
		params = json.loads(request.stream.read())
		ID = session.id_from_session(session_token)
		gid = get_val(params, "group_id")

		if gid is None:
			response.media = "Need a group to accept"
			return
		
		connection = sql.SQL()
		connection.run_stored_proc(procs.accept_group_invite, sid, gid)
		connection.commit()

	# Decline an invite
	def on_delete(self, request, response):
		session_token = get_session(request)

		sid = session.id_from_session(session_token)
		gid = get_val(request.params, "group_id")

		if gid is None:
			response.media = "Please provide a group id to decline"
			return

		connection = sql.SQL()
		connection.run_stored_proc(procs.decline_group_invite, sid, gid)
		connection.commit()
