#!/usr/bin/python

import json
from private import *
import models.group
import models.student
import session

from utils import *

class Group(Endpoint):
	def on_get(self, request, response):
		# TODO make sure the database is up, otherwise send status code 5xx
		stud = get_student_by_id(self.student_id)
		gid = stud.info["group_id"]

		sql = sql_create_session()
		group = sql.query(models.group.Group).filter_by(group_id=gid).first()

		if group:
			response.media = group.dict(exclude=[sex])
		else:
			response.media = "{}"
	
	def on_delete(self, request, response):
		sql_run_stored_proc(procs.leave_group, self.student_id)

class GroupMembers(Endpoint):
	def on_get(self, request, response):
		response.media = {}
		# TODO make sure the database is up, otherwise send status code 5xx
		stud = get_student_by_id(self.student_id)
		gid = stud.info["group_id"]

		sql = sql_create_session()
		members = sql.query(models.student.Student).filter_by(group_id=gid).all()

		response.media = []
		for person in members:
			response.media.append(person.dict())

class GroupInvite(Endpoint):
	def on_get(self, request, response):
		results = sql_run_stored_proc_for_multiple_items(procs.get_group_invites, self.student_id)

		response.media = []
		if results:
			for inv in results:
				response.media.append(models.group.Invitations(inv))
	# Invite a student
	# TODO prevent student from inviting another to a different group
	def on_post(self, request, response):
		params = json.loads(request.stream.read())
		stud = get_student_by_id(student_id.ID)

		sid = get_val(params, "student_id")
		gid = stud["group_id"]

		if sid is None or gid is None:
			response.media = "Missing parameters"
			return

		sql_run_stored_proc(procs.invite_to_group, sid, gid)

	# Accept an invite
	def on_put(self, request, response):
		params = json.loads(request.stream.read())
		gid = get_val(params, "group_id")

		if gid is None:
			response.media = "Need a group to accept"
			return
		
		sql_run_stored_proc(procs.accept_group_invite, self.student_i, gid)

	# Decline an invite
	def on_delete(self, request, response):
		gid = get_val(request.params, "group_id")

		if gid is None:
			response.media = "Please provide a group id to decline"
			return

		sql_run_stored_proc(procs.decline_group_invite, self.student_id, gid)
