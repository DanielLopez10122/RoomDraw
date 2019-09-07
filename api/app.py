#!/usr/bin/python

import falcon
from falcon_cors import CORS
from endpoints import *
import session
from middleware.authentication import *
from middleware.exception_handlers import *

class API(object):
	def __init__(self):
		# TODO fix this
		self.allowed_origins = ["*"]
		self._setup_cors()
		self._setup_errors()

	def _setup_cors(self):
		self.cors_middleware = CORS(allow_origins_list=self.allowed_origins)
		self.authentication_middleware = AuthenticationMiddleware()

		self.api = falcon.API(middleware=[self.cors_middleware.middleware, self.authentication_middleware])

	def _setup_errors(self):
		self.api.add_error_handler(Exception, InternalServerError)

	def add_route(self, route, obj):
		self.api.add_route(route, obj)

def main(debug=True):
	api = API()

	# GET, DELETE, ###### DONE
	api.add_route("/group", groups.Group())
	api.add_route("/group/members", groups.GroupMembers())
	# GET, DELETE, PUT
	api.add_route("/group/invite", groups.GroupInvite())
	# GET, PUT, DELETE ###### Done
	api.add_route("/group_wishlist", group_wishlist.GroupWishlist())
	# GET, PUT, DELETE ###### Done
	api.add_route("/wishlist", student_wishlist.StudentWishlist())
	# GET ###### DONE
	api.add_route("/myinfo", student.MyInfo())
	# GET ###### almost DONE
	api.add_route("/dorms", dorms.Dorm())
	# GET ###### almost DONE
	api.add_route("/rooms", rooms.Room())

	if debug:
		# for testing
		session.create_session(0, "alex")
		session.create_session(1, "denton")
		session.create_session(2, "eli")
		session.create_session(3, "michael")
