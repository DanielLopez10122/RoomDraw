#!/usr/bin/python

import falcon
import json
from private import *
import models
import session

from utils import *

def reinit_group(group_id, session=None):
	"""Reinitialize the group data based on the "highest-weighted" student"""
	commit = False
	if session is None:
		session = sql_create_session()
		commit = True
	members = get_group_members(group_id, session)
	group = session.query(models.Group).filter_by(group_id=group_id).first()
	# update the group
	group.random_number = min(members, key=lambda student : student.random_number).random_number
	group.grade_level = max(members, key=lambda student : student.grade_level).grade_level
	
	if commit:
		session.commit()

def get_group_members(group_id, session=None):
	if session is None:
		session = sql_create_session()
	return session.query(models.Student).filter_by(group_id=group_id).all()

class Group(object):
	def on_get(self, request, response):
		stud = get_student_by_id(self.student_id)
		gid = stud.group_id

		sql = sql_create_session()
		group = sql.query(models.Group).filter_by(group_id=gid).first()

		response.media = group.dict() if group else "{}"
	
	# Leave the group
	def on_delete(self, request, response):
		sql = sql_create_session()
		student = get_student_by_id(self.student_id, sql)
		old_group = student.group_id

		if student.student_id != old_group:
			student.group_id = self.student_id
		else:
			members = get_group_members(old_group, sql)
			# if not in a group
			if len(members) == 1:
				return
			leader = min(members, key=lambda x : x.random_number)
			old_group = leader.student_id
			for m in members:
				m.group_id = old_group

		reinit_group(old_group, sql)
		reinit_group(student.group_id, sql)

		sql.commit()

class GroupMembers(object):
	def on_get(self, request, response):
		stud = get_student_by_id(self.student_id)
		gid = stud.group_id

		sql = sql_create_session()
		members = get_group_members(gid)

		response.media = []
		for person in members:
			response.media.append(person.dict())

class GroupInvite(object):
	def on_get(self, request, response):
		sql = sql_create_session()
		invitations = sql.query(models.Invitation).filter_by(student_id=self.student_id).all()
		response.media = []
		for inv in invitations:
			response.media.append(inv.dict(exclude='student_id'))

	# Invite a student
	def on_post(self, request, response):
		params = json.loads(request.stream.read())
		stud = get_student_by_id(self.student_id)

		recepient = INT(params.get("student_id"))
		gid = stud.group_id

		sql = sql_create_session()
		invitation = sql.query(models.Invitation).filter_by(student_id=recepient, group_id=gid).first()
		if invitation is not None:
			return
		invitation = models.Invitation(student_id=recepient, group_id=gid)
		sql.add(invitation)
		sql.commit()

	# Accept an invite
	def on_put(self, request, response):
		params = json.loads(request.stream.read())
		gid = INT(params.get("group_id"))

		sql = sql_create_session()
		student = get_student_by_id(self.student_id, sql)
		student.group_id = gid
		reinit_group(gid, sql)

		sql.query(models.Invitation).filter_by(student_id=self.student_id).delete()
		sql.commit()

	# Decline an invite
	def on_delete(self, request, response):
		gid = INT(request.params.get("group_id"))

		sql = sql_create_session()
		sql.query(models.Invitation).filter_by(student_id=self.student_id, group_id=gid).delete()
		sql.commit()
