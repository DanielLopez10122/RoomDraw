#!/usr/bin/python

from falcon import HTTPUnauthorized
from utils import get_session
import session

def authenticated(session_token):
	return session.id_from_session(session_token) is not None

class AuthenticationMiddleware(object):
	def process_request(self, request, response):
		if request.method == 'OPTIONS':
			return

		session_token = get_session(request)
		if not authenticated(session_token):
			raise HTTPUnauthorized(title="Not authenticated", challenges=["Bearer"])
