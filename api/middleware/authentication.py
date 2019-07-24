#!/usr/bin/python

from falcon import HTTPUnauthorized
from utils import *

class AuthenticationMiddleware(object):
	def process_request(self, request, response):
		session_token = get_session(request)
		if not authenticated(session_token):
			raise HTTPUnauthorized(title="Not authenticated", challenges=["Bearer"])
