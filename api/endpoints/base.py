import session
from utils import *

class Endpoint(object):
	def on_request(self, request, response):
		self.session_token = request.headers.get("SESSION-ID")
		self.student_id = session.get_id(self.session_token)

