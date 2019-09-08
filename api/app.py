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
		# self._setup_errors()
		self._setup_endpoints()

	def _setup_cors(self):
		self.cors_middleware = CORS(allow_origins_list=self.allowed_origins)
		self.authentication_middleware = AuthenticationMiddleware()

		self.api = falcon.API(middleware=[self.cors_middleware.middleware, self.authentication_middleware])

	def _setup_errors(self):
		self.api.add_error_handler(Exception, InternalServerError)

	def _setup_endpoints(self):
		# GET, DELETE, ###### DONE
		self.api.add_route("/group", groups.Group())
		self.api.add_route("/group/members", groups.GroupMembers())
		# GET, DELETE, PUT
		self.api.add_route("/group/invite", groups.GroupInvite())
		# GET, PUT, DELETE ###### Done
		self.api.add_route("/group_wishlist", group_wishlist.GroupWishlist())
		# GET, PUT, DELETE ###### Done
		self.api.add_route("/wishlist", student_wishlist.StudentWishlist())
		# GET ###### DONE
		self.api.add_route("/myinfo", student.MyInfo())
		# GET ###### almost DONE
		self.api.add_route("/dorms", dorms.Dorm())
		# GET ###### almost DONE
		self.api.add_route("/rooms", rooms.Room())

api = API()

session.create_session(0, "alex")
session.create_session(1, "denton")
session.create_session(2, "eli")
session.create_session(3, "michael")
