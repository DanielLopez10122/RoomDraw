#!/usr/bin/python

from utils import *

_sessions = {}
# _sessions = {"alex": 0, "denton": 1, "eli": 2, "michael": 3}

def id_from_session(session_token):
	if session_token in _sessions:
		return _sessions[session_token]
	return None

# if token is not None, use that for testing purposes
def create_session(student_id, token=None):
	"""
	Create a student and put it into the sessions dictionary
	Returns the session token
	"""
	if token is None:
		# TODO
		token = "random session token"
	_sessions[token] = student_id
	return token

def destroy_session(session_token):
	if session_token in _sessions:
		del _sessions[session_token]
